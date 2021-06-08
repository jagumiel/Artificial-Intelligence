import PIL
import glob
import os
from PIL import Image

files = glob.glob('*.png')

for file in files:
	im1 = Image.open(file)
	filename=os.path.splitext(file)[0]
	print(filename)
	im1.save(filename+'.jpeg')
