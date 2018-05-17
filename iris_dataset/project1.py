import csv
import matplotlib.pyplot as plt
from numpy import exp, array, random, dot

input_data = []
output_data = []

#PREPARE INPUT AND OUTPUT DATASET
def prepare_input_and_output_data():
	#READ THE CSV FILE
	filename = 'iris.csv'
	raw_data = open(filename, 'r')
	reader = csv.reader(raw_data)
	#READING DATA AND CREATING THE DATASET
	x=0
	temp_row = []
	for row in reader:
		column = []
		temp_row.append(row)
		column.append(float(temp_row[x][0]))
		column.append(float(temp_row[x][1]))
		column.append(float(temp_row[x][2]))
		column.append(float(temp_row[x][3]))
		input_data.append(column)
		var=temp_row[x][4]
		if var=="setosa":
			output_data.append(0)
		elif var=="versicolor":
			output_data.append(1)
		elif var=="virginica":
			output_data.append(2)
		x=x+1
	#print(output_data)

class NeuralNetwork(object):
	def __init__(self):
		random.seed(1)
		#GENERATING RANDOM WEIGHTS
		self.weights0 = 2 * random.random((2,3)) - 1
		self.weights1 = 2 * random.random((3,150)) - 1
		# print(self.weights0)
		# print(self.weights1)
	#SIGMOID ACTIVATION FUNCTION
	def sigmoid(self,x):
		return 1/(1+exp(-x))
	#DERIVATIVE OF SIGMOID FUNCTION
	def sigmoid_derivative(self,x):
		return x*(1-x)
	#NETWORK THINKS
	def think(self, inputs, weights=None):
		if weights is not None:
			return self.sigmoid(dot(inputs, weights))
		else:
			return self.sigmoid(dot(inputs, self.weights0))
	#TRAINING NETWORK
	def train(self, layer0, training_set_outputs, number_of_training_iterations):
		for iteration in range(number_of_training_iterations):
			layer1 = self.think(layer0, self.weights0)
			layer2 = self.think(layer1, self.weights1)
			#NOW CALCULATING ERRORS
			layer2_error=training_set_outputs-layer2
			# #BACKPROPOGATION OF ERRORS
			layer2_delta=layer2_error*self.sigmoid_derivative(layer2)
			layer1_error=layer2_delta.dot(self.weights1.T)
			layer1_delta=layer1_error*self.sigmoid_derivative(layer1)
			#GRADIENT DESCENT USING DELTAS
			self.weights1 += layer1.T.dot(layer2_delta)*.1
			self.weights0 += layer0.T.dot(layer1_delta)*.1
		#self.dimensions(layer0,self.weights0,layer1,self.weights1,layer2)
	#PRINT DIMENSIONS OF MATRICES FORMED
	def dimensions(self,l0,w0,l1,w1,l2):
		print(len(l0),len(l0[0]))
		print(len(w0),len(w0[0]))
		print(len(l1),len(l1[0]))
		print(len(w1),len(w1[0]))
		print(len(l2),len(l2[0]))

prepare_input_and_output_data()
ann = NeuralNetwork()

training_set_inputs = array(input_data)
training_set_outputs = array(output_data).T
ann.train(training_set_inputs, training_set_outputs, 10000)
#NEW PREDICTION
op=ann.think(training_set_inputs[140])
print(op)
