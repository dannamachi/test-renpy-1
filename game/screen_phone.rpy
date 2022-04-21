screen magic_phone():
    style_prefix "phone"

    frame:
        id 'phone'

        imagemap:
            ground pinkscreen
            hotspot (0, 0, 200, 100):
                # child screenshot
                action Return()