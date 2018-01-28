""" this program is called by the coffee shell script to determine
    whether output/expected output files are the same. """

import os
import sys

# expected_output = "expected-output.txt
expected_output = sys.argv[1]
user_output = "output.txt"

class Answer:
    """ stores boolean - whether a case was passed and a response message"""
    def __init__(self, passed, response):
        self.passed = passed
        self.response = response

def main():
    """ tests whether two txt files are the same """
    compare_files(expected_output, user_output)

    # Checks to see that all answers are entered in the answer_list correctly
    # for answer in answer_list:
    #     print(str(answer.passed))
    #     print(answer.response)

def compare_files(expected_file, out_file):
    """ takes two txt files, sees if contents are identical """
    answers = [] # creates an empty list of answers (booleans, temporarily)

    # Gets access to the correct directories
    # script_path =  # i.e. /path/to/dir/foobar.py
    script_dir = os.path.split(os.path.abspath(__file__))[0] #i.e. /path/to/dir/
    rel_ex_path = "expected-output-files/" + expected_file
    rel_out_path = "user-output-files/" + out_file
    abs_ex_path = os.path.join(script_dir, rel_ex_path)
    abs_out_path = os.path.join(script_dir, rel_out_path)

    expected_text = open(abs_ex_path)
    out_text = open(abs_out_path)

    case_count = 0
    expected_line = expected_text.readline()
    out_line = out_text.readline()

    exp_arr = []
    out_arr = []
    while len(expected_line) != 0:
        # out_line = out_text.readline()
        # print("Current line: " + expected_line)
        if "--CASE" in expected_line: # splits output file into cases
            # print("New case starting! Line is: " + expected_line)
            expected_line = expected_text.readline().rstrip()
            out_line = out_text.readline().rstrip()
            passed = (expected_line == out_line)
            # print("First expected line: " + expected_line)
            count = 0
            exp_arr.clear()
            out_arr.clear()
            # print("Condition 1: " + str("--CASE" not in expected_line))
            # print("Condition 2: " + str(len(expected_line) != 0))
            while "--CASE" not in expected_line and len(expected_line) != 0:
                # print("Expected line is: " + expected_line)
                # print("Condition 1: " + str("--CASE" not in expected_line))
                # print("Condition 2: " + str(len(expected_line) != 0))
                # print(len(expected_line) == 0)
                # print("Line length: " + str(len(expected_line)))
                # print("1. Expected line: " + expected_line)
                exp_arr.append(expected_line)
                out_arr.append(out_line)
                expected_line = expected_text.readline().rstrip()
                out_line = out_text.readline().rstrip()
                # print("2. Expected line: " + expected_line)
                # For testing purposes
                count += 1
                if count > 4:
                    print("Break forced")
                    break
                passed = (expected_line == out_line)
            # print("After while loop: " + expected_line)
            response = ""
            if passed:
                response = ("* Test case passed!")
            else:
                response = ("* Test case failed!")
            print("***")
            print("* CASE " + str(case_count))
            print(response)
            print("*\n* Your output: ")
            print_array(out_arr)
            print("*\n* Expected output: ")
            print_array(exp_arr)
            print("***")
            print()
            answers.append(Answer(passed, response))
            case_count += 1
    return answers

def print_array(array):
    """ Prints out contents of an array """
    for line in array:
        print("* " + line)
if __name__ == "__main__":
    main()
