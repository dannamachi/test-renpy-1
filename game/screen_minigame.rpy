screen minigame():

    ## This ensures that any other menu screen is replaced.
    tag minigame

    add images.player

    ## This empty frame darkens the main menu.
    frame:
        style "minigame_frame"

    vbox:
        textbutton "Magic Close" action Hide('minigame')
