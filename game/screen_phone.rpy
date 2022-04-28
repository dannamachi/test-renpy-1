screen magic_phone():
    style_prefix "phone"

    tag phone_case

    # show top
    zorder 10

    predict False

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
            yadj = ui.adjustment()

        viewport:
            yadjustment yadj
            python:
                if yadj.value == yadj.range:
                    yadj.value = float('inf')
            # cols 1 (for vpgrid)
            yinitial 1.0
            # ysize 2000

            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True

            side_yfill True

            # style_prefix "history"
            $ lines = gamedata.getChatLines()

            vbox: # for viewport
                for i, item in enumerate(lines):

                    window:
                        style 'chat_window'
                        if i + 1 == len(lines):
                            at transform:
                                alpha 0.0
                                linear 0.3 alpha 1.0

                        ## This lays things out properly if history_height is None.
                        has fixed:
                            yfit True

                        if item['who']:
                            if i > 0 and lines[i-1]['who'] == item['who']:
                                $ hasName = False
                            else:
                                $ hasName = True
                                label item['who'].name:
                                    style "chat_name"
                                    substitute False

                        text item['what']:
                            if hasName:
                                style "chat_text"
                            else:
                                style "chat_text2"
                            substitute False

            if gamedata.getChatCount() == 0: # mbe change this to reduce iter time on large chat list ?
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
