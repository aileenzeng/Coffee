""" this program is called by the coffee shell script to determine
    whether output/expected output files are the same. """
class Answer:
    """ stores boolean - whether a case was passed and a response message"""
    def __init__(self, passed, response):
        self.passed = passed
        self.response = response

    def get_passed(self):
        """ gets boolean """
        return self.passed

    def get_response(self):
        """ gets string """
        return self.response

def main():
    """ tests whether two txt files are the same """
    answer_list = compare_files("expected-output.txt", "output.txt")
    # TODO: print out all parts of answer from answer_list to check that it's working properly
    

def compare_files(expected_file, out_file):
    """ takes two txt files, sees if contents are identical """
    answers = [] # creates an empty list of answers (booleans, temporarily)
    expected_text = open(expected_file, "r")
    out_text = open(out_file, "r")

    case_count = 0

    for expected_line in expected_text:
        out_line = out_text.readline()
        # print("In: " + expected_file + " Out: " + out_line)
        if "--CASE" in expected_line: # splits output file into cases
            # print("Hooray! Case: " + str(case_count))
            # TODO: Separate cases by --CASE string for multi-line outputs
            expected_line = expected_text.readline()
            #print(expected_line)

            out_line = out_text.readline()
            # print("In: " + expected_line + "Out: " + out_line)
            answers.append(expected_line == out_line)
            response = ""
            if expected_line == out_line:
                response = "Test case passed! \nOutput: " + expected_line
            else:
                response = "Test case failed! \nExpected output: " + expected_line + "\nActual output: " + out_line

            answers.append(Answer(expected_line == out_line, response))
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
