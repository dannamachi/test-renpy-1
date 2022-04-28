screen minigame():

    ## This ensures that any other menu screen is replaced.
    tag minigame

    style_prefix 'minigame'

    ## Frame for background and all static displayables
    frame:
        # cud
        default pong = ClassicAnimator(assets.anima_1_right)
        add pong
        
        fixed:
            text 'Hello' xpos 400 # for testing
            add 'eye blinking'

    # add images.player xalign 0.0 yalign 0.0

    vbox:
        textbutton "Magic Close" action Hide('minigame')
