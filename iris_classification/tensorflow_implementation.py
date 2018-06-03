import tensorflow as tf
from pandas import read_csv

dataframe=read_csv('iris_training.csv')

for i in dataframe.iterrows():
	print i