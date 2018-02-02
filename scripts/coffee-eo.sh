#!/bin/sh
# This script generates an expected output file (given a list of inputs)
# Assumes that the java file that is submitted is correct

array=() # array of inputs (to be read from input file)
java_master="$1"
input_file="$1-input.txt"
expected_output="$1-eo.txt" 

echo --- Executing coffee shell script ---
echo --- Getting test cases... ---
cd input-files/
counter=0
# fills array with input read in from input file
while read -r line
do
    if [[ "$line" =~ ^$ ]]; then
        # echo "empty line"
        # echo Adding $name
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
cd ../java-master
javac $1.java    # compiles all java files into class files
> $expected_output    # Clears expected output file

count=0
for input in "${array[@]}"
do
    #pipes input from shell into java file 
    echo "--CASE $count" >> $expected_output
    echo "$input" | java $java_master >> $expected_output    
    echo Test Case $count created...    #prints out counter for array
    let "count++"
done

mv $expected_output ../expected-output-files/$expected_output
