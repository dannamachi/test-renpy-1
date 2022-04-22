screen magic_phone():
    style_prefix "phone"

    # show top
    zorder 10

    frame:
        at showFadeIn
        id 'phone'

        imagemap:
            ground pinkscreen
            hotspot numbers.button_1:
                action Return()

        add screenshot:
            xpos numbers.button_1[0]
            ypos numbers.button_1[1]
            xsize numbers.button_1[2]
            ysize numbers.button_1[3]
        
        for i, item in enumerate(gamedata.getList()):
            text item['who'] ypos (300 + i*30) xpos 0
            text item['what'] ypos (300 + i*30) xpos 70

screen phone_display(who, what):
    # show topper
    zorder 20

    text who id "who"
    text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    # if not renpy.variant("small"):
    #     add SideImage() xalign 0.0 yalign 1.0