# Problem

https://edabit.com/challenge/LM5d2b6YG5vXuYiME


Can You Enter the Cave?
You are playing a video game. Your screen can be represented as a 2D array, where 0s represent walkeable areas and 1s represent unwalkeable areas. You are currently searching for the entrance to a cave that is located on the right side of the screen. Your character starts anywhere in the leftmost column.

Create a function that determines if you can enter the cave. You can only move left, right, up, or down (not allowed to move diagonally).

To illustrate:

[
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 0]
]
You found the entrance! Function should output True.

[
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 1, 1, 1, 1, 0]
]
Nope, keep looking. Function should output False.

Examples
can_enter_cave([
  [0, 1, 1, 1, 0, 1, 1, 0],
  [0, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1, 1, 0]
]) ➞ False

# You cannot walk diagonally!


can_enter_cave([
  [0, 1, 1, 1, 0, 1, 1, 0],
  [0, 0, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 1, 1, 1, 1, 0]
]) ➞ True


can_enter_cave([
  [0, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 0],
  [0, 1, 1, 0, 0, 1, 1, 0]
]) ➞ False
Notes
You are seeing the game screen from a birds-eye view.
Another way of thinking about it: You can enter the cave if you can move from the left side of the screen to the right side by only walking up, down or right.
The entrance is not necessarily the first square, you may have to search for it in the left hand column.

# Retrospective

Lucas Medeiros will bring problems to the next Dojo

## Attendees

- Lucas Medeiros
- Brenner Vaz
- Fernando Bertoldi
- Marlon Trapp

## :)
- Recursion
- Good knowledge on the language
- It was fun

## :(
- Recursion
- Low attendance rate
- Avoid raw mathematical expressions without aliases
