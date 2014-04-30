'''
Known bugs:
    1. On Windows, please save deck file as "UTF-8 without BOM", otherwise you get problem in
        console like: ValueError: invalid literal for int() with base 10: '\ufeff'
        This is caused by BOM character.
'''

import cmd
import os
import Constants
from CardCondition import CardCondition
from MtgDataBase import MtgDataBase
from Utilities import MtgException

class pyMtg(cmd.Cmd):
    '''
    Command Line Interface for MTG game.
    '''
    
    prompt = "Magic$ "
    intro = "Magic the Gathering single-person-game, card search, deck analysis at your console."
    doc_header = "Available commands"
    undoc_header = "Available commands"
    misc_header = 'misc_header'
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.last_cli_output = None
        self.last_search_result = None
        self.last_search_result_index = 0
    
    def do_search(self, line):
        '''
        Search cards from MTG data base by given condition.
        
        Usage:
        
        '''
        # build CardCondition
        try:
            card_condition = CardCondition()
            for one_condition in line.split(';'):
                one_condition = one_condition.split()
                if len(one_condition) == 0:
                    continue
                if len(one_condition) < 3:
                    raise MtgException("Illegal condition: %s" % ' '.join(one_condition))
                key = one_condition[0]
                if one_condition[1] == 'not':
                    op = ' '.join(one_condition[1:3])
                    value_start_index = 3
                else:
                    op = one_condition[1]
                    value_start_index = 2
                value = ' '.join(one_condition[value_start_index:])
                card_condition.add(key, op, value)
        except Exception as err:
            print(err)
            return
        # search
        try:
            self.last_search_result = MtgDataBase.get_cards(card_condition)
            self.last_search_result_index = 0
            print("Found %d matching cards." % len(self.last_search_result))
        except Exception as err:
            print(err)
            return
    
    def do_version(self, line):
        '''
        Print version of the software.
        '''
        print(Constants.VERSION)
    
    def do_EOF(self, line):
        '''
        End of program.
        '''
        return True
    
    def do_shell(self, line):
        '''
        Run a shell command.
        '''
        try:
            output = os.popen(line).read()
            print(output)
            self.last_cli_output = output
        except:
            print("Shell command failed: %s" % line)

if __name__ == '__main__':
    pyMtg().cmdloop()