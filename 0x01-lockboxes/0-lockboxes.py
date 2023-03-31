#!/usr/bin/python3
"""Locked boxes algorithm"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes (list): A list of lists.
    Each list contains keys that can open other boxes.

    Returns:
    True if all boxes can be opened, else False.
    """
    available_keys = [0]
    unlocked_boxes = [0]

    while available_keys:
        key = available_keys.pop()

        for box_key in boxes[key]:
            if box_key not in available_keys and box_key not in \
                    unlocked_boxes and box_key < len(boxes):
                available_keys.append(box_key)

        if key not in unlocked_boxes:
            unlocked_boxes.append(key)

    return len(unlocked_boxes) == len(boxes)
