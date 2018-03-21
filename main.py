import argparse
import logging
import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from core import logger

#Parse argument
from core.logger import TestLogger

parser = argparse.ArgumentParser(
        description="Welcome to use Selenium to help you do UI automation test!"
    )

parser.add_argument(
    'test_script_path', help="Please add test script path here, it's mandatory!", type=str
)
parser.add_argument(
    '-b','--browser', help="Please select blower you want to run your test scripts", type=str, default='chrome'
)

args = parser.parse_args()

test_script_name = args.test_script_path
browser_name = args.browser
#Create log file
TestLogger(test_script_name)


if __name__ == '__main__':
    #discover test cases in test script path
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test/' + str(test_script_name))
    discover = unittest.defaultTestLoader.discover(script_dir, pattern='test_*.py')
    logging.info("Discover test cases finished! {num_of_tc} test cases found!".format(num_of_tc=discover.countTestCases()))

    #Prepare for test report
    test_report_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs/reports/')
    if not os.path.exists(test_report_folder_path):
        os.makedirs(test_report_folder_path)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    test_report_file_path = str(test_script_name) + time_str
    kwargs = {
        "output": test_report_folder_path,
        "report_name": test_report_file_path
    }
    #Run test and generate test report
    runner = HTMLTestRunner(**kwargs)
    runner.run(discover)