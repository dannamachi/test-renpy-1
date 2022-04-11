screen minigame():

    ## This ensures that any other menu screen is replaced.
    tag minigame

    ## This empty frame darkens the main menu.
    frame:
        style "minigame_frame"

    add images.player xalign 0.0 yalign 0.0

    vbox:
        textbutton "Magic Close" action Hide('minigame')
