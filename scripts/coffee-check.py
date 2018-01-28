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
    answer_list = compare_files(expected_output, user_output)

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

    for expected_line in expected_text:
        out_line = out_text.readline()
        if "--CASE" in expected_line: # splits output file into cases
            # print("Hooray! Case: " + str(case_count))
            expected_line = expected_text.readline().rstrip()
            out_line = out_text.readline().rstrip()
            passed = (expected_line == out_line)
            while ("--CASE" not in expected_line or expected_line == ".") and passed:
                expected_line = expected_text.readline().rstrip()
                out_line = out_text.readline().rstrip()
                passed = (expected_line == out_line)
                # print("Next line is: " + expected_line)
                if "--CASE" not in expected_line or expected_line == ".":
                    break #yikes! don't like this, but it works?
            response = ""
            if passed:
                response = ("* Test case passed! \n*\n* Expected output:\n* " + expected_line
                            + "\n* \n* Actual Output:\n* " + out_line)
            else:
                response = ("* Test case failed! \n*\n* Expected output:\n* " + expected_line
                            + "\n* \n* Actual output:\n* " + out_line)
            print("***")
            print("* CASE " + str(case_count))
            print(response)
            print("***")
            print()
            answers.append(Answer(passed, response))

            """
            # Having major iteration troubles
            while "--CASE" not in expected_line:
                print(expected_line)
                expected_line = expected_text.readline() # new line
            """
            case_count += 1
    return answers


if __name__ == "__main__":
    main()
