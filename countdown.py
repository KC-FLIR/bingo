# countdown.py
# https://techtutorialsx.com/2018/07/08/python-opencv-drawing-circles/
# must have 3 vowels and four consonants, then two of either
import cv2
import numpy as np
import PIL
from PIL import Image
import random
import itertools as it
print('Pillow Version:', PIL.__version__)


class jiggleletters(object):
    thisword = None 
    perms = None

    def __init__(self,word):
        self.thisword = word

    def gen_perms(self,letters):
        return 

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
    ballpadding = 10 #= 10
    ballsize = 200    

    def __init__(self):
        self.image = np.zeros((self.height, self.width, 3), np.uint8)
        self.tile = np.zeros((200, 200, 3), np.uint8)

        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(self.rgb_black))
        # Fill image with color
        self.image[:] = color
        self.tile[:] = color

        self.npa_shelf = np.array(Image.open(self.shelf_file).resize((2000,400)))
        self.npa_tile = np.array(Image.open(self.blank_file).resize((160,160)))
        ##print("Shelf size {}".format(self.npa_shelf.shape))
        ##print("tile size {}".format(self.npa_tile.shape))
        cv2.imshow("shelf", self.npa_shelf)

    def white_to_transparency_gradient(img):
        x = np.asarray(img.convert('RGBA')).copy()

        x[:, :, 3] = (255 - x[:, :, :3].mean(axis=2)).astype(np.uint8)

        return Image.fromarray(x)

    def letter(self,charr):
        thisimage = np.array(self.npa_tile)
        ##print("\n\nLETTER: image size {}".format(thisimage.shape))
        ##print("LETTER: tile size {}".format(self.npa_tile.shape))

        font = cv2.FONT_HERSHEY_SIMPLEX 
        #org = ((int(size/3.3)),(int(size/1.7))) 
        fontScale = 6
        color = (5,50,1)
        thickness = 20
        tile_height = thisimage.shape[0]
        tile_width = thisimage.shape[1]
        # destination, char, (x,y (from top))
        cv2.putText(thisimage, charr, (int (thickness/2),(tile_height - thickness)), font,   fontScale, color, thickness, cv2.LINE_AA) 
        ##print("LETTER: image size {}\n\n".format(thisimage.shape))
        return thisimage

    def blank_tile(width=200, height=200, rgb_colour=(50, 50, 50)):
        # Create black blank image
        binimage = np.zeros((height, width, 3), np.uint8)

        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(rgb_colour))
        # Fill image with color
        binimage[:] = color

        return binimage

   

    def addtoshelf(self,letter):
        image = self.letter(letter)

        ##print("\n\nADD2SHELF: image size {}".format(image.shape))
        padding = self.ballpadding

        x_on_shelf = 200 + (self.letters * (image.shape[1]+padding))

       
        # https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv

        ##print("ADD2SHELF: Shelf size {}".format(self.npa_shelf.shape))
        ##print("ADD2SHELF: image size {}".format(image.shape))

        y_on_shelf=40

        ##print("ADD2SHELF: y from {} y to {}".format(y_on_shelf,y_on_shelf+image.shape[0]))
        ##print("ADD2SHELF: x from {} x to {}".format(x_on_shelf,x_on_shelf+image.shape[1]))



        #print("Alpha? {}".format((255 - image[:, :, :3].mean(axis=2)).astype(np.uint8)))
        #image[:, :, 3] = (255 - image[:, :, :3].mean(axis=2)).astype(np.uint8)

        self.npa_shelf[y_on_shelf:y_on_shelf+image.shape[0],x_on_shelf:x_on_shelf+image.shape[1]] = image

        self.letters += 1
        return self.npa_shelf

    def show(self):
        cv2.imshow("shelf", self.npa_shelf)



vowels = "AEIOU"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"
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
        quiz = "{}{}".format(quiz,letter)
        lcount -= 1
    
print("\n{}\n".format(quiz))
#exit(0)



hewer = lettershelf()
#for i, v in enumerate(vowels):
for i, v in enumerate(quiz):
    hewer.addtoshelf(v)
    hewer.show()

qlist = list(quiz)
print("Quiz string is {} long".format(len(qlist)))
bflist = []
for plen in range(2,len(qlist)):
    print("Generating perms of length : {}".format(plen))
    perms = list(it.permutations(qlist,plen))
    bflist = bflist + perms
#perms = list(it.permutations(qlist))
print("So thats {} combination".format(len(bflist)))
cv2.waitKey(0)
# Build dict
pdict={}
for perm in bflist:
    string = "".join(perm)
    if string not in pdict:
        pdict[string] = 1
print("So thats {} uniques".format(len(pdict)))
    
cv2.destroyAllWindows()
with open('key-list.txt',"w") as outputfile:
    for key in pdict:
        outputfile.write("{}\n".format(key))


with open('perms-list.txt',"w") as outputfile:
    for perm in bflist:
        string = "".join(perm)
        outputfile.write("{}\n".format(string))

exit(0)

