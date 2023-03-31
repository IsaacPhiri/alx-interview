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

    # Create a list of keys for available boxes,
    # initialized with the first key
    available_keys = [0]

    # Create a list to keep track of unlocked boxes,
    # initialized with the first box
    unlocked_boxes = [0]

    # Iterate through the list of available keys
    # and unlock any boxes that correspond to the key
    while available_keys:
        key = available_keys.pop()

        # Iterate through the list of keys in the
        # box that corresponds to the key
        for box_key in boxes[key]:

            # If the key is not already in the available_keys
            # or unlocked_boxes lists, add it to available_keys
            if box_key not in available_keys and box_key not in \
                    unlocked_boxes and box_key < len(boxes):
                available_keys.append(box_key)

        # Add the box to unlocked_boxes
        if key not in unlocked_boxes:
            unlocked_boxes.append(key)

    # If there are any locked boxes, return False, otherwise return True
    return len(unlocked_boxes) == len(boxes)
