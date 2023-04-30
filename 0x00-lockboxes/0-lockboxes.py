#!/usr/bin/python3

def canUnlockAll(boxes):
    keys = [0]
    visited = [False] * len(boxes)
    visited[0] = True

    while keys:
        key = keys.pop(0)
        for box in boxes[key]:
            if box < len(boxes) and not visited[box]:
                visited[box] = True
                keys.append(box)

    return all(visited)
