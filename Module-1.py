import PIL
import pandas
from PIL import Image

filename = "C:/Users/Yash Makwana/Desktop/Project/13_left.jpeg"
try:
	with Image.open(filename) as image:
		
		
		aspect_ratio = image.size[0] / image.size[1]
		print("Width:", image.size[0])
		print("Height:", image.size[1])
		#image.resize((basewidth, baseheight), PIL.Image.ANTIALIAS)
		#image.save('resized_13_left.jpeg')
except IOError as e:
	raise e