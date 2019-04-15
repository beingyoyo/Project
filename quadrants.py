import PIL
from PIL import Image

try:
	filename = "C:/Users/sniha/Desktop/train/16_right.jpeg"
	
	with Image.open(filename) as image:

		#p=width, q=height, m=half of width, n=half of height
		p=image.size[0]
		q=image.size[1]
		m=p//2
		n=q//2
		print(p,q,m,n)

		#image.crop(x1,y1,x2,y2) crops the image taking as input (x1,y1):top left co-ordinates & (x2,y2):bottom right co-ordinates

		#Quadrant 1
		image.crop((m,0,p,n)).show()

		#Quadrant 2
		image.crop((0,0,m,n)).show()	

		#Quadrant 3			
		image.crop((0,n,m,q)).show()

		#Quadrant 4
		image.crop((m,n,p,q)).show()	

except IOError as e:
	raise e