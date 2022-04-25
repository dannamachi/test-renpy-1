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

    def divide_into_lines(text_string, max_char):
        # divide into sections by \n
        sections = text_string.split('\n')
        lines = []
        for section in sections:
            # get all words in section
            words = section.strip().split(' ')
            while True:
                segment_string = ""
                # add word to segment string until reached max_char
                while True:
                    # check still have word left
                    if len(words) == 0:
                        break
                    if len(segment_string) + len(words[0]) > max_char:
                        break
                    segment_string += words.pop(0) + " "
                lines.append(segment_string)
                # check still have word left
                if len(words) == 0:
                    break
                # TO DO: break up if there is a string > max_char
        return lines
