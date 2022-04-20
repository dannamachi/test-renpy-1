screen pizza():

    # background
    add blackscreen

    fixed:
        xsize 500
        ysize 900
        xalign 1.3
        yalign 0.5

        style_prefix "pizza"

        textbutton _("Start") action Start() at pizza_button_1
        textbutton _("Load") action [ShowMenu("load"), FilePage(1)] selected isThisScreen('load') at pizza_button_2
        textbutton _("Preferences") action ShowMenu("preferences") at pizza_button_3
        textbutton "Magic Show" action Show("minigame") at pizza_button_4
        textbutton _("Quit") action Quit(confirm=not main_menu) at pizza_button_5