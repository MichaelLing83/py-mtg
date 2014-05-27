from typecheck import *
import os
import Constants
import atexit

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

class PyException(Exception):
    '''
    Customized Exception class.
    '''
    
    @typecheck
    def __init__(self, value: str) -> nothing:
        self.value = value
    
    def __str__(self) -> str:
        return repr(self.value)

@typecheck
def guarantee(true_condition: bool, message: str="") -> nothing:
    '''
    Raise an exception with message if true_condition is not met.
    
    @true_condition (bool): an boolean expression;
    @message (str): a message to add in case of true_condition is not true.
    
    @return (None)
    '''
    if not true_condition:
        raise PyException(message)

class PyLogger:
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
    OUTPUT_TO_CONSOLE = 0
    OUTPUT_TO_FILE = 1
    OUTPUT_OPTIONS = (OUTPUT_TO_CONSOLE, OUTPUT_TO_FILE)
    
    log_level = LOG_LEVEL_ERROR
    output_option = OUTPUT_TO_FILE
    log_file_name = Constants.LOG_FILE_NAME
    try:
        go_to_proj_root()
        log_file = open(log_file_name, 'w', encoding="utf8")
    except Exception as err:
        print(err)
        print("Cannot create log file, print to console instead.")
        output_option = OUTPUT_TO_CONSOLE
    
    @typecheck
    def __init__(self, *args, **kargs) -> nothing:
        '''
        This class should never be instantiated.
        '''
        raise PyException("PyLogger class should never be initialized!")
    
    @classmethod
    def cleanup(cls):
        try:
            log_file.close()
        except:
            pass
    
    @classmethod
    @typecheck
    def __print(cls, message: str) -> nothing:
        if output_option == OUTPUT_TO_CONSOLE:
            print(message)
        elif output_option == OUTPUT_TO_FILE:
            log_file.write(message + "\n")
    
    @classmethod
    @typecheck
    def debug(cls, message: str) -> nothing:
        if (self.log_level >= PyLogger.LOG_LEVEL_DEBUG):
            __print(message)
    
    @classmethod
    @typecheck
    def info(cls, message: str) -> nothing:
        if (self.log_level >= PyLogger.LOG_LEVEL_INFO):
            __print(message)
    
    @classmethod
    @typecheck
    def warning(cls, message: str) -> nothing:
        if (self.log_level >= PyLogger.LOG_LEVEL_WARNING):
            __print(message)
    
    @classmethod
    @typecheck
    def error(cls, message: str) -> nothing:
        if (self.log_level >= PyLogger.LOG_LEVEL_ERROR):
            __print(message)
    
    @classmethod
    @typecheck
    def critical(cls, message: str) -> nothing:
        if (self.log_level >= PyLogger.LOG_LEVEL_CRITICAL):
            __print(message)

atexit.register(PyLogger.cleanup)