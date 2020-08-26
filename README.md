# Black-Box-Game
An abstract Python game for one or two players, which simulates shooting rays into a black box to determine the locations of "atoms" hidden inside the box.

## Getting Started

To play this game, simply clone the repository onto your local machine and open the .py file in an integrated development environment (IDE) such as PyCharm. 

### Prerequisites

Must have an IDE to play this game (IDLE, PyCharm, Spyder, Eclipse, PyDev, Visual Studio, etc...)

## Rules of the Game
This game is a virtual Python imitation of Eric Solomon's Black Box Game, which can be found here https://en.wikipedia.org/wiki/Black_Box_(game). Users can shoot rays from rows 0 and 9 or columns 0 and 9 (excluding the 4 corners). Atoms must be placed somewhere in rows 1-8 and columns 1-8. A user starts with 25 points and the goal of the game is to hit all the atoms while maintaining the highest score possible. Everytime a ray enters the box, a user gets deducted 1 point. If the ray exits in a different location than the entry point, another point is deducted. Rays can either hit an atom, deflect off an atom, reflect off an atom, double deflect off an atom, or completely miss an atom. These conditions are explained more in depth in the wikipedia link provided above. Users can also guess the location of an atom. If guessed incorrectly, 5 points will be deducted from the user. 

## How to Play
Step 1: create a new instance of the BlackBoxGame class
```
game = BlackBoxGame([(3,2),(1,7),(4,6),(8,8)])
```

## Built With

* Node.Js - used for our server environment
* Express - used to create the API routes 
* MySQL - used to store data of trips, activities, and users
* Plop -node package used to create structure of our app, specifically presentational components /controller components and express controllers/ express routers. 
* Sequelize - our orm to map object syntax onto our MySQL database schemas
* React - used to create our front end display 
* Reactstrap/Bootstrap - used to style our app
* Javascript - client side programming language to handle functionality
* Auth0 - used to authenticate and authorize users 

## Contributing

N/A at this time

## Authors

* **Sam Pai**
* **DivyaGayathri Enjamuri**
* **Max Reinmueller**
* **Karishma Hattar**

## License



## Acknowledgments

* The instructional staff at the UCSD Extention's Web Development Bootcamp
