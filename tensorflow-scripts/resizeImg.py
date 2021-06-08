import PIL
import glob
import os
from PIL import Image

files = glob.glob('*.jpeg')
image_size = 320

for file in files:
	im1 = Image.open(file)
	im1 = im1.convert("RGB")
	im1 = im1.resize((image_size, image_size))

	filename=os.path.splitext(file)[0]
	print(filename)
	im1.save('resized320/'+filename+'_320x320.jpeg')








