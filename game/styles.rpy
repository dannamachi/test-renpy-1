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

style cwin:
    xfill True
    ysize None
    bottom_padding 20
    left_padding 10
    right_padding 10
    background Image("images/interfaces/chatbox.png", xalign=0.5, yalign=1.0)

style chat_name:
    xpos 50
    xanchor 0.0 #1.0
    ypos 20

style chat_name_text:
    bold True

style chat_text:
    ypos 60
    xanchor 0.0

style chat_text2:
    ypos 20
    xanchor 0.0

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