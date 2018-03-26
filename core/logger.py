import logging
import time
import os

import sys


class TestLogger:
    def __init__(self, test_script_name):
        log_file__folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'outputs', 'log')
        if not os.path.exists(log_file__folder_path):
            os.makedirs(log_file__folder_path)
        time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        test_log_file_path = os.path.join(log_file__folder_path,str(test_script_name)+'_'+time_str+'.log')
        logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S',
                                handlers=[logging.FileHandler(test_log_file_path),logging.StreamHandler()]
                                )
