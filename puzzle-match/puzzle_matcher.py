import cv2
import numpy as np

# Load the puzzle box image
puzzle_box_image = cv2.imread('../static/images/puzzle_box.jpg')

# Display the puzzle box image
cv2.imshow('Puzzle Box Image', puzzle_box_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
