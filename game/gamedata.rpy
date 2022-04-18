################################################################################
## Define game object structure
################################################################################

init -10 python:

    class GameData:
        def __init__(self):
            self.someList = [
                'dear god',
                'apple',
                'mint tea'
            ]
            self.anotherList = [
                {
                    'name'        : 'Mochi',
                    'age'         : 10,
                    'love_power'  : -1
                },
                {
                    'name'        : 'Kacchi',
                    'age'         : 20,
                    'love_power'  : 100
                }
            ]
            self.name = 'Hahahah'