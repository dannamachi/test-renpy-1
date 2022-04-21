screen magic_phone():
    style_prefix "phone"

    frame:
        id 'phone'

        imagemap:
            ground pinkscreen
            hotspot (0, 0, 200, 100):
                action Return()

        add screenshot:
            xpos 0
            ypos 0
            xsize 200
            ysize 100