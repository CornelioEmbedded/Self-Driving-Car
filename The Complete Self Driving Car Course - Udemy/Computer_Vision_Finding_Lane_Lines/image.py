import cv2
import numpy as np
import matplotlib.pyplot as plt
from functions import *

image = cv2.imread(r"C:\Users\DELL\Desktop\Cursos\The self driving car course\The-Complete-Self-Driving-Car-Course\The Complete Self Driving Car Course - Udemy\Computer_Vision_Finding_Lane_Lines\Image\test_image.jpg")
edges = canny(image)
triangule = region_of_interest(edges)

cv2.imshow('Result', region_of_interest(edges))
cv2.waitKey(0)

