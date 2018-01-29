#!/bin/sh
array=() # array of inputs (to be read from input file)

# Reads in command line arguments for files
java_file="$1"
input_file="$1-input.txt"
output_file="output.txt"
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
cd ../java-files
javac $1.java    # compiles all java files into class files
> $output_file    # Clears output file

count=0
for input in "${array[@]}"
do
    #pipes input from shell into java file 
    echo "--CASE $count" >> $output_file
    echo "$input" | java $java_file >> $output_file    
    echo Test Case $count completed...    #prints out counter for array
    let "count++"
done

mv $output_file ../user-output-files/$output_file

echo --- Executing python script ---
cd ../
python3 coffee-check.py $expected_output
echo --- Terminating python script 
echo --- Terminating coffee shell script ---
