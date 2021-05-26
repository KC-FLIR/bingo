# countdown.py
# https://techtutorialsx.com/2018/07/08/python-opencv-drawing-circles/
# must have 3 vowels and four consonants, then two of either
import cv2
import numpy as np
import PIL
from PIL import Image
import random
import itertools as it
import enchant
import copy

print("Pillow Version:", PIL.__version__)


class jiggleletters(object):
    thisword = None
    perms = None

    def __init__(self, word):
        self.thisword = word

    def gen_perms(self, letters):
        return


class letter_bag(object):
    consonantCount = 0
    vowelCount = 0
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SCRABBLE = dict(A = 9 , 
                    B = 2 , C = 2 ,D=4,E=12,F=2,G=3,H=2,I=9,J=1,K=1,L=4,M=2,N=6,O=8,P=2,Q=1,R=6,S=4,T=6,U=4,V=2,W=2,X=1,Y=2,Z=1)
    gameBag = {}


    def __init__(self):
        self.gameBag = copy.deepcopy(self.SCRABBLE)
        self.vowelCount = 0
        for index, letter in enumerate(self.vowels):
            self.vowelCount += self.gameBag[letter]
        self.consonantCount = 0
        for index, letter in enumerate(self.consonants):
            self.consonantCount += self.gameBag[letter]

    def reset(self):
        self.gameBag = copy.deepcopy(self.SCRABBLE)
        self.vowelCount = 0
        for index, letter in enumerate(self.vowels):
            self.vowelCount += self.gameBag[letter]
        self.consonantCount = 0
        for index, letter in enumerate(self.consonants):
            self.consonantCount += self.gameBag[letter]


    def vowel(self):
        letter = None
        while letter is None and self.vowelCount > 0:
            diceRoll = random.randint(0, len(self.vowels) - 1)
            tryletter = self.vowels[diceRoll]
            if self.gameBag[tryletter] > 0:
                self.gameBag[tryletter] -= 1
                self.vowelCount -= 1
                letter = tryletter
        return letter

    def consonant(self):
        letter = None
        while letter is None and self.consonantCount > 0:
            diceRoll = random.randint(0, len(self.consonants) - 1)
            tryletter = self.consonants[diceRoll]
            if self.gameBag[tryletter] > 0:
                self.gameBag[tryletter] -= 1
                self.consonantCount -= 1
                letter = tryletter
        return letter

class CountdownLetters(letter_bag):
    # Must have 3 vowels
    vcount = 3
    # and 4 consonants
    ccount = 4
    # and total string length is 9
    lcount = 9
    # quiz will be our string
    quiz = ""

    #big fucking list
    # - all the permutations
    bflist = []
    # Used to make unique list of permutations
    pdict = {}
    # only english words
    valids = {}

    # OUr dictionary object
    d = None

    def __init__(self):
        super().__init__()
        self.d = enchant.Dict("en_GB")

    def genString(self, lcount=9):
        self.quiz=""
        while lcount > 0:
            # could have done binary random I guess, but chose to do 1-100
            # greater than 50, its a vowel
            # less than 50, it's a consonant
            choice = random.randint(1, 100)

            # No choice made yet
            letter = None

            # ok - if chance chose vowel, and we havent maxxed out our vowel count yet..
            if choice > 50 and self.vcount > 0:
                letter = self.vowel()
                if letter is not None:
                    self.vcount -= 1  # take one off our alloted vowels

            # ok - if chance chose consonant, and we havent maxxed out our consonant count yet..
            if choice < 50 and self.ccount > 0:
                letter = self.consonant()
                if letter is not None:
                    self.ccount -= 1  # take one off our alloted vowels

            # Hmm here and no letter yet?  Only do this bit if we have exhausted our mandatory selections defined by te consonant count and vowle counts
            if letter is None and (self.vcount + self.ccount) < 1:
                # consonant or vowel, let chance decide the remainers of our string
                if choice > 50:
                    letter = self.vowel()
                else:
                    letter = self.consonant()

            # if we have found a letter, append it to our string
            if letter is not None:
                self.quiz = "{}{}".format(self.quiz, letter)
                lcount -= 1
        return self.quiz

    def genPerms(self, solvestring=None):
        # First job is to generate all the permutaions of strings from 2 characters up to string length, from the character mix we've selected above
        if solvestring is None:
            solvestring = self.quiz
        # if you dont give me a string to solve, and we've not gened one in genString, return
        if solvestring is None:
            return None
        qlist = list(solvestring)
        print("Quiz string is {} long".format(len(qlist)))
        self.bflist = []
        for plen in range(2, len(qlist)):
            print("Generating perms of length : {}".format(plen))
            perms = list(it.permutations(qlist, plen))
            self.bflist = self.bflist + perms
        print("So thats {} combination".format(len(self.bflist)))

    def stripDupes(self):
        # Second job is to remove all the dupes.  If out character mix is   e e b b , the permuations will include
        # char[1] char[2] char[3] --> eeb
        # char[2] char[1] char[3] --> eeb
        # Which are the same. There's probably a super smart python way of filtering this out
        # but hacky me is using the built in dictionary object to do the hashing for me

        # Build dict
        self.pdict = {}
        for perm in self.bflist:
            # perm is a list  or char[1],char[2],char[3] etc, so smash them together into a string using .join
            string = "".join(perm)  
            # using a dict and in is such a very simple way of filtering dupes
            if string not in self.pdict:  
                self.pdict[string] = 1
        print("So thats {} uniques".format(len(self.pdict)))


    def butIsItEnglish(self):
        # Now look up these uniques in a good old british dictionary
        self.valids = {}
        for key in self.pdict:
            if self.d.check(key):
                self.valids[key] = len(key)

    def solve(self, solvestring=None):
        # First job is to generate all the permutaions of strings from 2 characters up to string length, from the character mix we've selected above
        if solvestring is None:
            solvestring = self.quiz
        # if you dont give me a string to solve, and we've not gened one in genString, return
        if solvestring is not None:
            self.genPerms(solvestring)
            self.stripDupes()
            self.butIsItEnglish()
        return self.valids



