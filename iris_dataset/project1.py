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
		self.weights = 2 * random.random((4,1)) - 1

	#SIGMOID ACTIVATION FUNCTION
	def sigmoid(self,x):
		return 1/(1+exp(-x))
	#DERIVATION OF SIGMOID FUNCTION
	def sigmoid_derivative(self, x):
		return x*(1-x)

	def think(self, inputs):
		return self.sigmoid(dot(inputs, self.weights))

	def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
		for iteration in range(number_of_training_iterations):
			output = self.think(training_set_inputs)
			error = training_set_outputs - output
			adjustment = dot(training_set_inputs.T, error * self.sigmoid_derivative(output))
			self.weights += adjustment

prepare_input_and_output_data()
ann = NeuralNetwork()

training_set_inputs = array(input_data)
training_set_outputs = array(output_data).T
ann.train(training_set_inputs, training_set_outputs, 10000)
# #NEW PREDICTION
# op=ann.think(array([5.1, 3.5, 1.4, 0.2]))
# print(op)
