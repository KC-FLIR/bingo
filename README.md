# bingo
bingo project - just a bit of fun creating random bingo cards, and a bingo ball calling program

two very similar python scripts that really should use a common class for rendering images on screen.. anyhow

* bingosheet.py which will generate 2000 random bingo cards
These will be split into 200 numbered PNG images for ten teams, so thats team-(1-10)_card-nnn (1-200)

* bingoballer.py which will pull, randomly, 90 balls numbered 1-90
The ball will initially be rendered in a window for the perosn running the script to see, 
then on a keyboard click, this will be added to a window containing all the balls, in called order

The idea was that in a Zoom call, the caller can "share" the ball-box window so the users can see the balls
But the render of the ball first occurs to the caller, and is not visible until the button click
This allows the caller to do their fancy call of two fat ducks or whatever before the user gets to see the ball

CAVEAT - the cards are 4 rows of 5 numbers, randomly selected. Initial feedback is that this is not the way real
cards are printed, and this totally random render makes the game harder.  True enough, when I ran this live 
with teams, most had "missed" numbers that actually had been called.  So the bingo card generator needs some work
