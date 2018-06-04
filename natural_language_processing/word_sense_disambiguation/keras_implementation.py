import ast
import gensim as GS
import PrepareData as PD
from numpy import array, asarray, zeros
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, Embedding

'''GET DATA'''
docs=PD.docs
labels=PD.labels

'''PREPARE TOKENIZER'''
t = Tokenizer()
t.fit_on_texts(docs)
vocab_size = len(t.word_index) + 1

'''ENCODE INTEGER DOCS'''
encoded_docs = t.texts_to_sequences(docs)

'''PAD DOCUMENTS TO LENGTH OF 300 WORDS'''
max_length = 300
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')


'''LOAD EMBEDDINGS'''
# embeddings_index = dict()
# f = open('../glove_dataset/glove.6B.100d.txt')
# for line in f:
# 	values=line.split()
# 	word=values[0]
# 	coefs=asarray(values[1:], dtype='float32')
# 	embeddings_index[word]=coefs
# f.close()
# print('Loaded %s word vectors.' % len(embeddings_index))
'''CREATE WEIGHT MATRIX FOR WORDS IN TRAINING DOCS'''
# embedding_matrix = zeros((vocab_size, 100))
# for word, i in t.word_index.items():
# 	embedding_vector = embeddings_index.get(word)
# 	if embedding_vector is not None:
# 		embedding_matrix[i] = embedding_vector


'''IMPLENT USING WORD2VEC'''
# model2=GS.models.Word2Vec.load('stored_train_data/w2v_model_file.model')
# embedding_of_key=model2.wv
# print embedding_of_key['program']

# embedding_matrix = zeros((vocab_size, 100))
# for sentence, i in len(docs):
# 	for word in sentence:
# 		if embedding_of_key[word] is not None:
# 			embedding_matrix[i] = embedding_of_key[word]


# '''MODEL'''
# model = Sequential()
# model.add(Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=300, trainable=False))
# model.add(Flatten())
# model.add(Dense(1, activation='sigmoid'))

# '''COMPILE THE MODEL'''
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

# '''SUMMARIZE THE MODEL'''
# print(model.summary())

# '''FIT THE MODEL'''
# model.fit(padded_docs, labels, epochs=3, batch_size=64 , verbose=0)

# '''EVALUATE THE MODEL'''
# loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
# print('Accuracy: %f' % (accuracy*100))