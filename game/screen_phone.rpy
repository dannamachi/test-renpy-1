screen magic_phone():
    style_prefix "phone"

    tag phone_case

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

        python:
            linesList = []
            for item in gamedata.getList():
                lineList = divide_into_lines(item['what'], 25)
                for segment in lineList:
                    linesList.append({
                        'who'  : item['who'],
                        'what' : segment
                    })

        vpgrid:
            cols 1
            yinitial 0.0

            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True

            side_yfill True

            # style_prefix "history"

            for item in linesList:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if item['who']:

                        label item['who'].name:
                            style "history_name"
                            substitute False

                    text item['what']:
                        substitute False

            if len(linesList) == 0:
                label 'No text message, say something ?'
        
        # for i, item in enumerate(linesList):
        #     text item['who'].name ypos (100 + i*30) xpos 0
        #     text item['what'] ypos (100 + i*30) xpos 70

screen phone_display(who, what):
    # show topper
    zorder 20

    fixed:
        if gamedata.isHidingPhoneDisplay():
            at invisible
        text who id "who"
        text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    # if not renpy.variant("small"):
    #     add SideImage() xalign 0.0 yalign 1.0

screen phone_icon():
    button:
        style 'icon_phone'
        background pinkscreen
        action Function(togglePhoneDisplay)
