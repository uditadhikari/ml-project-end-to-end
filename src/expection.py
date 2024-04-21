import sys

def error_message_details(error, error_details : sys):
    _,_,execp_tb = error_details.exc_info()
    file_name = execp_tb.tb_frame.f_code.co_filename
    line_number = execp_tb.tb_lineno
    error_msg = "Error in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        line_number,
        str(error)
    )
    return error_msg


class CustomExecptionHandler(Exception):
    def __init__(self, error_msg, error_details):
        super().__init__(error_msg)
        self.error_msg = error_message_details(error_msg, error_details)
        self.error_details = error_details

    def __str__(self):
        return self.error_msg
