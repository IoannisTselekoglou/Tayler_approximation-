#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import newmathlib as nmp


path_test = "/Users/jannitselekoglou/projects_Ml/mse/assets"
range_x = 100

#use list comprehension cause range just takes int not float 
g_x = [i for i in range(-5,5)]
g_y = g_x

#return factorial of input
fac = lambda x:np.math.factorial(x)

def taylor_sin(grad,x,start):
    y = []
    form = []
    grad_array = nmp.derivate(grad+1,[1,0],start)
    for i in range(grad+1):
        y_1 = grad_array[i]
        y_2 = (x-start)**i
        y.append(y_1*y_2/fac(i))
        #form.append(f"{str(y_1)}*(x-{start}^{i})/{fac(i)}")
    return sum(y)

#Plot Taylor_polynomials
def plot_taylor(range_i, starting_point, grad: list):
    save_fig = True
    sin_w = True
    titles = []
    T_x_total = np.linspace(-range_i,range_i, 1000)
    T_y_total = []
    
    # append y to total_y 
    for gradiant in grad:
        T_y_total.append(taylor_sin(gradiant,T_x_total, starting_point))


    if sin_w == True:
        plt.plot(T_x_total, np.sin(T_x_total))
        titles.append("original sin-function")

    for i in range(len(grad)):
        plt.plot(T_x_total, T_y_total[i])

    plt.ylim([-10,10])
    plt.grid(True)

    titles += [f"T_x_{i}" for i in grad]

    plt.legend(titles)

    plt.title("Taylor Approximation of Sinwave")
    return plt.show()

    #savefig
    if save_fig is True:
        plt.savefig("assets/taylor_approx.png",dpi1550, bbox_inches="tight")

plot_taylor(10,0,[1,3,5,15])



