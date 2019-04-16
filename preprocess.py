import PIL
from PIL import Image
from resizeimage import resizeimage

class preprocess:
	def __init__(self,f):
		self.filename=f

		try:
			self.image=Image.open(filename)

		except IOError as e:
			raise e

	def resize(self):
		self.image.show(title="Original")

		#Calculate aspect ratio where image.size[0] is width & image.size[1] is height
		aspect_ratio = self.image.size[0] / self.image.size[1]

		#Compute new height keeping width constant as 512
		new_width = 512
		new_height = int((new_width / aspect_ratio))

		#resize and display
		#image = resizeimage.resize_cover(image, [new_width, new_height], validate = False)
		image = self.image.resize((new_width,new_height), Image.ANTIALIAS)
		image.show(title="Resized")

filename = "C:/Users/sniha/Desktop/train/16_right.jpeg"
	
obj=preprocess(filename)
obj.resize()