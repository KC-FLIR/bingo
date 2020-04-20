# bingoballer.py
# https://techtutorialsx.com/2018/07/08/python-opencv-drawing-circles/
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


def render_sballs(image=None, numbertext=None):

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

def render_scballs(image=None, number=None):

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
        image = blank_balls(size, size)

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


class ballBox:
    name = "defaultbox"
    rows = 9
    columns = 10
    border = 5
    ballpadding = 10
    ballsize = 100
    image = None
    canvas_width = None

    def __init__(self, name=None):
        self.name = name
    

    def create(self):
        total_image_dimension = self.ballsize+(self.ballpadding*2) 
        self.canvas_width = (total_image_dimension*self.columns)+(self.border*2)
        self.canvas_height = (total_image_dimension*self.rows)+(self.border*2)
        #print("Big Box is: (rows {}, cols {}) width {}  height {}".format(self.rows,self.columns,self.canvas_width, self.canvas_height))
        self.image = blank_balls(self.canvas_width, self.canvas_height)
        cv2.rectangle(self.image, (0, 0), (self.canvas_width, self.canvas_height), (200, 200, 200), self.border)
        return self.image

    def placeBall(self,ballImage=None,index=0):
        padding = self.ballpadding
        border = self.border
        ballSize = self.ballsize
        row = int(index/self.columns)
        column = index - (row*self.columns)
        box_width = ballSize + (padding * 2)
        box_x = border + (box_width * column)
        box_y = border + (box_width * row)
        ball_x = box_x + padding
        ball_y = box_y + padding

        #print("Ball #{} Box({},{})  Ball({},{})".format(index, box_x, box_y, ball_x, ball_y))

        cv2.rectangle(self.image, (box_x, box_y), (box_x + box_width, box_y + box_width), (255, 10, 10), 1)

        if ballImage is not None:
            # https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv
            y1, y2 = ball_y, ball_y + ballImage.shape[0]
            x1, x2 = ball_x, ball_x + ballImage.shape[1]

            self.image[y1:y2,x1:x2] = ballImage

            #alpha_s = ballImage[:, :, 3] / 255.0
            #alpha_l = 1.0 - alpha_s

            #for c in range(0, 3):
            #    boxImage[y1:y2, x1:x2, c] = (alpha_s * ballImage[:, :, c] +
            #                      alpha_l * ballImage[y1:y2, x1:x2, c])
        return self.image

    def show(self):
        cv2.imshow(self.name, self.image)



box = ballBox()
box.create()
box.show()




numbers2do = 90
numbersDone = 0
picked = []

while numbersDone < numbers2do:
    thisrando = randomint(1,90)
    if thisrando not in picked:
        picked.append(thisrando)
        #print("Rando {}".format(thisrando))
        image = render_scballs(number=thisrando)
        cv2.imshow('Test image', image)
        cv2.waitKey(0)

        box.placeBall(ballImage=image,index=numbersDone)
        box.show()

        numbersDone += 1
        

cv2.waitKey(0)
cv2.destroyAllWindows()
