import sys
import os
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # carry 3 values, 3rd imp -> info of on which file, which line
    file_name = exc_tb.tb_frame.f_code.co_filename  # Getting where filename is stored(in documentation)
    error_message = (f'Error encountered under python Script [{file_name}] on line number [{exc_tb.tb_lineno}] '
                     f'with error message[{str(error)}]')
    return error_message


class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Inheriting init function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


# CHECKING PROGRAM


if __name__ == '__main__':
    try:
        a = 1 / 0
    except Exception as e:
        logging.info('Divide by Zero Error')  # initially won't log as the logger.py has to be called above as a package
        raise CustomException(e, sys)

    
		