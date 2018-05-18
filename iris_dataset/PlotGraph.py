import matplotlib.pyplot as PLT
import PrepareData as PD
import Accuracy as ACC

accuracy=ACC.count_accuracy()

PD.original_graph_data()

#PLOTTING ORIGINAL FEATURES
PLT.scatter(PD.p1x, PD.p1y, label= "setosa", color= "red", marker= "o", s=50)
PLT.scatter(PD.p2x, PD.p2y, label= "versicolor", color= "green", marker= "o", s=50)
PLT.scatter(PD.p3x, PD.p3y, label= "virginica", color= "blue", marker= "o", s=50)
#PLOTTING PREDICTED FEATURES
PLT.scatter(ACC.pred_x, ACC.pred_y, label= "prediction", color= "black", marker= "|", s=100)

PLT.xlabel('sepal length')
PLT.ylabel('sepal width')
PLT.title( accuracy )
PLT.legend()
PLT.show()