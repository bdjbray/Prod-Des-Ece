#!/usr/bin/env python

'''
python ana_sentiment_main.py
'''

from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

list_rdb = []
list_ctt = []
rdb = [' ', '!', '&', '(', ')', '-', ':', ';', '\'', '\"', ',', '.', '?']

def analyze_sentiment(content):

	client = language_v1.LanguageServiceClient()
	if isinstance(content, six.binary_type):
		content = content.decode('utf-8')
	type_ = enums.Document.Type.PLAIN_TEXT
	document = {'type': type_, 'content': content}
	response = client.analyze_sentiment(document)
	sentiment = response.document_sentiment
	
	return sentiment.score , sentiment.magnitude

def get_content(the_path):
	file = open(the_path, encoding="utf8", errors='ignore')
	for n in range(0,5):
		lines_ctt = file.readline(10000000000)
		s = [i for i in lines_ctt if (str.isalnum(i) or i in rdb)]
		s2 = ''.join(s)
		list_rdb.append(s2)
		list_ctt.append(lines_ctt)


if __name__ == '__main__':
	
	# to get twitter content, type in the txt path
	get_content("./trump.txt")

	# analyze the most recent 5 twitters
	set_num = 5
	sum_score = 0
	print('\nThe twitters to analyze are:\n')
	for i in range(0, set_num):
		aaa = analyze_sentiment(list_rdb[i])[0]
		print('{}\n#  Sentiment score of this one is: [{:+.5f}]\n\n\n\n' . format(list_ctt[i] , aaa))
		sum_score += aaa

	print('***********************************')
	print('Average Sentiment Score: {:+.4f}' . format(sum_score/set_num))
	print('***********************************')
