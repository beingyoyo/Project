import image_slicer
from PIL import ImageDraw,ImageFont

try:
	filename = "C:/Users/sniha/Desktop/train/16_right.jpeg"
		
	tiles=image_slicer.slice(filename,4)
	print(tiles)

	#The PIL Image object can be accessed with Tile.image
	for tile in tiles:
		tile.image.show()

except IOError as e:
	raise e