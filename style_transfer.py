import pandas as pd
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import torch
import torch.optim as optim

from torchvision import transforms, models
from PIL import Image
from io import BytesIO
from google.colab import files

vgg = models.vgg19(pretrained=True).features

for param in vgg.parameters():
  param.requires_grad_(False)

def load_image(img, max_size=128, shape=None):

    image = cv.imread(img, 1)

    # large images will slow down processing
    if max(image.size) > max_size:
        size = max_size
    else:
        size = max(image.size)

    if shape is not None:
        size = shape

    in_transform = transforms.Compose([
                        transforms.Resize(size),
                        transforms.ToTensor(),
                        transforms.Normalize((0.485, 0.456, 0.406),
                                             (0.229, 0.224, 0.225))])

    # discard the transparent, alpha channel (that's the :3) and add the batch dimension
    image = in_transform(image)[:3,:,:].unsqueeze(0)

    return image

content = cv.imread(files.upload())
style = load_image(files.upload())

def imcovert(tensor):
  image = tensor.to('cpu').clone().detach()
  image = image.np().squeeze()
  image = image.transpose(1, 2,0)
  image = image * np.array((0.299, 0.224, 0.225)) + np.array((0.485, 0.456, 0.406))
  image = image.clip(0, 1)

  return image

fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(20,10))
axis1.imshow(imcovert(content))
axis2.imshow(imcovert(style))

def get_features(image, model, layers=None):
  if layers is None:
    layers = {'0': 'conv1_1',
              '5': 'conv2_1',
              '10': 'conv3_1',
              '19': 'conv4_1',
              '21': 'conv4_2',
              '28': 'conv5_1'}
  features = {}
  x = image

  for name, layer in model._modules.items():
    x = layer(x)
    if name in layers:
      features[layers[name]] = x

  return features

def gram_matrix(tensor):
  _, d, h, w = tensor.size()

  tensor = tensor.view(d, h * w)

  gram = torch.mm(tensor, tensor.t())

  return gram

content_features = get_features(content, vgg)
style_features = get_features(style, vgg)

style_gram = {layer: gram_matrix(style_features[layer]) for layer in style_features}

style_weight = {'conv1_1': 1,
                'conv2_1': 0.75,
                'conv3_1': 0.2,
                'conv4_1': 0.2,
                'conv5_1': 0.2}
content_weight = 1
style_weight = 1e3

show_every = 400

optimziser = optim.Adam([target], lr-0.003)
steps = 2000

for ii in range(1, steps+1):
  target_features = get_features(target, vgg)
  content_loss = torch.mean((target_features['conv4_2'] - content_features['conv4_2']) ** 2)
  style_loss = 0

  for layer in style_weight:
    target_feature = target_features[layer]
    target_gram = gram_matrix(target_feature)
    _, d, w, h = target_feature.shape
    style_gram = style_gram[layer]
    layer_style_loss = style_weight[layer] * torch.mean((target_gram - style_gram) ** 2)
    style_loss += layer_style_loss / (d * h * w)

  total_loss = content_weight * content_loss + style_weight * style_loss

  optimziser.zero_grad()
  total_loss.backward()
  optimziser.step()

  if ii % show_every == 0:
    print('Total loss: {total_loss.item()}')
    plt.imshow(im_convert(target))
    plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
ax1.imshow(im_convert(content))
ax2.imshow(im_convert(target))
target = content.clone().requires_grad_(True).to(decive)
