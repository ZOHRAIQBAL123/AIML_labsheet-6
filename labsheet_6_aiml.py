# -*- coding: utf-8 -*-
"""Labsheet 6 AIML

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OEzDcLAD9TEjHzGeWAiAabhc_TYdu_kO
"""

#Linear Algebra
import numpy as np
import pandas as pd

#load the Libraries and data
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data=pd.read_csv('/Sales.csv')

#Grab the relevant data,scale the predictor variable and add a column
x=data['GrLivArea']
y=data['SalePrice']
x=(x-x.mean())/x.std()
x=np.c_[np.ones(x.shape[0]),x]

#GRADIENT DESCENT
alpha=0.01
iterations=1000
m=y.size
np.random.seed(123)
theta=np.random.rand(2)


#GRADIENT DESCENT
def gradient_descent(x,y,theta,iterations,alpha):
  past_costs=[]
  past_thetas=[theta]
  for i in range(iterations):
    prediction=np.dot(x,theta)
    error=prediction-y
    cost=(1/(2*m))*np.dot(error.T,error)
    past_costs.append(cost)
    theta=theta-(1/m)*alpha*(np.dot(x.T,error))
    past_thetas.append(theta)
  return past_thetas,past_costs

#print the resuilts
print("gradient descent:{:.2f},{:.2f}".format(theta[0],theta[1]))

#GRADIENT DESCENT
alpha=0.01
iterations=1000
m=y.size
np.random.seed(123)
theta=np.random.rand(2)

# Call the gradient_descent function and store the returned values
past_thetas, past_costs = gradient_descent(x, y, theta, iterations, alpha)

#print the resuilts
print("gradient descent:{:.2f},{:.2f}".format(theta[0],theta[1]))

#plot the cost function
plt.title('Cost Function ')
plt.ylabel('Cost')
plt.xlabel(' No of Iterations')
plt.plot(past_costs)
plt.show()

from __future__ import annotations #Fixed typo in module name
#set the plot up,
fig=plt.figure()
ax=plt.axes()
plt.title('Sale Price vs Living Area')
plt.xlabel('Living Area')
plt.ylabel('SalePrice ($)')
plt.scatter(x[:,1],y,color='red')
line, =ax.plot([],[],lw=2)
annotation = ax.text(-1,350000,'')
annotation.set_animated(True)
plt.close()

def init():
  line.set_data([],[])
  annotation.set_text('')
  return line,annotation

from google.colab import drive
drive.mount('/content/drive')

def animate(i):
  x=np.linspace(-5000,20000,10000)
  y=past_thetas[i][1]*x+past_thetas[i][0]
  line.set_data(x,y)
  annotation.set_text('cost={:.2f}'.format(past_costs[i]))
  return line,annotation
  anim=animation.FuncAnimation(fig,animate,init_func=init,frames=300,interval=0,blit=True)

  anim.save('animation.gif',writer='imagemagick',fps=30)

#display the animation
import io
import base64
from IPython.display import HTML, display
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# Ensure the animation file is created
def init():
  line.set_data([],[])
  annotation.set_text('')
  return line,annotation

def animate(i):
  x=np.linspace(-5000,20000,10000)
  y=past_thetas[i][1]*x+past_thetas[i][0]
  line.set_data(x,y)
  annotation.set_text('cost={:.2f}'.format(past_costs[i]))
  return line,annotation

# Set up the figure and axes for the animation
fig=plt.figure()
ax=plt.axes()
plt.title('Sale Price vs Living Area')
plt.xlabel('Living Area')
plt.ylabel('SalePrice ($)')
# Assuming 'x' and 'y' are defined elsewhere in your code
plt.scatter(x[:,1],y,color='red')
line, =ax.plot([],[],lw=2)
annotation = ax.text(-1,350000,'')
annotation.set_animated(True)

anim=animation.FuncAnimation(fig,animate,init_func=init,frames=300,interval=0,blit=True)

# Save the animation (replace 'imagemagick' if necessary)
anim.save('animation.gif',writer='imagemagick',fps=30)

filename='animation.gif'

Video=io.open(filename,'r+b').read()
encoded=base64.b64encode(Video)
display(HTML('<img src="data:image/gif;base64,{0}" />'.format(encoded.decode('ascii'))))