#!/usr/bin/python3
"""
    You have n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each box may contain keys
    to the other boxes.

    Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """Initialize to track unlocked boxes"""
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = boxes[0]
    to_visit = [0]

    while to_visit:  # loop through until no more boxes to visit
        current_box = to_visit.pop()

        for key in boxes[current_box]:  # iterate over keys in current box
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # unlock the box
                to_visit.append(key)  # add newly unlocked box to visit list

    return all(unlocked)
