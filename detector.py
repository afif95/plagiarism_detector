import sys

def preprocess_common(text):
    removables = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't",
                  "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by",
                  "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
                  "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have",
                  "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him",
                  "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is",
                  "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself",
                  "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our",
                  "ours	ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's",
                  "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs",
                  "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
                  "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't",
                  "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's",
                  "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
                  "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself",
                  "yourselves"]
    removables2 = ["[", "]", "{", "}", "“", "’", "”", "!", "\"" "#", "$", "%", "&", "'", "(", ")", "*", "+", "-", ".",
                   "/", ":", ";", "<", "=", ">", "?", "@", "\\", "^", "_", "`", "|", "~", "\"", ","]
    text = text.lower()
    text = ''.join([text[i] for i in range(len(text)) if text[i] not in removables2])
    text = ' '.join(word for word in text.split() if word not in removables)
    return text.split()

def output_generator(newfile1, newfile2, dic1, dic2, hold_length):
    counter = 0
    for per_word in newfile2:
        per_word_length = len(per_word)
        if (per_word_length > 0):
            if per_word in newfile1:
                counter += min(dic1[per_word], dic2[per_word])
    value = 100 * counter / hold_length
    if(value > 50):
        print(1)
    else:
        print(0)

def conv_dictionary(file_list):
    dic = {}
    for element in file_list:
        if(element in dic):
            dic[element] +=1
        else:
            dic[element] = 1
    return dic

def conv_list(dic):
    return [key for key in dic]


f1 = sys.argv[1]
f2 = sys.argv[2]

f1 = open(f1, "r")
file1 = f1.read()
newfile1 = preprocess_common(file1)
hold_length1 = len(newfile1)
dic1 = conv_dictionary(newfile1)
newfile1 = conv_list(dic1)

f2 = open(f2, "r")
file2 = f2.read()
newfile2 = preprocess_common(file2)
hold_length2 = len(newfile2)
dic2 = conv_dictionary(newfile2)
newfile2 = conv_list(dic2)

output_generator(newfile1, newfile2, dic1, dic2, hold_length2)

