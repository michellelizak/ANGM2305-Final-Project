# ANGM2305-Final-Project: Space Invaders

## Demo
Demo Video: <https://youtu.be/u4NzviOn9tQ)>

## GitHub Repository
GitHub Repo: <https://github.com/michellelizak/ANGM2305-Final-Project.git>

## Description

- Summary
	- My program is a space shooter game implemented in Python using the Pygame library. The game initializes a player character, sets up health and score parameters, creates obstacles, aliens, and an additional enemy type called "Extra," which is the extra alien spaceship. The player can move horizontally, shoot lasers, and must avoid obstacles and enemy attacks. The goal is to eliminate the alien invaders and achieve a high score. I added a custom background, a high score feature, explosions each time the player hits an alien, an explosion on the player once they run out of lives, a gradient laser, custom artwork that I designed for the characters and spaceship, a game over message, and a victory message when all aliens are destroyed, both animated with a typewriter effect. The game ends if the player runs out of lives, and a game over message is displayed. The code consists of different classes for the player, obstacles, aliens, lasers, and the game itself. The main loop handles user input, updates game elements, and continuously redraws the game screen at a set frame rate.

- Files
	- All of my python files are in a folder called code. My alien.py file is responsible for storing vital information regarding the aliens. It has an alien class, which initializes alien sprites with specific colors and score values and an extra class, which manages additional enemy sprites that appear from either the left or right side of the screen, each with their own movement speed. My laser.py file initializes a laser sprite with a specified position, speed, and screen height. The laser moves vertically on the screen, and its destroy method removes it when it goes beyond the screen boundaries. Additionally, the class includes a method, create_gradient_surface, to generate a gradient-colored laser trail. My obstacle.py file s initializes a block sprite with a specified size, color, and position. The shape list represents a pattern for arranging these blocks, forming an obstacle in the game environment. My player.py file initializes the player’s spaceship with an image, position, speed, and constraints. The get_input method captures keyboard input for moving the player horizontally and shooting lasers. It manages the recharge time for shooting lasers, ensures the player stays within the screen constraints, and updates the position of the player's lasers. My background image and other graphics are in my graphics folder, and my font file used for the game over and scoring text is in my font folder.

- Accomplishments
	- What I am most proud of with my program would probably be my explosion animations, text animations, and my custom characters. My characters didn’t require much programming, but I had fun designing them. My explosion and text animations though, were very complicated and I had no idea where to start with them.

- Improvements
	- One area of improvement would be that the explosions hitting the aliens make the game a little bit choppy for lack of better wording, and I wish I could have improved upon it. I also planned originally to add a respawn mechanism to the game, but it was too complex for me to figure out how to implement it so I decided to add other features instead, like the exploding animation, text animations, and gradient effects on the lasers. Also, for some reason after I added the main function my extra alien at the top of the screen disappeared and I could not figure out how to get it back.

##

I referenced the video “Creating Space Invaders in Pygame/Python” by Clear Code on Youtube as a base, which I linked below. 

<https://www.youtube.com/watch?v=o-6pADy5Mdg>


