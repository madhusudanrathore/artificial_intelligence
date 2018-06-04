import tensorflow as tf
import numpy as np
import ast
import gensim as GS
import PrepareData as PD

'''READING AND SPLITTING EMBEDDINGS WORDS AND VECTORS'''
embeddings_words=list()
embeddings_values=list()
f = open('../glove_dataset/glove.6B.50d.txt')
for line in f:
	read_line = line.split()
	word = read_line[0]#GET THE EMBEDDING WORD
	value = np.asarray(read_line[1:], dtype='float32')#GET THE EMBEDDING VALUE VECTOR
	embeddings_words.append(word)
	embeddings_values.append(value)
f.close()

embeddings_words=np.array(embeddings_words)#CONVERTING VECTORS TO NUMPY ARRAY
embeddings_values=np.array(embeddings_values)#CONVERTING VECTORS TO NUMPY ARRAY
# print len(embeddings_words), embeddings_words[0]
# print len(embeddings_values), len(embeddings_values[0]), type(embeddings_values), type(embeddings_values[0])


#DEFINE PARAMETERS
num_senses = 5
batch_size = None#32
vocab_size = len(keys.wv.vocab)#len(embeddings_words)
word_emb_size = len(embeddings_values[0])
max_sent_size = 300
hidden_size = 300
learning_rate=0.01


#MODEL
words_ids=tf.placeholder('int32', shape=[batch_size, max_sent_size])
sequence_lengths=tf.placeholder('int32', shape=[batch_size])
print words_ids.shape, sequence_lengths.shape


L=tf.Variable(embeddings_values, dtype=tf.float32, trainable=False)
pre_trained_embeddings=tf.nn.embedding_lookup(L, words_ids)
print L.shape, pre_trained_embeddings.shape


cell_fw=tf.contrib.rnn.LSTMCell(hidden_size)
cell_bw=tf.contrib.rnn.LSTMCell(hidden_size)
print cell_fw, cell_bw


#CONTEXT REPRESENTATION
(output_fw, output_bw), _ =tf.nn.bidirectional_dynamic_rnn(cell_fw, cell_bw, pre_trained_embeddings, sequence_length=sequence_lengths, dtype=tf.float32)
context_rep=tf.concat([output_fw,output_bw], axis=-1)
print context_rep.shape


#DECODING
W=tf.get_variable("W",shape=[2*hidden_size,num_senses],dtype=tf.float32)
b=tf.get_variable("b",shape=[2*hidden_size,num_senses],dtype=tf.float32)

print W.shape, b.shape


ntime_steps=tf.shape(context_rep)[1]
context_rep_flat=tf.reshape(context_rep, [-1,2*hidden_size])
pred=tf.matmul(context_rep_flat, W)+b
scores=tf.reshape(pred, [-1, ntime_steps, num_senses])

print ntime_steps, context_rep_flat.shape, pred.shape, scores.shape

#TRAINING
labels=tf.placeholder(tf.int32, shape=[None, None])
losses=tf.nn.sparse_softmax_cross_entropy_with_logits(logits=scores, labels=labels)

mask=tf.sequence_mask(sequence_lengths)

losses=tf.boolean_mask(losses,mask)

loss=tf.reduce_mean(losses)

optimizer=tf.train.AdamOptimizer(learning_rate)
train_op=optimizer.minimize(loss)



sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

labels_pred=tf.cast(tf.argmax(pred, axis=-1), tf.int32)
print labels_pred

for i in range(30):
    sess.run(train_step, feed_dict={input_: input_data, output_: y})
    if i % 100 == 0:
        l = sess.run(loss, feed_dict={input_: input_data, output_: y})


print sess.run(loss, feed_dict={input_: input_data, output_: y})
