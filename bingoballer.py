# bingoballer.py
# https://techtutorialsx.com/2018/07/08/python-opencv-drawing-circles/
import cv2
import numpy as np

# seed the pseudorandom number generator
from random import seed
from random import randint as randomint


def blank_balls(width, height, rgb_colour=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_colour))
    # Fill image with color
    image[:] = color

    return image


def render_balls(image=None, numbertext=None):

    size = 200
    thickness = 20
    radius = int ((size-(2*thickness)) / 2)
    radius = int ((size-thickness) / 2)
    centre = int (size / 2 )
    fudge = int(centre/2)

    if image is None:
        image = blank_balls(size, size)

    cv2.circle(image, (centre, centre), radius, (255, 255, 255), -1)
    cv2.circle(image, (centre, centre), radius, (139, 0, 139), thickness)

    if numbertext is not None:
        font = cv2.FONT_HERSHEY_SIMPLEX 
        org = ((int(size/3.3)),(int(size/1.7))) 
        fontScale = 2
        color = (0,0,0)
        thickness = 10
        cv2.putText(image, numbertext, org, font,      fontScale, color, thickness, cv2.LINE_AA) 


    return image


numbers2do = 90
picked = []
seed(1)
while numbers2do > 0:
    thisrando = randomint(1,90)
    if thisrando not in picked:
        picked.append(thisrando)
        image = render_balls(numbertext='{}'.format(thisrando))
        numbers2do -= 1
        cv2.imshow('Test image', image)
        cv2.waitKey(500)

cv2.destroyAllWindows()
