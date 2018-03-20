import argparse
import unittest
import os

import time
from pyunitreport import HTMLTestRunner

#Parse argument
parser = argparse.ArgumentParser(
    description="Welcome to use Selenium to help you do UI automation test!"
)

parser.add_argument(
    'test_script_path', help="Please add test script path here, it's mandatory!", type=str
)

parser.add_argument(
    '--broswer'
)
args = parser.parse_args()

test_script_name = args.test_script_path

#discover test cases in test script path
script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test/' + str(test_script_name))
discover = unittest.defaultTestLoader.discover(script_dir, pattern='test_*.py')

#Prepare for test report
test_report_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests/reports/')
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