import math
import matplotlib.pyplot as plt
#Here we program a quadratic expression and visualize its parabolic nature i.e, like throw of a ball from the ground
# y = -0.0024x**2 + x + 5.5
# Here y is height and x is ditance travelled
#The main intention is to know the distance and height for different values and the way it travels
l = [0] 
m = [0]
#Complete distance travelled by a ball if 46 feet
def f(b,a,c):
    
    z = (-b + math.sqrt(b**2 - 4*a*c))/2*a # for computing x values

    def g():
        
        while True:
            x = input("Input some x values i.e, less than the above limit: ")
        #if you want to stop enter an empty string
            if x == '':
                break
            else:
                float(x)
                l.append(x)
                y = (-0.0241 *(x**2) + 1 * x) + 5.5
                m.append(y)
        l.append(z)
        m.append(0)
        plt.plot(l,m)# here we represented x and y as l,m
        plt.xlabel('Distance(Feet)')
        plt.ylabel('Height(Feet)')
        plt.title('Representation of Ball thrown from the ground')
        plt.show()
    g()

f(1,-0.0241,5.5)
              
    
            
        
