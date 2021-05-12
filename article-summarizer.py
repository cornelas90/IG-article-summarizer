import nltk
import requests
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer as Summarizer 
from sumy.nlp.stemmers import Stemmer 
from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing 
from wand.display import display
from wand.font import Font
nltk.download('punkt')

url = 'https://jacobinmag.com/2021/05/service-industry-workers-minimum-wage-welfare-benefits-coronavirus'
image_url = 'https://images.jacobinmag.com/wp-content/uploads/2021/05/05161536/GettyImages-1307438432.jpg'
image_blob = requests.get(image_url)
with Image(blob=image_blob.content) as img:
	print(img.size)
'''
## article summarizer code block
article = Article(url)
article.download()
article.parse()

print(article.images)  
LANGUAGE = 'english'
SENTENCES_COUNT = 10

parser = PlaintextParser.from_string(article.text, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)
summarizer = Summarizer(stemmer)

for sentence in summarizer(parser.document, SENTENCES_COUNT):
	print(sentence)
'''

dims = (1080, 1920)
ideal_width = dims[0]
ideal_height = dims[1]
ideal_aspect = ideal_width / ideal_height
with Image(blob = image_blob.content) as img:
	size = img.size

width = size[0]
height = size[1]
aspect = width / height
CAPTION1 = 'Business owners around the country are offering up a lament:\
		“no one wants to work.” A McDonalds franchise said they had to close because no one wants to work;\
		North Carolina congressman David Rouzer claimed that a too-generous welfare state has turned us all lazy as he circulated photos\
		of a shuttered fast-food restaurant supposedly closed “due to NO STAFF."'

CAPTION2 = 'They find that food and agricultural workers morbidity rates increased by the widest margins by far,\
			 much more so than medical professionals or other occupations generally considered to be on the “front lines”\
			 of the pandemic. Within the food industry, the morbidity rates of line cooks increased by 60 percent,\
			 making it the deadliest profession in America under coronavirus pandemic.'
##Cropping original photos
if aspect > ideal_aspect:
	new_width = int(ideal_aspect * height)
	offset = (width-new_width) / 2
	resize = ((0, 0,  int(new_width), int(height)), (int(width-new_width), 0, int(width), int(height)))
else:
	new_height = int(width / ideal_aspect)
	offset = (height - new_height) / 2
	resize = ((0, 0, int(width), int(new_height)), (0, int(height - new_height), int(width), int(height)))


'''
with Image(blob = image_blob.content) as canvas:
	with Drawing() as draw:
		draw.stroke_width = 2
		draw.fill_color = Color('red')
		draw.fill_opacity = 0.5
		draw.stroke_color = Color('red')
		draw.stroke_opacity = .5
		draw.rectangle(left = 500, top = 500, width = 500, height = 500)
		draw.draw(canvas)
	print(canvas.width)
	canvas.crop(*resize[0])
	print(canvas.width)
	canvas.font = Font('Times-Bold.otf', color = Color('white'))
	caption_width = int(canvas.width/1.2)
	margin_left = int((canvas.width-caption_width)/2)
	margin_top = int(canvas.height/2)
	canvas.caption(CAPTION1, gravity = 'north_west', width = caption_width, left = margin_left, top = margin_top)

	canvas.format = 'jpg'
	canvas.save(filename = 'text_overlayed_1.jpg')
'''
with Drawing() as draw:
	with Image(blob = image_blob.content) as canvas:
		draw.stroke_width = 2
		draw.fill_color = Color('red')
		draw.fill_opacity = 0.5
		draw.stroke_color = Color('red')
		draw.stroke_opacity = .5
		draw.rectangle(left = 500, top = 500, width = 500, height = 500)
		draw.draw(canvas)
		print(canvas.width)
		canvas.crop(*resize[0])
		print(canvas.width)
		canvas.font = Font('Times-Bold.otf', color = Color('white'))
		caption_width = int(canvas.width/1.2)
		margin_left = int((canvas.width-caption_width)/2)
		margin_top = int(canvas.height/2)
		canvas.caption(CAPTION1, gravity = 'north_west', width = caption_width, left = margin_left, top = margin_top)

		canvas.format = 'jpg'
		canvas.save(filename = 'text_overlayed_1.jpg')

with Image(blob = image_blob.content) as canvas:
	canvas.crop(*resize[1])
	canvas.font = Font('Times-Bold.otf', color = Color('White'))
	canvas.fill_color = Color('white')
	canvas.caption(CAPTION2, gravity = 'south_east', width = caption_width, left = margin_left, top = margin_top)
	canvas.format = 'jpg'
	canvas.save(filename = 'text_overlayed_2.jpg')