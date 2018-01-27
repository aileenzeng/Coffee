""" this program is called by the coffee shell script to determine
    whether output/expected output files are the same. """
class Answer: 
    def __init__(self, passed, response):
        self.passed = False
        self.response = "no"

def main():
    """ tests whether two txt files are the same """
    print("hello")
    compare_files("expected-output.txt", "output.txt")

def compare_files(expected_file, out_file):
    """ takes two txt files, sees if contents are identical """
    print("comparing files")
    answers = [] # creates an empty list of answers
    expected_text = open(expected_file, "r")
    out_text = open(out_file, "r")

    case_count = 0



    for expected_line in expected_text:
        out_line = out_text.readline()
        print("In: " + expected_file + " Out: " + out_line)
        if "--CASE" in expected_line: # splits output file into cases
            print("Hooray! Case: " + str(case_count))
            # TODO: Separate cases by --CASE string for multi-line outputs
            expected_line = expected_text.readline()
            #print(expected_line)

            out_line = out_text.readline()
            print("In: " + expected_line + "Out: " + out_line)
            print(expected_line == out_line)
            """
            # Having major iteration troubles
            while "--CASE" not in expected_line:
                print(expected_line)
                expected_line = expected_text.readline() # new line
            """
            case_count += 1


if __name__ == "__main__":
    main()
