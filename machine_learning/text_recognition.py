from PIL import Image
from pytesseract import image_to_string

#img = Image.open('/Code/SentimentAnalysis/example_01.png')
#print(image_to_string(img))

img2 = Image.open('/Code/SentimentAnalysis/kinder.jpg')
print(image_to_string(img2))
#print image_to_string(Image.open('test-english.jpg'), lang='eng')