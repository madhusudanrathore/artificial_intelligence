import ast
from keras.preprocessing.text import Tokenizer

with open('sentences.txt', 'r') as file_sent:#OPEN LIST STORED IN TXT FILE AS A LIST
    sen_list = ast.literal_eval(file_sent.read())#AND STORE IT

with open('pos_tags.txt', 'r') as file_pos_tag:#OPEN LIST STORED IN TXT FILE AS A LIST
    pos_tag_list = ast.literal_eval(file_pos_tag.read())#AND STORE IT

#TOKENIZE ALL THE SENTENCES
t = Tokenizer()
t.fit_on_texts(sen_list)
#INTEGER ENCODE ALL SENTENCES
encoded_docs = t.texts_to_sequences(sen_list)#THIS SERVES AS 'WORDS_ID' IN OUR TENSORFLOW MODEL
#print len(encoded_docs)
# for i in xrange(len(sen_list)):
# 	print encoded_docs[i]