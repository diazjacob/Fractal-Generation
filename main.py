import cv2.cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import time

iteration_depth = 4000
magnitude_cap = float(np.power(10, 8))

color = [51,151,255]
color_coeff = float(0.045)

resX = 1536
resY = 2048

zoom = .4
#center -.8, zoom 3
graph_center_x = 0
graph_center_y = 0

jx,jy = -1,.28

def iterated_mandelbrot(x0, y0):
    x, y = x0, y0
    needed_iterations = 0
    for i in range(iteration_depth):
        needed_iterations += 1
        #x, y = x * x - y * y + x0, 2 * np.abs(x * y) + y0  # Burning Ship Calculation
        #x, y = x * x - y * y + x0, 2 * x * y + y0  # Mandelbrot Calculation

        x, y = x * x - y * y + x0,  2 * x * y + y0 # Mandelbrot Calculation

        #z = complex(x,y)
        #c = complex(x0,y0)
        #z = np.power(z, 2) + c
        #x = np.real(z)
        #y = np.imag(z)

        if x*x+y*y > magnitude_cap:
            break

    return needed_iterations

def iterated_julia_set(x0, y0):
    x, y = x0, y0
    needed_iterations = 0
    for i in range(iteration_depth):
        needed_iterations += 1
        #x, y = x * x - y * y + x0, 2 * np.abs(x * y) + y0  # Burning Ship Calculation
        #x, y = x * x - y * y + x0, 2 * x * y + y0  # Mandelbrot Calculation

        x, y = x * x - y * y + jx,  2 * x * y + jy # Mandelbrot Calculation


        if x*x+y*y > magnitude_cap:
            break

    return needed_iterations


def calculate_frame():
    start_time = time.time()

    image = np.zeros((resY,resX,3), np.uint8)

    graph_dim_x = zoom
    graph_dim_y = resY/resX * zoom

    bound_x_min = graph_center_x - graph_dim_x/float(2)
    bound_y_min = graph_center_y - graph_dim_y/float(2)

    x_iteration_size = graph_dim_x/float(resX)
    y_iteration_size = graph_dim_y/float(resY)

    for i in range(resY):
        for j in range(resX):
            print("Pixel:", (j,i))

            pixel_value = iterated_julia_set(bound_x_min + (j * x_iteration_size),
                                                      bound_y_min + (y_iteration_size * i))
            if pixel_value == iteration_depth:
                image[i][j] = [255,255,255]
            else:
                depth_check = int(np.ceil((iteration_depth/pixel_value)*color_coeff))

                image[i][j] = [np.clip((255-(color[0] / depth_check)), 0, 255),
                              np.clip((255-(color[1] / depth_check)), 0, 255),
                               np.clip((255-(color[2] / depth_check)), 0, 255)]

    print("Calculation time:", (time.time() - start_time), "s")
    return image

def calculate_image():
    curr_iteration = 0

    img = calculate_frame()
    #img_smooth = cv2.GaussianBlur(img, (1, 1), cv2.BORDER_DEFAULT)
    #bilinear_img = cv2.resize(img,None, fx = 1.2, fy = 1.2, interpolation = cv2.INTER_CUBIC)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.autoscale()
    plt.title("Fractal")
    plt.show()

    cv2.imwrite("multibrot.png", img)

    print("Frame " + str(curr_iteration) + " Finished")

calculate_image()





#rotation_matrix = cv2.getRotationMatrix2D((w/2,h/2), -180, 0.5)
#rotated_image = cv2.warpAffine(image_scaled, rotation_matrix, (w, h))

#image_scaled = cv2.resize(image, None, fx=.1, fy=.1, interpolation=cv2.INTER_LINEAR)


