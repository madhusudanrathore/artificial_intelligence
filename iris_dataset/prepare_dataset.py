import csv

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