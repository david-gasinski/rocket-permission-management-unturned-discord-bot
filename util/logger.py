import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename=self.log_file, level=logging.INFO)
        self.logger.info("APPLICATION START")

    def log_request(self, request_origin, method_name, status):
        if status:
            self.logger.info(f'HTTP 200 - {request_origin} requested {method_name}.')  
        else:
            self.logger.error(f'HTTP 500 - {request_origin} requested {method_name}. The process succeded with status False')  

    def get_logger(self):
        return self.logger
    