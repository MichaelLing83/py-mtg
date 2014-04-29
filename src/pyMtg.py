'''
Known bugs:
    1. On Windows, please save deck file as "UTF-8 without BOM", otherwise you get problem in
        console like: ValueError: invalid literal for int() with base 10: '\ufeff'
        This is caused by BOM character.
'''