import csv
import matplotlib.pyplot as plt

rows = []
col0 = []
col1 = []
col2 = []
col3 = []
output = []

#READ THE CSV FILE
filename = 'iris.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data)

#READING DATA AND ASSIGNING APPROPRIATE DATA
x=0
for row in reader:
	rows.append(row)
	col0.append( float(rows[x][0]) )
	col1.append( float(rows[x][1]) )
	col2.append( float(rows[x][2]) )
	col3.append( float(rows[x][3]) )
	output.append(rows[x][4])
	x=x+1

# plotting the points
plt.scatter(col0, col1)
# function to show the plot
plt.show()