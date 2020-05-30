import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
import numpy as np
from PIL import Image
import re 
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer



currdir = os.path.dirname(__file__)

def get_wiki(query):
	title = wikipedia.search(query)[0]
	page =  wikipedia.page(title)
	return page.content

        
        

def create_wordcloud(text):
	mask = np.array(Image.open(os.path.join(currdir,"C:/Users/sgsox/Desktop/15 days/coursera and other certificates/wordcloud-example-master/cloud.png")))
	stop = set(STOPWORDS)
	wc = WordCloud(background_color="white",mask=mask,max_words=200,stopwords=stop)
	messages = nltk.sent_tokenize(text)
	corpus=[]
	lemmatizer = WordNetLemmatizer()
	stemmer = PorterStemmer()
	for i in range(len(messages)):
  		temporary = re.sub('[^a-zA-Z]',' ',messages[i])
  		temporary = temporary.lower()
  		temporary = temporary.split()
  		temporary = [stemmer.stem(word) for word in temporary if word not in set(stopwords.words('english'))]
  		temporary = ' '.join(temporary)
  		corpus.append(temporary)

	listToStr = ' '.join([str(elem) for elem in corpus]) 
	wc.generate(listToStr)
	wc.to_file(os.path.join(currdir,"wc2.png"))

	corpus2=[]
	for i in range(len(messages)):
  		temp = re.sub('[^a-zA-Z]',' ',messages[i])
  		temp = temp.lower()
  		temp = temp.split()
  		temp = [lemmatizer.lemmatize(word) for word in temp if word not in set(stopwords.words('english'))]
  		temp = ' '.join(temp)

  		corpus.append(temporary)

	listToStr = ' '.join([str(elem) for elem in corpus]) 
	wc.generate(listToStr)
	wc.to_file(os.path.join(currdir,"wc.png"))

	


create_wordcloud(get_wiki("Hollywood")) 