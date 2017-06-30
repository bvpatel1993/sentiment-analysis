
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import pylab as pl
import numpy as np
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
from sklearn.cluster import KMeans

from sklearn.metrics.pairwise import cosine_similarity
import json

stopwords = ["a", "about","quot","u", "2016","amp" ,"above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

tweets = []
with open("positive/all_cities_positive.txt", 'r') as tweet_data:
    tweets = tweet_data.readlines()


# Extract the vocabulary of keywords
lines = dict()
for tweet_text in tweets:
    for char in tweet_text.split():
        char = char.lower()
        if len(char) > 2 and char not in stopwords:
            if lines.has_key(char):
                lines[char] = lines[char] + 1
            else:
                lines[char] = 1

# Remove chars whose frequencies are less than a threshold (e.g., 15)
vocab = {char: freq for char, freq in lines.items() if freq > 20}
# Generate an id (starting from 0) for each char in vocab
vocab = {char: idx for idx, (char, freq) in enumerate(vocab.items())}

# Generate X
X = []
for tweet_text in tweets:
    x = [0] * len(vocab)
    chars = [char for char in tweet_text.split() if len(char) > 2]
    for char in chars:
        if vocab.has_key(char):
            x[vocab[char]] += 1
    X.append(x)

# K-means clustering
km = KMeans(n_clusters = 9, n_init = 85) # try 100 different initial centroids
km.fit(X)

cluster = []
data = dict()
# Print tweets that belong to cluster 2
for idx, cls in enumerate(km.labels_):
    if data.has_key(cls):
        data[cls] += 1
    else:
        data[cls] = 1
    open('cluster/cluster-{0}.txt'.format(cls), 'a').write(json.dumps(tweets[idx]) + '\r\n')
print 'total number of clusters: {0}\r\n'.format(len(data))
#for cls, count in raw_data.items():
