import PIL
from resizeimage import resizeimage
from PIL import Image
##############################################################
# 1.The aspect ratio of an image describes the proportional  #
# relationship between its width and height.                 #
# 2.image.size function returns a list of width and height   #
#   where size[0] is the width and size[1] is height.        #
# 3.aspect ratio is calculated as width / height             #
# 4.Using the aspect ratio new height is calculated using the#
#   new defined width of the image                           #
##############################################################


try:
	filename = "C:/Users/Yash Makwana/Desktop/Project/13_left.jpeg"
	new_width = 512
	with Image.open(filename) as image:

		aspect_ratio = image.size[0] / image.size[1]
		print("Aspect Ratio:", aspect_ratio)
		print("Width:", image.size[0])
		print("Height:", image.size[1])

		new_height = int((new_width / aspect_ratio))
		print("New Width:", new_width)
		print("New Height:", new_height)

		image = resizeimage.resize_cover(image, [new_width, new_height], validate = False)
		image.save('13_left.jpeg', image.format)

except IOError as e:
	raise e