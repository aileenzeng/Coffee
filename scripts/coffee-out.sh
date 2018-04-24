#!/bin/sh
# This is like... a weak coffee :)
# Does not compare expected output - just runs test cases

array=() # array of inputs (to be read from input file)

# Reads in command line arguments for files
# First argument: name of java test file
# Second argument: name of problem to be tested against
java_test="$1"
question="$2"
name="$3"
input_file="$2-input.txt"
output_file="$1-output.txt"

echo --- Executing coffee shell script ---
echo --- Getting test cases... ---
cd temp/test-files/$question

counter=0
# fills array with input read in from input file
while read -r line
do
if [[ "$line" =~ ^$ ]]; then #if line is empty
# echo "empty line"
# echo Adding:
# echo $name
# runs test case from array
array[$counter]=$name
let "counter++"
name=""
# run test on array
else
name=$name"$line\n"
# echo "Name read from file - $line"
fi
array[$counter]=$name # Adding in last test case
done < "$input_file"
echo --- Compiling java files... ---

javac $java_test.java # compiles java file into class file
# > $output_file # Clears output file

count=0
# "$name" >> $output_file
for input in "${array[@]}"
do
    #pipes input from shell into java file
    echo "--CASE $count" >> $output_file
    echo "In: $input" >> $output_file
    echo "Out: $input" | java $java_test >> $output_file
    echo Test Case $count completed... #prints out counter for array
    let "count++"
done
mv $output_file ../../output-files/$2/$output_file