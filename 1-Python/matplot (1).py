# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:18:44 2023

@author: Vishwajeet

"""

# 📌🐍 -----------------------------------------------------------------------
import matplotlib.pyplot as plt

plt.plot([1,3,2,4])
plt.show()

# 📌🐍 -----------------------------------------------------------------------
#multiline graph

import matplotlib.pyplot as plt
x = range(1,5)
plt.plot(x,[xi*1.5 for xi in x])
plt.plot(x,[xi*3.0 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])

plt.show()


# 📌🐍 -----------------------------------------------------------------------
#grid


import matplotlib.pyplot as plt

import numpy as np

x = np.arange(1,5)
plt.plot(x,x*1.5 ,x , x*3.0, x/3.0)
plt.grid(True)
plt.show()


# 📌🐍 -----------------------------------------------------------------------
#Shift axis
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5 ,x , x*3.0, x/3.0)
plt.axis()
plt.axis([0,5,-1,13])

plt.show()

# 📌🐍 -----------------------------------------------------------------------
#lables on the graph

import matplotlib.pyplot as plt

plt.plot([1,3,2,4],'-.o')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()

# 📌🐍 -----------------------------------------------------------------------

import matplotlib.pyplot as plt
plt.plot([1,2,4,3,2,1])

plt.title("Shrikant Graph")
plt.show()

# 📌🐍 -----------------------------------------------------------------------
#adding legend to graph
import matplotlib.pyplot as plt
import numpy as np
x =np.arange(1,5)
plt.plot(x, x*1.5, label = 'Normal')
plt.plot(x, x*3, label = 'Fast ')
plt.plot(x, x/3, label = 'Slow')

plt.legend()

plt.show()
# 📌🐍 -----------------------------------------------------------------------
#adding colour 

'''colour abrivation
b blue 
C cyan 
g green 
m megenta 
w white 
k black 
r red 
y yellow
'''
import matplotlib.pyplot as plt

y = np.arange(1,5)
plt.plot(y , 'y')
plt.plot(y+1,'m')
plt.plot(y+2,'c')

plt.show()
# 📌🐍 -----------------------------------------------------------------------
#adding specing tyling as multiple plots

import matplotlib.pyplot as plt
import numpy as np

plt.plot() 
#plt.grid()
plt.show()

# 📌🐍 -----------------------------------------------------------------------
#adding markers in the graph

import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1,5)
plt.plot(y,'--x',y+1,'o',y+2, 'D',y+1.5 ,'^', y+4, 's') 
plt.grid()
plt.show()
# 📌🐍 -----------------------------------------------------------------------
#ploting histogram

import matplotlib.pyplot as plt
import numpy as np
y = np.random.randn(1000)
plt.hist(y);
plt.show()

# 📌🐍 -----------------------------------------------------------------------
#bar graph 

import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5])

plt.show()

# 📌🐍 -----------------------------------------------------------------------
#Scatterplots imp in machine learning 
#to display the colinearity and coherence

import matplotlib.pyplot as plt
import numpy as np

x = [1,4,5,7,3]
y = [1,3,5,9,2]

plt.scatter(x, y) 
plt.show()
# 📌🐍 -----------------------------------------------------------------------
import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(-4,4, 1024)
y =.25*(x + 4.)*(x + 1.) * (x - 2.)
plt.text(-0.5,-0.25,'Brachmard minimum')
plt.plot(x,y, c = 'k')
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x = range(1,10)
plt.plot([2,6,3,6,3],'-.o')
plt.show()

