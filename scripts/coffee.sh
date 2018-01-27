#!/bin/sh
array=("hello" "123" "goodbye")

echo --- Executing coffee shell script ---

testString="$(java HelloWorld)"
echo $testString

for count in {0..2}
do
    echo Iteration $count    #prints out counter for array
    echo "${array[$count]}" | java ScannerTest > output.txt    #pipes input from shell into java file
    echo 
done
echo --- Terminating coffee shell script ---
