import PIL
from PIL import Image
from resizeimage import resizeimage

try:
	filename = "C:/Users/sniha/Desktop/train/16_right.jpeg"
	
	with Image.open(filename) as image:
		image.show(title="Original")

		#Calculate aspect ratio where image.size[0] is width & image.size[1] is height
		aspect_ratio = image.size[0] / image.size[1]

		#Compute new height keeping width constant as 512
		new_width = 512
		new_height = int((new_width / aspect_ratio))

		#resize and display
		image = resizeimage.resize_cover(image, [new_width, new_height], validate = False)
		image.show(title="Resized")

except IOError as e:
	raise e