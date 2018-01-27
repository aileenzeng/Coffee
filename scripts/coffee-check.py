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

    for line in expected_text:
        if "--CASE" in line:
            print("hooray!")

if __name__ == "__main__":
    main()
