#!/bin/sh
array=("hello" "123" "goodbye") # inputs
java_file="ScannerTest"
output_file="output.txt"

echo --- Executing coffee shell script ---
echo --- Compiling java files... ---
javac *.java # compiles all java files into class files
> output.txt     # Clears output file

for count in {0..2}
do
    # TO-DO: store java files in a different directory
    #pipes input from shell into java file 
    echo "--CASE $count" >> $output_file
    echo "${array[$count]}" | java $java_file >> $output_file    
    echo Test Case $count completed...    #prints out counter for array
done
echo --- Executing python script ---
python3 coffee-check.py
echo --- Terminating python script 

echo --- Terminating coffee shell script ---
