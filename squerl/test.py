# Requirement 5: Which change will you make in the game to have more fun? Explain and add it!
# Comment all added or modified command with '# added or modified to provide functionality'
# added or modified to provide functionality
# I'll add a speed boost for the player when a key is held down, making the game more dynamic.
# Speed boost variables
SPEEDBOOST = 3
boost = False

# ...

# Inside the event handling loop:
elif event.type == KEYDOWN:
    if event.key in (K_UP, K_w):
        moveDown = False
        moveUp = True
    # ...

    # Requirement 5: Explanation and addition
    elif event.key == K_SPACE:
        # If the space key is pressed, enable speed boost
        boost = True

elif event.type == KEYUP:
    # ...

    # Requirement 5: Explanation and addition
    elif event.key == K_SPACE:
        # If the space key is released, disable speed boost
        boost = False

# ...

# Inside the actual movement logic:
# actually move the player
if moveLeft:
    playerObj["x"] -= MOVERATE * SPEEDBOOST if boost else MOVERATE
if moveRight:
    playerObj["x"] += MOVERATE * SPEEDBOOST if boost else MOVERATE
if moveUp:
    playerObj["y"] -= MOVERATE * SPEEDBOOST if boost else MOVERATE
if moveDown:
    playerObj["y"] += MOVERATE * SPEEDBOOST if boost else MOVERATE
