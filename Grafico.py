import matplotlib.pyplot as plt
import numpy as np
xaxis = [-3, -2, -1, 0, 1,2,3,4,5,6,7,8,9,10]
yaxis = list(map(lambda w: w*-1, xaxis))
plt.plot(xaxis,yaxis)
plt.ylabel('Analise de dados')
plt.show()



