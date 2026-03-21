import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class main:
    x = sp.symbols('x')
    domain = []
    
    def func(self):
        expr = input("Enter an algebric function in terms of x only:\n")
        while True:
            dm = eval(input("Enter the domain belonging to [-1000,1000] in which you want to plot the function in the form of a list (Ex: [a,b]):\n"))
            if len(dm)==2 and max(dm)<=1000 and min(dm)>=-1000:
                self.domain += dm
                self.domain.sort()
                break
            else:
                print("Invalid Input! Try again!")
        return expr
    
    def plotter(self,x1,y1,expr):
        plt.plot(x1,y1)
        plt.title(f"y = {expr}")
        plt.grid()
        plt.show()
    
    def control(self):
        expr = self.func().strip()
        sym_expr = sp.sympify(expr)
        final_expr = sp.lambdify(self.x, sym_expr, "numpy")

        x_values = np.linspace(self.domain[0],self.domain[1], 9999)
        y_values = final_expr(x_values)

        self.plotter(x_values, y_values, expr)
        print("Function has been successfully displayed!")
        print("Goodbye!")
        print("Developed by Soutrik Banerjee | GitHub: github.com/EnderionX\n© 2026 All Rights Reserved")

obj = main()
obj.control()
