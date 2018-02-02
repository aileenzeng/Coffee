#!/bin/sh
array=() # array of inputs (to be read from input file)

# Reads in command line arguments for files
# First argument: name of java test file
# Second argument: name of java solution file
java_test="$1"
java_master="$2"
input_file="$2-input.txt"
output_file="output.txt"
expected_output="$2-eo.txt" 

echo --- Executing coffee shell script ---
echo --- Getting test cases... ---
cd input-files/
counter=0
# fills array with input read in from input file
while read -r line
do
    if [[ "$line" =~ ^$ ]]; then
        # echo "empty line"
        echo Adding:
        echo $name
        # runs test case from array
        array[$counter]=$name
        let "counter++"
        name=""
        # run test on array
    else
        name=$name"$line\n"
        # echo "Name read from file - $line"   
    fi
    array[$counter]=$name   # Adding in last test case
done < "$input_file"
echo --- Compiling java files... ---
cd ../java-test/$java_master/    # gets into correct folder directory with test files
javac $java_test.java    # compiles java file into class file
> $output_file    # Clears output file

count=0
for input in "${array[@]}"
do
    #pipes input from shell into java file 
    echo "--CASE $count" >> $output_file
    echo "$input" | java $java_test >> $output_file    
    echo Test Case $count completed...    #prints out counter for array
    let "count++"
done
mv $output_file ../../user-output-files/$output_file

echo --- Executing python script ---
cd ../../
python3 coffee-check.py $expected_output
echo --- Terminating python script 
echo --- Terminating coffee shell script ---
