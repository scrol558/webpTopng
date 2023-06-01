import os
from convertator import Convert


image_webp = input("Enter the path to the webp file: ")

# Get the absolute path to the file
absolute_path = os.path.abspath(image_webp)

# Extract the filename without the path
file_name = os.path.basename(absolute_path)

# Generate the *.png file name
image_png = os.path.splitext(file_name)[0] + ".png"

Cn = Convert(absolute_path, image_png)

if __name__ == '__main__':
    Cn.main()
    print("Successful!")
