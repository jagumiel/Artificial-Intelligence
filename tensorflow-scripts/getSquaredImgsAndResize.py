import PIL
import glob
import os
from PIL import Image

files = glob.glob('*.jpg')
image_size = 100

for file in files:
	im1 = Image.open(file)
	width, height = im1.size
	if(width==height):
		im1 = im1.convert("RGB")
		im1 = im1.resize((image_size, image_size))
		filename=os.path.splitext(file)[0]
		print(filename)
		im1.save('resizedSquare/'+filename+'_100x100.jpg')