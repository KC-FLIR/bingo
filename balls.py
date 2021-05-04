# balls.py
import cv2
import numpy as np

# seed the pseudorandom number generator
from random import seed
from random import randint as randomint 

ball_colours = [(128, 0, 0),
                (128, 128, 0),
                (0, 128, 0),
                (77, 128, 0),
                (0, 128, 77),
                (23, 34, 200),
                (94, 128, 200),
                (34, 200, 100),
                (200, 128, 200),
                (255, 28, 144)
                ]


class balls:
    def blank_balls(self,width, height, rgb_colour=(0, 0, 0)):
        """Create new image(numpy array) filled with certain color in RGB"""
        # Create black blank image
        image = np.zeros((height, width, 3), np.uint8)

        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(rgb_colour))
        # Fill image with color
        image[:] = color

        return image


    def render_balls(self,image=None, numbertext=None):

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


    def render_sballs(self,image=None, numbertext=None):

        size = 100
        thickness = int(size/10)
        radius = int ((size-thickness) / 2)
        centre = int (size / 2 )
        
        if image is None:
            image = blank_balls(size, size)

        cv2.circle(image, (centre, centre), radius, (255, 255, 255), -1)
        cv2.circle(image, (centre, centre), radius, (139, 0, 139), thickness)

        if numbertext is not None:
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL 
            org = ((int(size/3.5)),(int(size/1.7))) 
            fontScale = 2
            color = (0,0,0)
            textthickness = int (thickness/2)
            cv2.putText(image, numbertext, org, font,      fontScale, color, textthickness, cv2.LINE_AA) 


        return image

    def render_scballs(self,image=None, number=None):

        size = 100
        thickness = int(size/10)
        radius = int ((size-thickness) / 2)
        centre = int (size / 2 )
        ThisBallColour = ball_colours[0]

        if number is not None:
            colour_index = int(number/10)
            #print("Balls please :{} colour index {}".format(number,colour_index))
            ThisBallColour = ball_colours[colour_index]
        
        if image is None:
            image = self.blank_balls(size, size)

        cv2.circle(image, (centre, centre), radius, (255, 255, 255), -1)
        #cv2.circle(image, (centre, centre), radius, (139, 0, 139), thickness)
        cv2.circle(image, (centre, centre), radius, ThisBallColour, thickness)

        if number is not None:
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL 
            y = int(size/1.63)
            if number<10:
                x = int(size/2.8)
            else:
                x = int(size/3.8)
            
            org = (x,y) 
            fontScale = 2
            color = (0,0,0)
            textthickness = int (thickness/2)
            cv2.putText(image, "{}".format(number), org, font,      fontScale, color, textthickness, cv2.LINE_AA) 

        return image
