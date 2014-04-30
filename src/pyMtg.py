'''
Known bugs:
    1. On Windows, please save deck file as "UTF-8 without BOM", otherwise you get problem in
        console like: ValueError: invalid literal for int() with base 10: '\ufeff'
        This is caused by BOM character.
'''

import cmd
import os
import Constants

class pyMtg(cmd.Cmd):
    '''
    Command Line Interface for MTG game.
    '''
    
    prompt = "Magic$ "
    intro = "Magic the Gathering single-person-game, card search, deck analysis at your console."
    doc_header = "Available commands"
    undoc_header = "Available commands"
    misc_header = 'misc_header'
    
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
            self.last_output = output
        except:
            print("Shell command failed: %s" % line)

if __name__ == '__main__':
    pyMtg().cmdloop()