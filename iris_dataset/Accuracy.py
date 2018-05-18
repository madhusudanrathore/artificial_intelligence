import NeuralNetwork as NN
import PrepareData as PD
import numpy as np

op=NN.predicted_op
op_len=len(op)

PD.prepare_testing_data()
test_inp=np.array(PD.test_data_input)
pred_x = []#IT HOLDS ONE FEATURE VALUE OF TRULY PREDICTED OUTPUT
pred_y = []#IT HOLDS ANOTHER FEATURE VALUE OF TRULY PREDICTED OUTPUT

def count_accuracy():
	count=0
	for x in range(0,op_len):
		if ( op[x]>=0 and op[x]<=0.1 ) or ( op[x]>=0.45 and op[x]<=0.55 ) or ( op[x]>=0.90 and op[x]<=1 ):
			count=count+1
			pred_x.append(test_inp[x][0])
			pred_y.append(test_inp[x][1])
	return 100*float(count)/float(len(op))