#from nltk.corpus import stopwords ('english')
#http://www.nltk.org/book/ch02.html

def stopwords():

    stopwords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours',
               'ourselves', 'you', 'your', 'yours', 'yourself',
               'yourselves', 'he', 'him', 'his', 'himself',
               'she', 'her', 'hers', 'herself', 'it', 'its',
               'itself', 'they', 'them', 'their', 'theirs',
               'themselves', 'what', 'which', 'who', 'whom',
               'this', 'that', 'these', 'those', 'am', 'is',
               'are', 'was', 'were', 'be', 'been', 'being',
               'have', 'has', 'had', 'having', 'do', 'does',
               'did', 'doing', 'a', 'an', 'the', 'and', 'but',
               'if', 'or', 'because', 'as', 'until', 'while',
               'of', 'at', 'by', 'for', 'with', 'about',
               'against', 'between', 'into', 'through',
               'during', 'before', 'after', 'above', 'below',
               'to', 'from', 'up', 'down', 'in', 'out', 'on',
               'off', 'over', 'under', 'again', 'further',
               'then', 'once', 'here', 'there', 'when', 'where',
               'why', 'how', 'all', 'any', 'both', 'each',
               'few', 'more', 'most', 'other', 'some', 'such',
               'no', 'nor', 'not', 'only', 'own', 'same', 'so',
               'than', 'too', 'very', 's', 't', 'can', 'will',
               'just', 'don', 'should', 'now', 'd', 'll', 'm',
               'o', 're', 've', 'y', 'ain', 'aren', 'couldn',
               'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn',
               'ma', 'mightn', 'mustn', 'needn', 'shan',
               'shouldn', 'wasn', 'weren', 'won', 'wouldn']
    
    return stopwords

# If nltk_stopwords.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
     
     list_of_stop_words=stopwords()
     print(list_of_stop_words)
     print(len(list_of_stop_words))
     

