# class BarcodeReader:

import cv2
import zxingcpp
from PIL import Image

img = cv2.imread('./images/jerky_barcode.png')
# img = Image.open('./images/coke_barcode.png')
# img = Image.open('./images/jerky_barcode.png')
# img.show()
results = zxingcpp.read_barcodes(img)
for result in results:
	print("Found barcode:\n Text:    '{}'\n Format:   {}\n Position: {}"
		.format(result.text, result.format, result.position))
if len(results) == 0:
	print("Could not find any barcode.")