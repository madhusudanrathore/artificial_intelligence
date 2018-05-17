import csv
import matplotlib.pyplot as plt
from numpy import exp, array, random, dot

input_data = []
output_data = []

def prepare_input_and_output_data():
	filename = 'iris2.csv'
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
		input_data.append(column)
		var=temp_row[x][4]
		if var=="setosa":
			output_data.append(0)
		elif var=="versicolor":
			output_data.append(1)
		elif var=="virginica":
			output_data.append(2)
		x=x+1

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

prepare_input_and_output_data()
ann = NeuralNetwork()

training_set_inputs = array(input_data)
training_set_outputs = array(output_data).T#TRANSPOSE MAKES IT A COLUMN VECTOR

ann.train(training_set_inputs, training_set_outputs, 10000)
ann.prediction()
