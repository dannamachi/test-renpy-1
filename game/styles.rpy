style minigame_frame:
    background 'images/backgrounds/minigame.png'

style phone_frame:
    align (0.5, 0.4)
    xsize numbers.phone_width
    ysize numbers.phone_height

style phone_frame_imagemap:
    xfill True
    yfill True

style icon_phone:
    xalign 0.9
    yalign 0.2
    xsize 150
    ysize 150

style pizza_button:
    background Solid("fff", xfill=True, yfill=True)
    size_group 'pizza'

style pizza_button_text:
    line_spacing 2
    underline True

style chat_window:
    xfill True
    ysize None

transform invisible:
    alpha 0.0

transform widthToZero:
    xsize numbers.screen_width
    linear 3.0 xsize 0

transform showFadeIn:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform pizza_button_1:
    #rotate_pad False
    yoffset 150
    xoffset 80
    rotate 30

transform pizza_button_2:
    #rotate_pad False
    yoffset 250
    xoffset 30
    rotate 15

transform pizza_button_3:
    #rotate_pad False
    yoffset 350
    xoffset 15
    rotate 0

transform pizza_button_4:
    #rotate_pad False
    yoffset 450
    xoffset 30
    rotate -15

transform pizza_button_5:
    #rotate_pad False
    yoffset 550
    xoffset 80
    rotate -30