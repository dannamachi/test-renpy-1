################################################################################
## Define all images
################################################################################

init -1 python:
    images = {}
    images.player = 'images/sprites/sprite.png'

    blackscreen = Solid("#000", xfill=True, yfill=True)
    screenshot = Solid("#fff", xfill=True, yfill=True)
    pinkscreen = Solid("#e766b6", xfill=True, yfill=True)