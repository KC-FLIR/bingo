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
        self.canvas_width = (self.ballsize*(self.columns+1))+(self.ballpadding*(self.columns+1))+(self.border*2)
        self.canvas_height = (self.ballsize*(self.rows+1))+(self.ballpadding*(self.rows + 1))+(self.border*2)
        #boxWidth = (ballSize*11)+(padding*11)+(border*2)
        self.image = blank_balls(self.canvas_width, self.canvas_height)
        print("Big Box is: width {}  height {}".format(self.canvas_width, self.canvas_height))
        cv2.rectangle(self.image, (0, 0), (self.canvas_width, self.canvas_height), (200, 200, 200), self.border)

        return self.image

    def createfilled(self,bgd=None):
        self.create()
        if bgd is None:
            bgd = (10, 10, 200)
        cv2.rectangle(self.image, (self.border, self.border), (self.canvas_width-(2*self.border), self.canvas_height-(2*self.border)), bgd,-1)
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


def getNumbers(to_pick=10, range_low=1,range_high=90):
    numbersDone = 0
    picked = []
    while numbersDone < to_pick:
        thisrando = randomint(range_low, range_high)
        if thisrando not in picked:
            picked.append(thisrando)
            numbersDone += 1
    return picked


class bingoCard:
    cards_columns = 10
    cards_per_row = 5
    cards_rows = 4
    name = 'Bingo Card'
    box = None

    def create(self,colourindex=0):
        self.box = ballBox()
        self.box.name = self.name
        self.box.rows = self.cards_rows
        self.box.columns = self.cards_columns
        self.box.createfilled(ball_colours[colourindex])
    
    def genCard(self):
        pick = self.cards_per_row * self.cards_rows
        selected = getNumbers(to_pick=pick)

        ball = 0
        for row in range(0,self.cards_rows):
            #print("\nROW ~{}".format(row))
            spots = getNumbers(self.cards_per_row, 0, (self.cards_columns-1))
            for balls in range(0, self.cards_per_row):
                # slots for balls already picked
                column = spots[balls]
                index = (row*self.cards_columns)+column
                print("ROW #{}  BALL#{}  POSITION#{}  (index#{})".format(row,balls,column,index))
                image = render_scballs(number=selected[ball])
                # Work out box number for placement
                self.box.placeBall(ballImage=image, index=index)
                #self.box.show()
                # Next ball from out preselected list
                ball += 1
        
    def show(self):
        self.box.show()

    def save(self):
        #path = "\Users\ukkev\gitwork\BINGO\cards\{}.png".format(self.name)
        #path = "/Users/ukkev/gitwork/BINGO/cards\{}.png".format(self.name)
        path = "cards/{}.png".format(self.name)
        result = cv2.imwrite(path,self.box.image)


card = bingoCard()
teamcount = {}
for item in range(0,2000):
    team = item % 10
    if team not in teamcount:
        teamcount[team] = 0
    teamcount[team] += 1
    card.name = "Team-{0:2}_Card-{0:5}".format(team, teamcount[team])
    card.create(team)
    card.genCard()
    #card.show()
    card.save()
    


cv2.destroyAllWindows()
