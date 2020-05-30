import pandas as pd
import re 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

messages = pd.read_csv('SMSSpamCollection',sep='\t',names=["label","message"])
#print(messages)

corpus = [] #intializing an empty list / corpus for our paragraph data
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

for i in range(len(messages)):
  temporary = re.sub('[^a-zA-Z]',' ',messages['message'][i])
  temporary = temporary.lower()
  temporary = temporary.split()
  temporary = [stemmer.stem(word) for word in temporary if word not in set(stopwords.words('english'))]
  temporary = ' '.join(temporary)
  corpus.append(temporary)
print(corpus)
