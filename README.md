# General knowledge quiz

This is a small battleships game desidgned for single player use. The object of the game is to guess the correct row and column that randomly generated ships will appear on. Once you have guessed all of the correct locations of the ships you will win the game. If you run out of turns you will lose the game.

![Landing content](https://github.com/Colmc2966/battleships/blob/main/media/Home%20-%20p3.JPG)

## Features 

### Existing Features

- __Randomly generates ship locations__

![Board](https://github.com/Colmc2966/battleships/blob/main/media/Board.JPG)

 - The Player is given a blank board in order to visiualize the game but cannot see ship locations uinl;ess they were to guess correctly.
- Once the player guesses a correct ship location an 'X' will appear to signify a hit
- if a player misses a ship, a '-' will appear in the guessed location to signify a miss

![Miss](https://github.com/Colmc2966/battleships/blob/main/media/MISS.JPG)
![Hit](https://github.com/Colmc2966/battleships/blob/main/media/Hit%20battleship%20indication.JPG)


- __Only allows relevant inputs__

  The terminal will only allow relevant inputs between row 1-6 and column A-F. Upon incorrect input termimal will contiunue looping asking for correct input.
  once correct input is sent the game progresses.

![Input Incorrect](https://github.com/Colmc2966/battleships/blob/main/media/incorrect%20input%20-%20p3.JPG)
![Inputs Correct](https://github.com/Colmc2966/battleships/blob/main/media/correct%20input.JPG)

-__Turns feature__

The game has a turn feature which will end the game no matter what after 8 turns. turns remainig is presented to the user after each guess
![Turns remaining](https://github.com/Colmc2966/battleships/blob/main/media/turns%20remaining.JPG)

- __Losing the game__

If the player runs out of turns without hitting all the battleships they will lose and can run the code to play again.

![Losing game](https://github.com/Colmc2966/battleships/blob/main/media/game%20over%20message.JPG)

-__Winning the game__

If the player guesses all correct locations of the battleships, they have won the game

![Winning game](https://github.com/Colmc2966/battleships/blob/main/media/winning%20message.JPG)

### Features Left to Implement

- Looking to implement a way for users to competer against one another
- Looking to implement a way for users to select the size of the board and how many ships to implement

## Testing 

- During my testing I verified that all inputs and outputs work as expected
- I passed the code through PEP8 and came back with no issues
- incorrect inputs are not allowed and wouldnt disrupt the game

### Validator Testing 

- PEP 8
  - No errors were returned when passing through the official ![PEP 8 validator](https://github.com/Colmc2966/battleships/blob/main/media/PEP%208%20check.JPG)

### Fixed bugs

- Fixed a bug causing game to crash when inputting invalid input
- Fixed a bug which placed hit markers where a guess was missed
- fixed a bug which caused the board size to be the unintended size
- fixed a bug which was causing 'x' and '-' to not display on the board

### Unfixed Bugs

- no unfixed bugs remaining

## Deployment

 

- I deployed this site to Heroku. The steps are as follows 

  - Go to Heroku main dashboard page
  - Select create app
  - ensure the buildbacks are set to pythoin and node.js in that order
  -  Link the Heroku app to the correct repository
  - Click on deploy

The live link of my project can be found here - [General Knowledge quiz](https://colmc2966.github.io/General-knowledge-quiz/)


## Credits 

### Content 
- Method of creating the guessing_code was inspired by [w3schools](https://www.w3schools.com)
- Method of fixing a bug with not being able to print 'X' or '-' to the board when inputs are sent was inspired by [Real Python](https://realpython.com)
- Several small syntax orders were inspired from [stack overflow](https://stackoverflow.com/)
- Method of deployment was inspired by Code Institute
