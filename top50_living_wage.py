import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('livingwage50states.csv')
coutries = np.array(data['state_territory'])
wage_single_adult = np.array(data['oneadult_nokids'])
wage_one_child = np.array(data['oneadult_onekid'])
wage_two_child = np.array(data['oneadult_twokids'])

print(wage_two_child)
print('Mean of 50 States:', wage_two_child.mean())
print('Minuimn of 50 States', wage_two_child.min())
print('Max of 50 States', wage_two_child.max())

plt.style.use(['dark_background'])

plt.grid(color='w', linestyle='solid')
plt.title('Living wage for One Adult with two kids')
plt.xlabel('USD')
plt.ylabel('Number of Coutries')
plt.hist(wage_two_child)
plt.show()
