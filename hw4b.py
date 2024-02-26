#Anthony's code edited by Robert and Andrew

#importsregion
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
#endregion

#problemregion
"""
Step 1: Define function 1 & function 2
Step 2: Use 'fsolve' to find the unique roots of the two functions
Step 3: Print the roots for function 1 and function 2
Step 4: Find the points of intersection between function 1 & function 2
Step 5: Print the points of intersection between function 1 and function 2
Step 6: Create a graph to display points of intersection
"""
def func1(x):  #f(x) = x - 3*cos(x)
    return x - 3 * np.cos(x)

def func2(x):  #g(x) = cos(2x)*x^3.
    return np.cos(2 * x) * (x ** 3)

def func_intersection(x):
    """
    Define the function representing the difference between func1 and func2 to find intersections.
    """
    return func1(x) - func2(x)

def find_unique_roots(func, guesses, tol):  #chatgpt was used here
    """
    Find unique roots of a function given initial guesses and a tolerance for uniqueness.
    """
    unique_roots = []
    for guess in guesses:
        root = fsolve(func, guess)[0]
        #check uniqueness within the specified tolerance
        if not any(np.isclose(root, u_root, atol=tol) for u_root in unique_roots):
            unique_roots.append(root)
    #optionally, round the roots for cleaner output
    unique_roots = np.round(unique_roots, 5)
    return np.unique(unique_roots)

#setup for finding intersections
tolerance = 0.1  #I was getting a plethora of roots as that were very very close to eachother. A 'ignore' tolerance was set
initial_guesses = np.linspace(-10, 10, 400)  #range of initial guesses

#find unique intersection points
unique_intersections = find_unique_roots(func_intersection, initial_guesses, tolerance)

# Print roots for function 1
roots_func1 = find_unique_roots(func1, initial_guesses, tolerance)
print("Roots for func1:")
for root in roots_func1:
    print(f"y = {func1(root)}") #these will be approximations

# Print roots for function 2
roots_func2 = find_unique_roots(func2, initial_guesses, tolerance)
print("Roots for func2:")
for root in roots_func2:
    print(f"y = {func2(root)}") #these will be approximations
    
#endregion

#plottingregion
#plotting setup and execution
#chatgpt was used for this function
x_values = np.linspace(-10, 10, 400)
y1_values = func1(x_values)
y2_values = func2(x_values)

#print the intersection points for function 1 and function 2
print("Intersection Points:")
for x in unique_intersections:
    y1 = func1(x)
    y2 = func2(x)
    print(f"x = {x}, y1 = {y1}, y2 = {y2}") #these wil be approximations

plt.figure(figsize=(10, 6))
plt.plot(x_values, y1_values, label="f(x) = x - 3cos(x)")
plt.plot(x_values, y2_values, label="g(x) = cos(2x)x^3")
plt.scatter(unique_intersections, func1(unique_intersections), color='red', zorder=5, label='Intersections')

plt.title("Graph of f(x) and g(x) with Intersection Points")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

#set the y-axis limits to be from -100 to 100
plt.ylim(-100, 100)

plt.show()
#endregion

