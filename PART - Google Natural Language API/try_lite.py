'''
python try_lite.py
'''

from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

def analyze_sentiment(content):

	client = language_v1.LanguageServiceClient()
	if isinstance(content, six.binary_type):
		content = content.decode('utf-8')
	type_ = enums.Document.Type.PLAIN_TEXT
	document = {'type': type_, 'content': content}
	response = client.analyze_sentiment(document)
	sentiment = response.document_sentiment
	
	return sentiment.score , sentiment.magnitude


if __name__ == '__main__':
	aaa = '0  On National Voter Registration Day, its up to us as citizens to make sure everyone we know can make their voices h https:t.corYRdykNARc'
	print('The content to analyze is:\n{}\nThe sentiment score of it is: [{}]' . format(aaa, analyze_sentiment(aaa)[0]))
