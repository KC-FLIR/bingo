# countdown.py
# https://techtutorialsx.com/2018/07/08/python-opencv-drawing-circles/
# must have 3 vowels and four consonants, then two of either
import cv2
import numpy as np
import PIL
from PIL import Image
import random
print('Pillow Version:', PIL.__version__)





class lettershelf(object):
    shelf_file="images/scrabble-rest.jpg"
    blank_file="images/scrabble-tile.jpg"
    screen = None
    image = None
    tile = None
    height = 200
    width = 2000
    rgb_black=(0, 0, 0)
    shelfImage = Image.open(shelf_file)
    tileImage = Image.open(blank_file)
    npa_shelf = None
    npa_tile = None
    letters = 0
    ballpadding = 0 #= 10
    ballsize = 200    

    def __init__(self):
        self.image = np.zeros((self.height, self.width, 3), np.uint8)
        self.tile = np.zeros((200, 200, 3), np.uint8)

        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(self.rgb_black))
        # Fill image with color
        self.image[:] = color
        self.tile[:] = color

#        self.npa_shelf = np.asarray(self.shelfImage)
#        self.npa_tile = np.asarray(self.tileImage)
        self.npa_shelf = np.array(Image.open(self.shelf_file).resize((2000,300)))
        self.npa_tile = np.array(Image.open(self.blank_file).resize((200,200)))
        print("Shelf size {}".format(self.npa_shelf.shape))
        print("tile size {}".format(self.npa_tile.shape))
        cv2.imshow("shelf", self.npa_shelf)
        cv2.imshow("tile", self.npa_tile)
        #return image

    def letter(self,charr):
        thisimage = np.array(self.npa_tile)
        print("\n\nLETTER: image size {}".format(thisimage.shape))
        print("LETTER: tile size {}".format(self.npa_tile.shape))

        font = cv2.FONT_HERSHEY_SIMPLEX 
        #org = ((int(size/3.3)),(int(size/1.7))) 
        fontScale = 2
        color = (5,50,1)
        thickness = 10
        cv2.putText(thisimage, charr, (100,50), font,   fontScale, color, thickness, cv2.LINE_AA) 
        print("LETTER: image size {}\n\n".format(thisimage.shape))
        return thisimage

    def blank_tile(width=200, height=200, rgb_colour=(50, 50, 50)):
        # Create black blank image
        binimage = np.zeros((height, width, 3), np.uint8)

        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(rgb_colour))
        # Fill image with color
        binimage[:] = color

        return binimage

    def letter2(self,charr):
        thisimage = self.blank_tile()
        print("\n\nLETTER: image size {}".format(thisimage.shape))
        print("LETTER: tile size {}".format(self.npa_tile.shape))

        font = cv2.FONT_HERSHEY_SIMPLEX 
        #org = ((int(size/3.3)),(int(size/1.7))) 
        fontScale = 2
        color = (5,50,1)
        thickness = 10
        cv2.putText(thisimage, charr, (100,50), font,   fontScale, color, thickness, cv2.LINE_AA) 
        print("LETTER2: image size {}\n\n".format(thisimage.shape))
        return thisimage


    def addtoshelf(self,letter):
        image = self.letter(letter)

        print("\n\nADD2SHELF: image size {}".format(image.shape))
        padding = self.ballpadding
        border = 5
        ballSize = self.ballsize
        column = self.letters
        box_width = ballSize + (padding * 2)
        box_x = border + (box_width * column)
        box_y = 100
        ball_x = box_x + padding
        ball_y = box_y + padding

        #print("Ball #{} Box({},{})  Ball({},{})".format(index, box_x, box_y, ball_x, ball_y))

        #cv2.rectangle(self.image, (box_x, box_y), (box_x + box_width, box_y + box_width), (255, 10, 10), 1)
        x_on_shelf = border+ self.letters * (image.shape[1]+padding)

        y1, y2 = ball_y, ball_y + image.shape[0]
        x1, x2 = ball_x, ball_x + image.shape[1]
        # https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv
        #y1, y2 = image.shape[0],image.shape[0]
        #x1, x2 = image.shape[1],image.shape[1]

        print("ADD2SHELF: Shelf size {}".format(self.npa_shelf.shape))
        print("ADD2SHELF: tile size {}".format(image.shape))

        y_on_shelf=50

        print("ADD2SHELF: y from {} y to {}".format(y_on_shelf,y_on_shelf+image.shape[0]))
        print("ADD2SHELF: x from {} x to {}".format(x_on_shelf,x_on_shelf+image.shape[1]))


        alpha_s = image[:, :, 2] / 255.0
        alpha_l = 1.0 - alpha_s

        self.npa_shelf[y_on_shelf:y_on_shelf+image.shape[0],x_on_shelf,x_on_shelf+image.shape[1]] = image

        #alpha_s = ballImage[:, :, 3] / 255.0
        #alpha_l = 1.0 - alpha_s

        #for c in range(0, 3):
        #    boxImage[y1:y2, x1:x2, c] = (alpha_s * ballImage[:, :, c] +
        #                      alpha_l * ballImage[y1:y2, x1:x2, c])
        self.letters += 1
        return self.npa_shelf

    def show(self):
        cv2.imshow("shelf", self.npa_shelf)



consonants = "AEIOU"
vowels = "BCDFGHJKLMNPQRSTVWXYZ"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    


vcount=3
ccount=4
lcount=9
quiz=""
while lcount > 0:
    choice=random.randint(1,100)
    letter = None
    if choice>50 and vcount>0:
        letter=vowels[random.randint(0,len(vowels)-1)]
        vcount -= 1
    if choice<50 and ccount>0:
        letter=consonants[random.randint(0,len(consonants)-1)]
        ccount -= 1
    if letter is None and (vcount+ccount)<1:
        if choice>50:
            letter=vowels[random.randint(0,len(vowels)-1)]
        else:
            letter=consonants[random.randint(0,len(consonants)-1)]
    if letter is not None:
        print("{} ".format(letter), end="")
        quiz = "()()".format(quiz,letter)
        lcount -= 1
    
print("\n{}\n".format(quiz))
#exit(0)



hewer = lettershelf()
for i, v in enumerate(vowels):
    hewer.addtoshelf(v)
    hewer.show()

exit(0)


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
