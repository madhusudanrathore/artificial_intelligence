import ast
import csv
import numpy as np
import gensim as GS

'''DEFINE FEATURES'''
with open('stored_train_data/sentences.txt', 'r') as file_sentences_list:
    sentence_list = ast.literal_eval(file_sentences_list.read())

docs=[]#HOLDS ALL SENTENCES
for sentence in sentence_list:
	for word in sentence:
		docs.append( ' '.join(word) )

'''PREPARE EMBEDDINGS MODEL OF WORDS READ FROM SENTENCE USING GENSIM WORD2VEC'''
w2v_model=GS.models.Word2Vec(sentence_list, size=100)
w2v_model.save('stored_train_data/w2v_model_file.model')#SAVE THE MODEL
# print type(w2v_model['the']), type(w2v_model), len(w2v_model.wv.vocab), w2v_model['the']


'''DEFINE LABELS'''
word_pos_list=[]
raw_data=open('stored_train_data/word_pos.csv', 'r')
reader=csv.reader(raw_data)
for row in reader:
	word_pos_list.append(row)

labels=[]
for word_pos in word_pos_list:
	if word_pos[1] == 'ADV':
		labels.append(0)
	elif word_pos[1] == 'NOUN':
		labels.append(1)
	elif word_pos[1] == 'ADP':
		labels.append(2)
	elif word_pos[1] == 'PRT':
		labels.append(3)
	elif word_pos[1] == 'DET':
		labels.append(4)
	elif word_pos[1] == 'PRON':
		labels.append(5)
	elif word_pos[1] == 'VERB':
		labels.append(6)
	elif word_pos[1] == 'X':
		labels.append(7)
	elif word_pos[1] == 'NUM':
		labels.append(8)
	elif word_pos[1] == 'CONJ':
		labels.append(9)
	elif word_pos[1] == 'ADJ':
		labels.append(10)
