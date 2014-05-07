'''
Known bugs:
    1. On Windows, please save deck file as "UTF-8 without BOM", otherwise you get problem in
        console like: ValueError: invalid literal for int() with base 10: '\ufeff'
        This is caused by BOM character.
'''

import cmd
import os
import Constants
from MtgDataBase import MtgDataBase
from CardCondition import CardCondition
from Utilities import MtgException
from Utilities import go_to_proj_root
from Deck import Deck

class pyMtg(cmd.Cmd):
    '''
    Command Line Interface for MTG game.
    
    Note: for verification purpose, use onecmd() method and last_cli_output attribute to get output of
    last command.
    '''
    
    prompt = "Magic$ "
    intro = "Magic the Gathering single-person-game, card search, deck analysis at your console."
    doc_header = "Available commands"
    undoc_header = "Available commands"
    misc_header = 'misc_header'
    
    def __init__(self):
        go_to_proj_root()
        cmd.Cmd.__init__(self)
        self.last_cli_output = None
        self.last_search_result = None
        self.last_search_result_index = 0
        self.seperator_line = "="*20
        self.deck = None
    
    def default(self, line):
        '''
        Default callback when a command is not recognized.
        '''
        self.last_cli_output = "***Unknown syntax: %s" % line
        print(self.last_cli_output)
    
    def do_pcard(self, line):
        '''
        Print a Card from search result. Note that you need to do a search first,
        otherwise nothing will be printed.
        
        Usage:
            pcard [option]
            
            if no option is given, then current card is printed;
            if "n" is given, then move to next card and print it;
            if "p" is given, then move to previous card and print it;
        '''
        line = line.strip()
        if line and (line not in ('n', 'p')):
            self.onecmd("help pcard")
            return
        if self.last_search_result:
            num_of_results = len(self.last_search_result)
            self.last_search_result_index = {
                '': lambda: self.last_search_result_index,
                'n': lambda: (self.last_search_result_index+1)%num_of_results,
                'p': lambda: (self.last_search_result_index-1)%num_of_results,
            }[line]()
            print(self.seperator_line,
                " %d/%d "%(self.last_search_result_index+1,num_of_results),
                self.seperator_line)
            print(self.last_search_result[self.last_search_result_index].to_str())
            print(self.seperator_line,
                " %d/%d "%(self.last_search_result_index+1,num_of_results),
                self.seperator_line)

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
        self.last_cli_output = Constants.VERSION
    
    def do_EOF(self, line):
        '''
        End of program.
        '''
        self.last_cli_output = "EOF"
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
    
    def do_deck_load(self, line):
        '''
        Load a deck.
        '''
        file_name = line.strip()
        try:
            self.deck = Deck(file_name="./data/%s"%file_name)
        except:
            self.last_cli_output = "Loading failed for deck: %s" % file_name
            print(self.last_cli_output)
        else:
            self.last_cli_output = "Deck \"%s\" is loaded" % file_name
            print(self.last_cli_output)

if __name__ == '__main__':
    pyMtg().cmdloop()