from PIL import Image

# Open the image
img = Image.open("./img/carlos_pic.jpg")

# Set the dimensions to crop the image to
width = 256
height = 256

# Get the current image dimensions
img_width, img_height = img.size

# Calculate the aspect ratios
aspect_ratio_img = img_width / img_height
aspect_ratio_crop = width / height

# Crop the image
if aspect_ratio_crop > aspect_ratio_img:
    # Crop the width
    new_width = img_height * aspect_ratio_crop
    left = (img_width - new_width) / 2
    top = 0
    right = left + new_width
    bottom = img_height
else:
    # Crop the height
    new_height = img_width / aspect_ratio_crop
    left = 0
    top = (img_height - new_height) / 2
    right = img_width
    bottom = top + new_height

img_cropped = img.crop((left, top, right, bottom))

# Save the cropped image
img_cropped.save("example_cropped.jpg")
