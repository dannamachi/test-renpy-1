################################################################################
## Define all images
################################################################################

init -1 python:
    images = {}
    images.player = 'images/sprites/sprite.png'
    
    blinkingPrefix = 'images/sprites/blinking/'
    images.blinkingList = [
        blinkingPrefix + 'row-1-column-1.jpg',
        blinkingPrefix + 'row-1-column-2.jpg',
        blinkingPrefix + 'row-1-column-3.jpg',
        blinkingPrefix + 'row-1-column-4.jpg'
    ]

    blackscreen = Solid("#000", xfill=True, yfill=True)
    screenshot = Solid("#fff", xfill=True, yfill=True)
    pinkscreen = Solid("#e766b6", xfill=True, yfill=True)

image eye blinking:
    images.blinkingList[0]
    pause 0.2
    images.blinkingList[1]
    pause 0.2
    images.blinkingList[2]
    pause 0.2
    images.blinkingList[3]
    pause 0.2
    images.blinkingList[2]
    pause 0.2
    images.blinkingList[1]
    pause 0.2
    images.blinkingList[0]
    pause 3.0
    repeat