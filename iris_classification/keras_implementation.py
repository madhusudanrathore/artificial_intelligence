from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import to_categorical
import numpy as NP


#MODEL
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=4))
model.add(Dense(100, activation='sigmoid'))
model.add(Dense(3, activation='softmax'))

PD.prepare_training_data()
PD.prepare_testing_data()

training_input = NP.array(PD.train_data_input)
training_output = NP.expand_dims(PD.train_data_output,axis=1)

one_hot_labels = to_categorical(training_output, num_classes=3)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(training_input, one_hot_labels, epochs=100)