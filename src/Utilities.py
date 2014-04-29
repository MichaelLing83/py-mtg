from typecheck import *
import os
import Constants

def go_to_proj_root():
    cwd = os.getcwd()
    if Constants.PROJECT_ROOT in cwd:
        # we're somewhere under our code structure, presumably
        while not cwd.endswith(Constants.PROJECT_ROOT):
            os.chdir("..")  # go to parent directory
            cwd = os.getcwd()
    else:
        #TODO: cope with situations that program is started from outside of this project's directory
        raise ValueError("Must be started from py-mtg directory! It's started from: %s" % cwd)

class MtgException(Exception):
    '''
    Customized Exception class.
    '''
    
    @typecheck
    def __init__(self, value: str) -> nothing:
        self.value = value
    
    def __str__(self) -> str:
        return repr(self.value)

@typecheck
def garantee(true_condition: bool, message: str) -> nothing:
    '''
    Raise an exception with message if true_condition is not met.
    
    @true_condition (bool): an boolean expression;
    @message (str): a message to add in case of true_condition is not true.
    
    @return (None)
    '''
    if not true_condition:
        raise MtgException(message)

class MtgLogger:
    '''
    A class providing logging support.
    '''
    LOG_LEVEL_DEBUG = 5 # Detailed information, typically of interest only when diagnosing problems.
    LOG_LEVEL_INFO = 4  # Confirmation that things are working as expected.
    LOG_LEVEL_WARNING = 3   # An indication that something unexpected happened, or indicative of
                            # some problem in the near future (e.g. ‘disk space low’). The software 
                            # is still working as expected.
    LOG_LEVEL_ERROR = 2 # Due to a more serious problem, the software has not been able to perform
                        # some function.
    LOG_LEVEL_CRITICAL = 1  # A serious error, indicating that the program itself may be unable to
                            # continue running.
    ALL_LOG_LEVELS = (LOG_LEVEL_DEBUG, LOG_LEVEL_INFO, LOG_LEVEL_WARNING, LOG_LEVEL_ERROR, LOG_LEVEL_CRITICAL)
    
    @typecheck
    def __init__(self, log_level: one_of(ALL_LOG_LEVELS)) -> nothing:
        '''
        Higher logging level enabled more traces.
        
        @log_level (MtgLogger.LOG_LEVEL_*): set logging level of this MtgLogger object.
        
        @return (None)
        '''
        self.log_level = log_level
    
    @typecheck
    def debug(message: str) -> nothing:
        if (self.log_level >= MtgLogger.LOG_LEVEL_DEBUG):
            print(message)
    
    @typecheck
    def info(message: str) -> nothing:
        if (self.log_level >= MtgLogger.LOG_LEVEL_INFO):
            print(message)
    
    @typecheck
    def warning(message: str) -> nothing:
        if (self.log_level >= MtgLogger.LOG_LEVEL_WARNING):
            print(message)
    
    @typecheck
    def error(message: str) -> nothing:
        if (self.log_level >= MtgLogger.LOG_LEVEL_ERROR):
            print(message)
    
    @typecheck
    def critical(message: str) -> nothing:
        if (self.log_level >= MtgLogger.LOG_LEVEL_CRITICAL):
            print(message)