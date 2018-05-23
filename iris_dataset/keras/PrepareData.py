import csv
import numpy as np

train_data_input = []
train_data_output = []

test_data_input = []
test_data_output = []

def prepare_training_data():
	filename = '../iris_training.csv'
	raw_data = open(filename, 'r')
	reader = csv.reader(raw_data)
	#CREATING TRAINING DATASET
	x=0
	temp_row = []
	
	for row in reader:
		column = []
		temp_row.append(row)
		
		column.append(float(temp_row[x][0]))
		column.append(float(temp_row[x][1]))
		column.append(float(temp_row[x][2]))
		column.append(float(temp_row[x][3]))
		train_data_input.append(column)
		
		var=temp_row[x][4]
		if var=="setosa":
			train_data_output.append(0)
		elif var=="versicolor":
			train_data_output.append(0.5)
		elif var=="virginica":
			train_data_output.append(1)
		x=x+1

def prepare_testing_data():
	filename = '../iris_testing.csv'
	raw_data = open(filename, 'r')
	reader = csv.reader(raw_data)
	#CREATING TRAINING DATASET
	x=0
	temp_row = []
	
	for row in reader:
		column = []
		temp_row.append(row)
		
		column.append(float(temp_row[x][0]))
		column.append(float(temp_row[x][1]))
		column.append(float(temp_row[x][2]))
		column.append(float(temp_row[x][3]))
		test_data_input.append(column)
		
		var=temp_row[x][4]
		if var=="setosa":
			test_data_output.append(0)
		elif var=="versicolor":
			test_data_output.append(0.5)
		elif var=="virginica":
			test_data_output.append(1)
		x=x+1

p1x = []
p1y = []
p2x = []
p2y = []
p3x = []
p3y = []
def original_graph_data():
	for y in xrange(0,30):
		if y>=0 and y<=9:
			p1x.append(test_data_input[y][0])
			p1y.append(test_data_input[y][1])
		elif y>=10 and y<=19:
			p2x.append(test_data_input[y][0])
			p2y.append(test_data_input[y][1])
		elif y>=20 and y<=29:
			p3x.append(test_data_input[y][0])
			p3y.append(test_data_input[y][1])