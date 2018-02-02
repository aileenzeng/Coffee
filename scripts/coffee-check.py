""" this program is called by the coffee shell script to determine
    whether output/expected output files are the same. """

import os
import sys

# expected_output = "expected-output.txt
expected_output = sys.argv[1]   # name of expected output file
user_output = "output.txt"
"""
class Answer:
    def __init__(self, passed, response):
        self.passed = passed
        self.response = response
"""

def main():
    """ tests whether two txt files are the same """
    compare_files(expected_output, user_output)

def compare_files(expected_file, out_file):
    """ takes two txt files, sees if contents are identical """
    answers = [] # creates an empty list of answers (booleans, temporarily)

    script_dir = os.path.split(os.path.abspath(__file__))[0] #i.e. /path/to/dir/
    rel_ex_path = "expected-output-files/" + expected_file
    rel_out_path = "user-output-files/" + out_file
    abs_ex_path = os.path.join(script_dir, rel_ex_path)
    abs_out_path = os.path.join(script_dir, rel_out_path)

    expected_text = open(abs_ex_path)
    out_text = open(abs_out_path)

    correct = 0
    case_count = 0
    expected_line = expected_text.readline()
    out_line = out_text.readline()

    exp_arr = []
    out_arr = []
    while len(expected_line) != 0:
        if "--CASE" in expected_line: # splits output file into cases
            # print("New case starting! Line is: " + expected_line)
            expected_line = expected_text.readline().rstrip()
            out_line = out_text.readline().rstrip()
            passed = (expected_line == out_line)

            exp_arr.clear()
            out_arr.clear()
            while "--CASE" not in expected_line and len(expected_line) != 0:
                exp_arr.append(expected_line)
                out_arr.append(out_line)
                expected_line = expected_text.readline().rstrip()
                out_line = out_text.readline().rstrip()
                passed = (expected_line == out_line)
            response = ""
            if passed:
                response = ("* Test case passed!")
                correct += 1
            else:
                response = ("* Test case failed!")
            print_results(case_count, response, out_arr, exp_arr)
            case_count += 1
    print ("(" + str(correct) + "/" + str(case_count) + ") test cases passed!")

def print_array(array):
    """ Prints out contents of an array """
    for line in array:
        print("* " + line)

def print_results(case_count, response, out_arr, exp_arr):
    """ Prints results from test cases - including user output/expected output"""
    print("***")
    print("* CASE " + str(case_count))
    print(response)
    print("*\n* Your output: ")
    print_array(out_arr)
    print("*\n* Expected output: ")
    print_array(exp_arr)
    print("***")
    print()

if __name__ == "__main__":
    main()