class lettershelf(object):
    shelf_file = "images/scrabble-rest.jpg"
    blank_file = "images/scrabble-tile.jpg"
    screen = None
    image = None
    tile = None
    height = 200
    width = 2000
    rgb_black = (0, 0, 0)
    shelfImage = Image.open(shelf_file)
    tileImage = Image.open(blank_file)
    npa_shelf = None
    npa_tile = None
    letters = 0
    ballpadding = 10  # = 10
    ballsize = 200

    def __init__(self):
        self.image = np.zeros((self.height, self.width, 3), np.uint8)
        self.tile = np.zeros((200, 200, 3), np.uint8)

        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(self.rgb_black))
        # Fill image with color
        self.image[:] = color
        self.tile[:] = color

        self.npa_shelf = np.array(Image.open(self.shelf_file).resize((2000, 400)))
        self.npa_tile = np.array(Image.open(self.blank_file).resize((160, 160)))
        ##print("Shelf size {}".format(self.npa_shelf.shape))
        ##print("tile size {}".format(self.npa_tile.shape))
        cv2.imshow("shelf", self.npa_shelf)

    def emptyShelf(self):
        self.npa_shelf = np.array(Image.open(self.shelf_file).resize((2000, 400)))
        self.letters = 0
        cv2.imshow("shelf", self.npa_shelf)
        cv2.waitKey(1)


    def white_to_transparency_gradient(img):
        x = np.asarray(img.convert("RGBA")).copy()

        x[:, :, 3] = (255 - x[:, :, :3].mean(axis=2)).astype(np.uint8)

        return Image.fromarray(x)

    def letter(self, charr):
        thisimage = np.array(self.npa_tile)
        ##print("\n\nLETTER: image size {}".format(thisimage.shape))
        ##print("LETTER: tile size {}".format(self.npa_tile.shape))

        font = cv2.FONT_HERSHEY_SIMPLEX
        # org = ((int(size/3.3)),(int(size/1.7)))
        fontScale = 6
        color = (5, 50, 1)
        thickness = 20
        tile_height = thisimage.shape[0]
        tile_width = thisimage.shape[1]
        # destination, char, (x,y (from top))
        cv2.putText(
            thisimage,
            charr,
            (int(thickness / 2), (tile_height - thickness)),
            font,
            fontScale,
            color,
            thickness,
            cv2.LINE_AA,
        )
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

    def addtoshelf(self, letter):
        image = self.letter(letter)

        ##print("\n\nADD2SHELF: image size {}".format(image.shape))
        padding = self.ballpadding

        x_on_shelf = 200 + (self.letters * (image.shape[1] + padding))

        # https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv

        ##print("ADD2SHELF: Shelf size {}".format(self.npa_shelf.shape))
        ##print("ADD2SHELF: image size {}".format(image.shape))

        y_on_shelf = 40

        ##print("ADD2SHELF: y from {} y to {}".format(y_on_shelf,y_on_shelf+image.shape[0]))
        ##print("ADD2SHELF: x from {} x to {}".format(x_on_shelf,x_on_shelf+image.shape[1]))

        # print("Alpha? {}".format((255 - image[:, :, :3].mean(axis=2)).astype(np.uint8)))
        # image[:, :, 3] = (255 - image[:, :, :3].mean(axis=2)).astype(np.uint8)

        self.npa_shelf[
            y_on_shelf : y_on_shelf + image.shape[0],
            x_on_shelf : x_on_shelf + image.shape[1],
        ] = image

        self.letters += 1
        return self.npa_shelf

    def show(self):
        cv2.imshow("shelf", self.npa_shelf)


cv2.startWindowThread()
rachel = CountdownLetters()
hewer = lettershelf()
cv2.waitKey(1)
quit = False
while not quit:
    quiz = rachel.genString()
    # dump to terminal
    print("\n{}\n".format(quiz))

    for i, v in enumerate(quiz):
        hewer.addtoshelf(v)
        hewer.show()
        cv2.waitKey(1)

    ourvalids = rachel.solve(quiz)
    print("Good words {} ".format(len(ourvalids)))
    for key in ourvalids:
        print("good: {}".format(key))

    mikey = None
    while mikey is None:
        mikey = cv2.waitKey(0)
        # hit space to regen
        if (mikey == ord(' ')):
            mikey = " "
            rachel.reset()
            hewer.emptyShelf()
        # hit escape to finish
        if mikey == 27:
            quit = True


cv2.destroyAllWindows()

exit(0)
