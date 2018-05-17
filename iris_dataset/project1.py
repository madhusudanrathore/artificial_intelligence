import prepare_dataset as pd
from numpy import exp, array, random, dot

class NeuralNetwork(object):
	def __init__(self):
		random.seed(1)
		self.weights0 = 2 * random.random((2,3)) - 1
		self.weights1 = 2 * random.random((3,1)) - 1

	def sigmoid(self,x):
		return 1/(1+exp(-x))

	def sigmoid_derivative(self,x):
		return x*(1-x)

	def think(self, inputs, weights):
		return self.sigmoid(dot(inputs, weights))

	def print_dimensions(self,l0,w0,l1,w1,l2):
		print(len(l0),len(l0[0]))
		print(len(w0),len(w0[0]))
		print(len(l1),len(l1[0]))
		print(len(w1),len(w1[0]))
		print(len(l2),len(l2[0]))

	def train(self, layer0, training_set_outputs, iterations):
		for iteration in range(iterations):
			layer1 = self.think(layer0, self.weights0)
			layer2 = self.think(layer1, self.weights1)
			#BACKPROPOGATION
			layer2_error=training_set_outputs-layer2
			#hidden_error = layer1 * (1 - layer1) * dot(layer2_error, self.weights1.T)
		self.print_dimensions(layer0,self.weights0,layer1,self.weights1,layer2)

	def prediction(self):
		pred=training_set_inputs[140]
		layer1 = self.think(pred, self.weights0)
		layer2 = self.think(layer1, self.weights1)
		print(layer2)

pd.prepare_input_and_output_data()
ann = NeuralNetwork()

training_set_inputs = array(pd.input_data)
training_set_outputs = array(pd.output_data).T#TRANSPOSE MAKES IT A COLUMN VECTOR

ann.train(training_set_inputs, training_set_outputs, 10000)
ann.prediction()
