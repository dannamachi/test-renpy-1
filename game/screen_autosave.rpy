screen save_custom_1():

    # set filepage when hidden
    on "hide" action FilePage(1)

    ## This ensures that any other menu screen is replaced.
    tag menu

    add blackscreen

    ## The grid of file slots.
    grid tables.save_custom_1.col tables.save_custom_1.row:
        style_prefix "slot"

        xalign 0.5
        yalign 0.5

        spacing tables.save_custom_1.spacing

        for i in range(tables.save_custom_1.col * tables.save_custom_1.row):

            button:
                action FileLoad(i + 1, page=numbers.slot_prefix)

                has vbox

                add screenshot

                text FileTime(i + 1, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot"), page=numbers.slot_prefix):
                    style "slot_time_text"

                text FileSaveName(i + 1, page=numbers.slot_prefix):
                    style "slot_name_text"

                # key "save_delete" action FileDelete(slot) (fn + delete on mac)

    textbutton _("Return"):
        style "return_button"

        action Show("main_menu")