# Author: Sam Pai
# Date: 8/12/2020
# Description: This Python class creates an implementation of the Black Box game (created by Eric Solomon) where users
# try to shoot rays into the black box in order to try and hit the atoms inside. There must be at at least one atom
# on the board to start.


class BlackBoxGame:
    """ This class is a virtual representation of the Black Box Game. Users can utilize the various methods in this
    class to play the game. The game will take place on a 10x10 grid where the atoms must be placed somewhere on rows
    1-8 and columns 1-8. Rays must be shot from rows 0 and 9 and columns 0 and 9 (corner locations are not allowed). """

    def __init__(self, atom_list):
        """ Init method that initializes the game with various private data members. The methods of the BlackBoxGame
        class utilize these private data members to update and play the game. """
        self._board = [
            # 0   #1  #2  #3  #4  #5  #6  #7  #8   #9
            ['', '', '', '', '', '', '', '', '', ''],  # 0

            ['', '', '', '', '', '', '', '', '', ''],  # 1
            ['', '', '', '', '', '', '', '', '', ''],  # 2
            ['', '', '', '', '', '', '', '', '', ''],  # 3
            ['', '', '', '', '', '', '', '', '', ''],  # 4
            ['', '', '', '', '', '', '', '', '', ''],  # 5
            ['', '', '', '', '', '', '', '', '', ''],  # 6
            ['', '', '', '', '', '', '', '', '', ''],  # 7
            ['', '', '', '', '', '', '', '', '', ''],  # 8

            ['', '', '', '', '', '', '', '', '', '']  # 9
        ]
        self._score = 25
        self._atoms = atom_list  # all atoms that have been inserted into the game.
        self._guessed_locations = set()  # will not contain duplicate locations.
        self._direction = None  # determines which direction the ray is moving.
        self._exit_positions = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                                (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8),
                                (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                                (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9)]
        self._hit_atoms = []
        self._used_positions = set()  # contains the entry/exit points of rays (no repeats).
        self._initial_position = None  # initial position of the ray.
        self._current_position = None  # current position of the ray.
        self._was_there_a_hit = False

    def get_score(self):
        """ This method returns the user's score via the private data member in the init method."""
        return self._score

    def get_atoms_left(self):
        """ This method communicates with the init method to return how many atoms are left on the board."""
        return len(self._atoms) - len(self._hit_atoms)

    def set_direction(self, coordinates):
        """ This method accepts the coordinates of the current position to determine which direction the ray will be
        travelling. Will be updated depending on interactions with atoms. Coordinates accepted as (row, col)."""
        # coordinates[0] represents the row and coordinates[1] represents the column
        if coordinates[0] == 0:
            self._direction = 'DOWN'
        elif coordinates[0] == 9:
            self._direction = 'UP'
        elif coordinates[1] == 0:
            self._direction = 'RIGHT'
        else:
            self._direction = 'LEFT'

    def moving_left(self):
        """ Method that checks the directional private data member and returns True if the direction is
        LEFT. Will be used by the shoot_ray method to move the ray through the board. """
        if self._direction == 'LEFT':
            return True
        else:
            return False

    def moving_up(self):
        """ Method that checks the directional private data member and returns True if the direction is
        UP. Will be used by the shoot_ray method to move the ray through the board. """
        if self._direction == 'UP':
            return True
        else:
            return False

    def moving_right(self):
        """ Method that checks the directional private data member and returns True if the direction is
        RIGHT. Will be used by the shoot_ray method to move the ray through the board. """
        if self._direction == 'RIGHT':
            return True
        else:
            return False

    def moving_down(self):
        """ Method that checks the directional private data member and returns True if the direction is
        DOWN. Will be used by the shoot_ray method to move the ray through the board. """
        if self._direction == 'DOWN':
            return True
        else:
            return False

    def change_direction_to_left(self):
        """ Method that updates the directional private data member to LEFT. This method will be called when a ray
        interacts with an atom, whether that be a reflection, deflection, or double deflection. """
        self._direction = 'LEFT'

    def change_direction_to_right(self):
        """ Method that updates the directional private data member to RIGHT. This method will be called when a ray
        interacts with an atom, whether that be a reflection, deflection, or double deflection. """
        self._direction = 'RIGHT'

    def change_direction_to_up(self):
        """ Method that updates the directional private data member to UP. This method will be called when a ray
        interacts with an atom, whether that be a reflection, deflection, or double deflection. """
        self._direction = 'UP'

    def change_direction_to_down(self):
        """ Method that updates the directional private data member to DOWN. This method will be called when a ray
        interacts with an atom, whether that be a reflection, deflection, or double deflection. """
        self._direction = 'DOWN'

    def has_atom_on_right(self, current_position):
        """ Within each movement of the ray through the board, this method will be called to check if there is an atom
        on the right side of the current ray's position. Returns True if there is, False if there isn't. """
        next_position = (current_position[0], current_position[1] + 1)  # right position is just column + 1.
        for atom in self._atoms:
            if next_position == atom:
                return True
        return False

    def has_atom_on_left(self, current_position):
        """ Within each movement of the ray through the board, this method will be called to check if there is an atom
        on the left side of the current ray's position. Returns True if there is, False if there isn't. """
        next_position = (current_position[0], current_position[1] - 1)  # left position is just column - 1.
        for atom in self._atoms:
            if next_position == atom:
                return True
        return False

    def has_atom_top_right(self, current_position):
        """ Within each movement of the ray through the board, this method will be called to check if there is an atom
        on the upper right side of the current ray's position. Returns True if there is, False if there isn't. """
        next_position = (current_position[0] - 1, current_position[1] + 1)  # row - 1 and column + 1.
        for atom in self._atoms:
            if next_position == atom:
                return True
        return False

    def has_atom_top_left(self, current_position):
        """ Within each movement of the ray through the board, this method will be called to check if there is an atom
        on the upper left side of the current ray's position. Returns True if there is, False if there isn't. """
        next_position = (current_position[0] - 1, current_position[1] - 1)  # row - 1 and column - 1
        for atom in self._atoms:
            if next_position == atom:
                return True
        return False

    def has_atom_above(self, current_position):
        """ Within each movement of the ray through the board, this method will be called to check if there is an atom
        right above the current ray's position. Returns True if there is, False if there isn't. """
        next_position = (current_position[0] - 1, current_position[1])  # row - 1 to check above, column stays the same.
        for atom in self._atoms:
            if next_position == atom:
                return True
        return False

    def has_atom_below(self, current_position):
        """ Within each movement of the ray through the board, this method will be called to check if there is an atom
        directly below the current ray's position. Returns True if there is, False if there isn't. """
        next_position = (current_position[0] + 1, current_position[1])  # row + 1 to check below, column stays the same.
        for atom in self._atoms:
            if next_position == atom:
                return True
        return False

    def has_atom_bottom_left(self, current_position):
        """ Within each movement of the ray through the board, this method will be called to check if there is an atom
        on the lower left side of the current ray's position. Returns True if there is, False if there isn't. """
        next_position = (current_position[0] + 1, current_position[1] - 1)  # row + 1 and col - 1.
        for atom in self._atoms:
            if next_position == atom:
                return True
        return False

    def has_atom_bottom_right(self, current_position):
        """ Within each movement of the ray through the board, this method will be called to check if there is an atom
        on the lower right side of the current ray's position. Returns True if there is, False if there isn't. """
        next_position = (current_position[0] + 1, current_position[1] + 1)  # col + 1 and row + 1
        for atom in self._atoms:
            if next_position == atom:
                return True
        return False

    def shoot_ray(self, row, col):
        """ This method accepts a specific row and col position for the initial input location of the ray and returns
        False if the input location is not valid, None if there is a hit, or a tuple containing the exit location of
        the ray. This method calls a series of helper methods to move the ray through the board. """

        # if row and col are both edges, then it's a corner.
        if col in [0, 9] and row in [0, 9]:
            return False
        # if neither row nor col is on the edge, then you can't shoot a ray from there either.
        elif col not in [0, 9] and row not in [0, 9]:
            return False
        # if either row or col is outside of the 0-9 range, it's invalid.
        elif col not in range(0, 10) or row not in range(0, 10):
            return False
        else:
            self._current_position = (row, col)
            self._initial_position = (row, col)
            self.set_direction(self._current_position)  # sets the direction depending on what side ray starts.
            first_move = True
            while self._current_position not in self._exit_positions or (first_move == True):
                # this loop keeps running as long as the entry ray has not exited the board yet.
                first_move = False
                if self._was_there_a_hit:
                    break  # if there was a hit, ray never exits so this break is needed.
                if self.moving_right():  # calls helper method to determine the direction of the ray.
                    self.move_ray_right(self._current_position)

                elif self.moving_left():
                    self.move_ray_left(self._current_position)

                elif self.moving_up():
                    self.move_ray_up(self._current_position)

                elif self.moving_down():
                    self.move_ray_down(self._current_position)

            if self._was_there_a_hit:
                return None
            else:
                return self.handle_exit()  # will return the current position which is the exit point of the ray.

    def handle_exit(self):
        """ Helper method that executes after the while loop has finished running. If the entry point of the ray is
        equal to the exit point of the ray, that means the user's score will be deducted by 1. Contrarily, if
        the entry/exit points are different, user's score will be deducted by 2 points. Entry and exit points
        will only be counted once for point deduction."""
        if self._initial_position == self._current_position:  # if it's a reflection or a double deflection.
            if self._initial_position not in self._used_positions:
                self._used_positions.add(self._current_position)
                self._score -= 1  # only deducted if entry point has never been used before.
                return self._current_position
            return self._current_position
        else:
            if self._current_position not in self._used_positions and self._initial_position not in self._used_positions:
                # only enters here if both the entry/exit points of the ray have never been used before.
                self._used_positions.add(self._current_position)
                self._score -= 2.  # ray was able to exit in a different spot
                return self._current_position
            return self._current_position

    def move_ray_right(self, current_position):
        """ Method for a ray that is moving right. It accepts the current position of the ray, and then checks all 4
        corners to see if there is an atom and change the direction of the ray accordingly. """
        if self.has_atom_on_right(current_position):  # if the ray is moving right and there is an atom on the right,
            # that means there is a hit.
            self.hit((current_position[0], current_position[0] + 1))  # send the atom to the helper function.
            self._was_there_a_hit = True
            # print("has atom on right")

        elif self.has_atom_bottom_right(current_position) and self.has_atom_top_right(current_position):
            # this would be a double deflection
            self.change_direction_to_left()  # go back in the direction the ray came from.
            # print("dbl def, moving left")

        elif self.has_atom_bottom_right(current_position):
            self.change_direction_to_up()

        elif self.has_atom_top_right(current_position):
            self.change_direction_to_down()

        else:
            # ray can keep moving right
            # move the current pos right one.
            # print('can move right')
            self._current_position = (current_position[0], current_position[1] + 1)

    def move_ray_left(self, current_position):
        """ Method for a ray that is moving left. It accepts the current position of the ray, and then checks all 4
        corners to see if there is an atom and change the direction of the ray accordingly. """
        if self.has_atom_on_left(current_position):
            self.hit((current_position[0], current_position[0] - 1))  # send the atom to the helper function
            self._was_there_a_hit = True
            # print("has atom on left")

        elif self.has_atom_bottom_left(current_position) and self.has_atom_top_left(current_position):
            # this would be a double deflection
            self.change_direction_to_right()
            # print("dbl def, moving right")

        elif self.has_atom_bottom_left(current_position):
            self.change_direction_to_up()

        elif self.has_atom_top_left(current_position):
            self.change_direction_to_down()

        else:
            # ray can keep moving left
            # move the current pos left one.
            # print('can move left')
            self._current_position = (current_position[0], current_position[1] - 1)

    def move_ray_up(self, current_position):
        """ Method for a ray that is moving up. It accepts the current position of the ray, and then checks all 4
        corners to see if there is an atom and change the direction of the ray accordingly. """
        if self.has_atom_above(current_position):
            self.hit((current_position[0] - 1, current_position[0]))  # send the atom to the helper function
            self._was_there_a_hit = True
            # print("has atom above")

        elif self.has_atom_top_left(current_position) and self.has_atom_top_right(current_position):
            # this would be a double deflection
            self.change_direction_to_down()
            # print("dbl def, moving down")

        elif self.has_atom_top_left(current_position):
            self.change_direction_to_right()

        elif self.has_atom_top_right(current_position):
            self.change_direction_to_left()

        else:
            # ray can keep moving up
            # move the current pos up one.
            # print('can move up')
            self._current_position = (current_position[0] - 1, current_position[1])  # col stays the same

    def move_ray_down(self, current_position):
        """ Method for a ray that is moving down. It accepts the current position of the ray, and then checks all 4
        corners to see if there is an atom and change the direction of the ray accordingly. """
        # print("move ray down")
        if self.has_atom_below(current_position):
            self.hit((current_position[0] + 1, current_position[0]))  # send the atom to the helper function
            self._was_there_a_hit = True
            # print("has atom below")

        elif self.has_atom_bottom_left(current_position) and self.has_atom_bottom_right(current_position):
            # this would be a double deflection
            self.change_direction_to_up()
            # print("dbl def, moving up")

        elif self.has_atom_bottom_left(current_position):
            self.change_direction_to_right()

        elif self.has_atom_bottom_right(current_position):
            self.change_direction_to_left()

        else:
            # ray can keep moving down
            # move the current pos down one.
            # print('can move down')
            self._current_position = (current_position[0] + 1, current_position[1])

    def guess_atom(self, row, col):
        """ This method allows the user to guess the location of the atom. It accepts an row and a col location as the
        input and utilizes the list of lists representing the board to determine if the guess is correct or not.
        If the guess is incorrect then the user will be penalized 5 points. """

        userGuess = (row, col)
        if userGuess in self._atoms:
            self._guessed_locations.add(userGuess)
            return True
        else:
            if userGuess in self._guessed_locations:
                return False
            else:  # if this location has not been guessed before, and it is incorrect
                self._guessed_locations.add(userGuess)
                self._score -= 5
                return False

    def hit(self, atom):
        """ This method is called by the move_ray_(left, right, up, down) methods to determine if there was a hit.
        There will be no exit array. If the entry point of the ray, that causes this hit, has never been used before,
        then a user's score is decremented by 1. """
        if atom not in self._hit_atoms:
            self._hit_atoms.append(atom)  # if the atom has never been hit before, it is added to the list.
            if self._initial_position not in self._used_positions:
                self._used_positions.add(self._initial_position)
                self._score -= 1


# test = [(3,7),(6,4),(8,1)]
# test2 = [(4, 8) ]
# test3 = [(3, 2), (3, 7), (6,4), (8,7)]
# game = BlackBoxGame(test3)
# print(game.get_score())
# print(game.get_atoms_left())
# print("Shoot Ray: ", game.shoot_ray(0,3))
# print("Shoot Ray: ", game.shoot_ray(4,9))
#
# print(game.guess_atom(5,2))
# print(game.guess_atom(7,2))
# # print(game.guess_atom(4, 5))
# print(game.get_score())
# print(game.get_atoms_left())










