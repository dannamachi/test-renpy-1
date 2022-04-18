﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# game flow
default gFlow = True
default gamedata = GameData()


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # menu loop test
    while gFlow:
        e "I've been told you're to be called [gamedata.name], but..."
        e "Is there something else you would like to be called ?"

        $ gamedata.name = renpy.input('Enter your name, or leave blank for default ^^').strip()

        if (gamedata.name == 'exit'):
            $ gFlow = False
            e "Eh, goodbye then !"

        if len(gamedata.name) == 0:
            $ gamedata.name = 'Stupido'

            e "Since you have no preference, I'll call you something arbitrary then ^^"
            e "Hello and welcome, [gamedata.name] !"
        else:
            e "Brilliant ! Welcome to our humble world, [gamedata.name] !"
            e "Hope you enjoy your stay :D"

    # This ends the game.

    return
