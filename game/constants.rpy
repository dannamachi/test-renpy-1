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

    def run_autosave():
        renpy.save(str(numbers.slot_prefix) + "-1", "")

    def isThisScreen(name):
        if renpy.get_screen(name):
            return True
        return False
