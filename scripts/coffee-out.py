# TODO: Open up the diff file, and read contents
# Afterwards, write to a new file containing the differences
# Bonus: make it pretty
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# print("Input file: " + input_file)
# print("Output file: " + output_file)

class TestCase:
    def __init__(self, line, ans, expected):
        self.__line = line
        self.__ans = ans
        self.__expected = expected
    
    def getLine(self):
        return self.__line
    
    def getAns(self):
        return self.__ans
    
    def getExpected(self):
        return self.__expected

cases = []
# case = TestCase('6c6', '1', '2')
# print('Line: ' + case.getLine())
# print('Answer: ' + case.getAns())
# print('Expected: ' + case.getExpected())
with open(input_file) as f:
    for line in f:
        # print(line)
        testLine = f.readLine()
        # ans = f.readLine()
        # f.readLine()
        # expected = f.readLine()
        print(testLine)
        # print(ans)
        # print(expected)
