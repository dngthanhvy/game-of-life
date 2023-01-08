# Game of Life

Python implementation of Conway's Game of Life.

LeetCode: https://leetcode.com/problems/game-of-life/

## Rules

* Any live cell with fewer than two live neighbors dies as if caused by under-population.
* Any live cell with two or three live neighbors lives on to the next generation.
* Any live cell with more than three live neighbors dies, as if by over-population.
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Solution method

Solved using a naive way.

The board is represented as an 2D array of size `m x n` to be transformed into a `Board` object which contains a 2D
array of `Cell` objects with empty neighbors.
(Runtime: O(mn))

Each `Cell` object neighbors are obtained by iterating through `Board` and checking the values of all neighbors.
(Runtime: O(mn))

The `Cell` objects are updated by iterating through the `Board` object. The next state is stored in the `next_state`
attribute of the `Cell` object.
(Runtime: O(mn))

The `Board` object is updated by iterating through the `Board` object and updating the `state` attribute of the `Cell`
object with its `next_value`. The `next_value` is then reset to `None` for the next generation.
(Runtime: O(mn))

Total runtime: `O(mn)`
