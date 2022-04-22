################################################################################
## Define all constants
################################################################################

init -5 python:
    tables = {}
    
    tables.save_custom_1 = {}
    tables.save_custom_1.col = 4
    tables.save_custom_1.row = 3
    tables.save_custom_1.spacing = 8

    numbers = {}
    
    numbers.slot_prefix = 100
    
    numbers.screen_width = 1280
    numbers.screen_height = 720

    numbers.phone_width = 350
    numbers.phone_height = 600

    numbers.button_1 = (0, 0, 200, 100)

    def togglePhoneDisplay():
        if (renpy.get_screen('magic_phone')): # name
            renpy.hide_screen('phone_case') # tag
        else:
            renpy.show_screen('magic_phone') # name

    def run_autosave():
        renpy.save(str(numbers.slot_prefix) + "-1", "")

    def isThisScreen(name):
        if renpy.get_screen(name):
            return True
        return False
