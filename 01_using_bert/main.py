from summarizer import Summarizer
from pprint import pprint
import urllib.request

text = 'India Today News breaks the most important stories in and from India and abroad in six sections - India News, Business News, Cinema News, Sports News, World News and Lifestyle News. India News keeps tab of every development in all parts of India. Business News has the latest business updates from India and abroad. Cinema News tracks the latest from Bollywood, Hollywood and the South film industries and TV channels. Sports News has all the sports from India and abroad with a special focus on cricket. Lifestyle News presents developments that impact ones lifestyle. World News makes sense of news across the world and its impact on India'

model = Summarizer()

result = model(text, num_sentences=1, min_length=60)

full = ''.join(result)

pprint(full)
