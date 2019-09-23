from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

def analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    print('Content: {}'.format(content))
    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}\n'.format(sentiment.magnitude))

if __name__ == '__main__':
	aaa = 'We lost the game again!'
	analyze_sentiment(aaa)
	bbb = 'Go fuck yourself.'
	analyze_sentiment(bbb)
	ccc = 'I love you so much.'
	analyze_sentiment(ccc)
	ddd = 'We shall fight in the fields and in the streets, we shall fight in the hills, we shall never surrender!'
	analyze_sentiment(ddd)
	eee = 'Freedom has many difficulties and democracy is not perfect, but we have never had to put a wall up to keep our people in, to prevent them from leaving us.'
	analyze_sentiment(eee)
