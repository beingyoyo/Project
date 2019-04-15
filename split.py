import PIL
from PIL import Image

try:
	filename = "C:/Users/sniha/Desktop/train/140_left.jpeg"
	
	with Image.open(filename) as image:

		#aspect_ratio = image.size[0] / image.size[1]
		#print("Aspect Ratio:", aspect_ratio)
		print("Width:", image.size[0])
		print("Height:", image.size[1])
		print(image.palette)
		m=image.size[0]//2
		n=image.size[1]//2
		print(image.getcolors(maxcolors=256))
		print(image.split()[2].show())
		#print(image.getpixel(12))

		rgb_im = image.convert('RGB')
		r, g, b = rgb_im.getpixel((512,512))
		print(r, g, b)
		#crop=image.crop((0,0,m,n))
		#crop.load()
		#crop.save("C:/Users/sniha/Desktop/DR/1",image.format)
		
		#image = resizeimage.resize_cover(image, [new_width, new_height], validate = False)
		#image.save('13_left.jpeg', image.format)

except IOError as e:
	raise e
