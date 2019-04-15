import PIL
from PIL import Image

try:
	filename = "C:/Users/sniha/Desktop/train/16_right.jpeg"
	
	with Image.open(filename) as image:

		#image.split() returns a tuple comprising of 3 images, one for each r, g & b
		print(image.split())

		image.split()[0].show()
		image.split()[1].show()
		image.split()[2].show()

except IOError as e:
	raise e