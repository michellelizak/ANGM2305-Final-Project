# Space Invasion

## Repository
<https://github.com/michellelizak/ANGM2305-Final-Project>

## Description
My program is a mini game that implements digital art by having a visuals and characters designed by me, and contains animated and interactive pixels that simulate movement (in the form of a game).

## Features
- Feature 1: Player and Laser
	- Player will shoot lasers in an attempt to kill all of the aliens. I would create a player class which would be defined using the Pygame library, and the player's position, speed, and horizontal constraint would be initialized. The class would include methods for handling player input and shooting lasers.

- Feature 2: Aliens
	- Pixel aliens will move across the screen in a unique pattern. I would do this by making an alien class that initializes an alien sprite with a specified color, position, and point value, and would create another class that allows the sprite to move from left to right

- Feature N: Kill and Win Screen
	- A kill screen and win screen will be displayed and player health and score will be kept track of. The code in my main function would keep track of the score by incrementing it when player lasers hit aliens or extra elements. The victory message would be drawn on the screen during the game loop when the condition for winning is met.

## Challenges
- Determine how to make complex custom pixel artwork of characters (different from the video provided)
- Determine how to keep track of high scores
- Determine how to make the aliens respawn during a round for an additional challenge to the player

## Outcomes
Ideal Outcome:
- Create a space invasion game with characters fully designed by me, aliens that can respawn after killed with lasers by the player, keeps track of the player's high score and current score, and a “You Win!”/”Game Over” screen.

Minimal Viable Outcome:
- Create a functioning space invasion game with animated aliens that are somewhat modified, a player that can move across the screen and shoot lasers at the aliens, a score tracker on the screen, and a “You Win!”/”Game Over” screen that is animated in some way.

## Milestones

- Week 1
  1. Create player and laser mechanism
  2. Create obstacles

- Week 2
  1. Create aliens
  2. Determine how to create respawn mechanism

- Week N (Final)
  1. Create score system and high score memory
  2. Create victory/loss screen 

##

I will be using the video “Creating Space Invaders in Pygame/Python” by Clear Code on Youtube as a base, which I linked below. 

<https://www.youtube.com/watch?v=o-6pADy5Mdg>
