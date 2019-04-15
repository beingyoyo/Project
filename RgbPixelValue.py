import PIL
from PIL import Image

try:
	filename = "C:/Users/sniha/Desktop/train/16_right.jpeg"
	
	with Image.open(filename) as image:

		#Convert the image into rgb format and save as rgb_im
		rgb_im = image.convert('RGB')

		#Determine the rgb value at position (x,y) using function rgb_im.getpixel((x,y))
		r, g, b = rgb_im.getpixel((512,512))
		print(r, g, b)

except IOError as e:
	raise e