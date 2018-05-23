import PrepareData as PD
from numpy import exp, array, random, dot, expand_dims, absolute

class NeuralNetwork(object):
	def __init__(self):
		random.seed(1)
		self.weights0 = 2 * random.random((4,5)) - 1
		self.weights1 = 2 * random.random((5,1)) - 1

	def sigmoid(self,x):
		return 1/(1+exp(-x))

	def sigmoid_derivative(self,x):
		return x*(1-x)

	def train(self, input_layer, training_output, iterations):
		learning_rate=0.1
		for it in range(iterations):
			#HIDDEN LAYER FORWARD PROPOGATION
			hidden_layer_input=dot(input_layer, self.weights0)
			hidden_layer_output=self.sigmoid(hidden_layer_input)
			#OUTPUT LAYER FORWARD PROPOGATION
			output_layer_input=dot(hidden_layer_output, self.weights1)
			output_layer_output=self.sigmoid(output_layer_input)
			#BACKPROPOGATION OF ERRORS
			E=training_output-output_layer_output

			slope_output_layer = self.sigmoid_derivative(output_layer_output)
			slope_hidden_layer = self.sigmoid_derivative(hidden_layer_output)
			
			d_output = E * slope_output_layer

			Error_at_hidden_layer = dot(d_output, self.weights1.T)
			d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
			#GRADIENT DESCENT
			self.weights1 = self.weights1 + dot(hidden_layer_output.T, d_output)*learning_rate
			self.weights0 = self.weights0 + dot(input_layer.T,d_hiddenlayer)*learning_rate

	def prediction(self, pred):
		layer1=self.sigmoid(dot(pred, self.weights0))
		layer2=self.sigmoid(dot(layer1, self.weights1))
		return layer2

ann = NeuralNetwork()

PD.prepare_training_data()
training_input = array(PD.train_data_input)
training_output = expand_dims(PD.train_data_output,axis=1)

ann.train(training_input, training_output, 10000)

PD.prepare_testing_data()
test_inp=array(PD.test_data_input)
predicted_op=ann.prediction(test_inp)
