import os

ALL_FORMATS = ("Classic", "Commander", "Extended", "Freeform", "Block", "Legacy", "Modern",
                "Prismatic", "Singleton 100", "Tribal Wars Legacy", "Tribal Wars Standard",
                "Vintage", "Standard")
MAIN_DECK_MIN_SIZE = 60
SIDE_BOARD_MAX_SIZE = 15
MTG_JSON_FILE_PATH = "./data/AllSets-x.json"
PROJECT_ROOT = "py-mtg"

cwd = os.getcwd()
if PROJECT_ROOT in cwd:
    # we're somewhere under our code structure, presumably
    while not cwd.endswith(PROJECT_ROOT):
        os.chdir("..")  # go to parent directory
        cwd = os.getcwd()
else:
    #TODO: cope with situations that program is started from outside of this project's directory
    raise ValueError("Must be started from py-mtg directory! It's started from: %s" % cwd)