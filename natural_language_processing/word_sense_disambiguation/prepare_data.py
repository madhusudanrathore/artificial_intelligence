import numpy as np
import ast
import gensim as GS
from keras.preprocessing.text import Tokenizer

'''GET LIST FROM TXT FILE'''
with open('stored_data/sentences.txt', 'r') as file_pos_tag:
    sentence_list = ast.literal_eval(file_pos_tag.read())

# data = np.loadtxt('../data/semcor.gold.key.bnids.txt', usecols=(1), dtype='string')

# word_keys=list()#LIST TO HOLD KEYS FOR WORD
# word_pos=list()#LIST TO HOLD KEY'S PART OF SPEECH TAG
# temp_data=list()

# for i in xrange(len(data)):
# 	temp_data.append(str(data[0]).replace('bn:', ''))
# 	word_pos.append(temp_data[i][-1])
# 	word_keys.append(temp_data[i][:-1])

# word_keys = np.array(word_keys)#CONVERT TO NUMPY ARRAY
# word_keys = word_keys.astype(np.int)#CONVERT TO INT TYPE

# print word_pos[0], type(word_pos[0]), len(word_pos)
# print word_keys[0], type(word_keys[0]), len(word_keys)

# with open('sentences.txt', 'r') as file_sent:#OPEN LIST STORED IN TXT FILE AS A LIST
#     sen_list = ast.literal_eval(file_sent.read())#AND STORE IT

# a=sen_list[0]

# #a.split(' ')

# [i.split(' ', 1)[0] for i in a]

# print type(sen_list), type(sen_list[0]), a, type(a)

'''PREPARE WORD EMBEDDINGS OF WORDS READ FROM SENTENCE'''
model=GS.models.Word2Vec(sentence_list, min_count=1)
print type(model['the']), type(model)

# '''GENERATE ONE HOT ENCODINGS OF 5 POS TAGS'''
# ENC_ADJ=[1,0,0,0,0]
# ENC_ADV=[0,1,0,0,0]
# ENC_ADV=[0,0,1,0,0]
# ENC_ADV=[0,0,0,1,0]
# ENC_X=  [0,0,0,0,1]
