# Black-Box-Game
An abstract Python game for one or two players, which simulates shooting rays into a black box to determine the locations of "atoms" hidden inside the box.

## Getting Started

To play this game, simply clone the repository onto your local machine and open the .py file in an integrated development environment (IDE) such as PyCharm. 

### Prerequisites

Must have an IDE to play this game (IDLE, PyCharm, Spyder, Eclipse, PyDev, Visual Studio, etc...)

## Rules of the Game
This game is a virtual Python imitation of Eric Solomon's Black Box Game, which can be found here https://en.wikipedia.org/wiki/Black_Box_(game). Users can shoot rays from rows 0 and 9 or columns 0 and 9 (excluding the 4 corners). Atoms must be placed somewhere in rows 1-8 and columns 1-8. A user starts with 25 points and the goal of the game is to hit all the atoms while maintaining the highest score possible. Everytime a ray enters the box, a user gets deducted 1 point. If the ray exits in a different location than the entry point, another point is deducted. Rays can either hit an atom, deflect off an atom, reflect off an atom, double deflect off an atom, or completely miss an atom. These conditions are explained more in depth in the wikipedia link provided above. Users can also guess the location of an atom. If guessed incorrectly, 5 points will be deducted from the user. 

## How to Play
Below is an example of how you could play the game:

Step 1: Create a new instance of the BlackBoxGame class and initialize where the atoms will be.
```
game = BlackBoxGame([(3,2),(1,7),(4,6),(8,8)])
```
Step 2: Choose a valid place on the board to shoot the initial ray.
```
game.shoot_ray(0,2)
```
Step 3:Depending on the path of your ray, you can try guessing where an atom is.
```
game.guess_atom(5,5)
```
Step 4: Through the game, you can check your score to determine how the ray interacted with the different atoms in the box.
```
game.get_score()
```
Step 5: If you want to check how many atoms are left, you can enter the following command.
```
game.atoms_left()
```

## Built With

* Python

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email (samuelpai16@gmail.com), or any other method with the owners of this repository before making a change. Building a user interface would be a contributing priority for this game. 

## Author

* **Sam Pai**

