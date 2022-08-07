import os

# Function to rename multiple files

folder = "Vol.01 Ch.0003 - Confesión en la azotea. (es-la) [5-Hanayome Translations]"
for count, filename in enumerate(os.listdir(folder)):
    dst = f"Color {str(count)}.jpg"
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"

        # rename() function will
        # rename all the files
    os.rename(src, dst)

# Driver Code
