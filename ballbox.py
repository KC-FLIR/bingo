#ball box

import cv2
import numpy as np

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

