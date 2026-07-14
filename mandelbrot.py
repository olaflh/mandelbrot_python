
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,1,500)
y = np.linspace(-1.25,1.25,500)
re_values, im_values = np.meshgrid(x,y)
c = re_values + im_values *1j
z = np.zeros((500,500))

bound = 4 #any positive integer greater or equal to 2 
power = 2 
max_iterations = 500
color_map = 'magma_r'

not_diverged = abs(z) < bound
pixel_values = np.zeros((500,500))

for iteration in range(max_iterations):
    z = np.where(not_diverged, z**2 + c, z)
    pixel_values = np.where((abs(z) > 4) & (not_diverged), iteration, pixel_values)
    not_diverged = not_diverged & (abs(z) < bound) 

pixel_values[pixel_values == 0] = max_iterations

#plot
ax = plt.axes()
ax.set_aspect("equal")
graph = ax.pcolormesh(re_values, im_values, np.log(pixel_values + 1), cmap = color_map)
plt.xlabel("Real axis")    
plt.ylabel("Imaginary axis")   
plt.title("Mandelbrot set")
plt.show()




    


