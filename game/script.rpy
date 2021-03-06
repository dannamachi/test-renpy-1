# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define phone = Character("Phone", screen='phone_display')
define phone2 = Character("Not Phone", screen='phone_display')

init python:
    def p(what, **kwargs):
        if gamedata.isSendingToPhone():
            gamedata.addToList(phone, what)
        phone(what, **kwargs)

    def p2(what, **kwargs):
        if gamedata.isSendingToPhone():
            gamedata.addToList(phone2, what)
        phone2(what, **kwargs)

# game flow
default gFlow = True
default gamedata = GameData()
default assets = AssetProvider()

# splash screen
label splashscreen:
    scene black
    with Pause(1)

    show text "Mochi presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


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
            e "Eh, goodbye then !"
            return

        if len(gamedata.name) == 0:
            $ gamedata.name = 'Stupido'

            e "Since you have no preference, I'll call you something arbitrary then ^^"
            e "Hello and welcome, [gamedata.name] !"
        else:
            e "Brilliant ! Welcome to our humble world, [gamedata.name] !"
            e "Hope you enjoy your stay :D"

        if gamedata.name != 'Stupido':
            e "Hmmmm... sounds good, let's go !"
            $ gFlow = False
        else:
            e "Hmmmmmmmmm... no, this ain't it."

    # blinking test
    show eye blinking at topleft

    # window hide Dissolve(1.0)
    show screen magic_phone

    # show button to toggle show/hide phone
    show screen phone_icon

    p "Wow"
    p "This is pretty cool ngl."
    p "I see now..."

    $ gamedata.setHidePhoneDisplay()
    $ gamedata.setSendToPhone(True)

    p "This is going straight to the phone"
    p "So cool isn't it !?"

    # calling some label
    call some_scene

    # This ends the game.
    return

label some_scene:
    $ gamedata.setHidePhoneDisplay(False)
    p "Eh ?"
    p "Right."
    $ gamedata.setHidePhoneDisplay(True)
    p "Message here."
    p "Another message here."
    p2 "Message grouping to be done later."
    p2 "This is to test scrolling and overflow."
    p "I hope i don't have to do the 4-piece cropping plan if possible."
    p2 "Cool as it is, i think it might be a bit too much eh."
    p "Haiz, it do be hard when things are conveniently modularized but you don't know how it all works."
    p2 "Testing text wrapping as well."
    p "Is this long enough already ?"
    p "Let's write a bit more."
    p "Man i'm not hungry actually, but it's already evening time."
    p2 "Haiyai, mendokusai..."
    p "Mmmmmmm what should i do ?"
    p "Is this enough for you i wonder ?"
    p "Bruh wouldn't it be funny--"
    p2 "I think it's enough already teh."

    $ gamedata.setSendToPhone()
    p "This won't go to phone."
    p "Brilliant."
