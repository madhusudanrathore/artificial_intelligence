import csv
import matplotlib.pyplot as plt

rows = []
input_data = []
output = []

#READ THE CSV FILE
filename = 'iris.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data)

#READING DATA AND ASSIGNING APPROPRIATE DATA
x=0
for row in reader:
	column = []
	rows.append(row)
	column.append(float(rows[x][0]))
	column.append(float(rows[x][1]))
	column.append(float(rows[x][2]))
	column.append(float(rows[x][3]))
	input_data.append(column)
	output.append(rows[x][4])
	x=x+1

#print(type(input_data))
#print(type(input_data[0]))
#print(type(input_data[0][0]))
for x in xrange(150):
	print(input_data[x])

# col0 = []
# col1 = []
# for x in xrange(150):
# 	col0.append(input_data[x][0])
# 	col1.append(input_data[x][1])

# #PLOTTING POINTS
# plt.scatter(col0, col1)
# #SHOW THE PLOT
# plt.show()
