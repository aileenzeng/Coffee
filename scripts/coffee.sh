#!/bin/sh
array=() # array of inputs (to be read from input file)

# Reads in command line arguments for files
# First argument: name of java test file
# Second argument: name of java solution file

java_test="$1"
java_runner="$1Runner"
input_file="$2-input.txt"
expected_output="$2-eo.txt" 
output_file="output.txt"
diff_file="$2-diff.txt"

echo --- Executing coffee shell script ---
echo --- Getting test cases... ---
cd input-files/
counter=0
# fills array with input read in from input file
while read -r line
do
    #if [[ "$line" =~ ^$ ]]; then    #if line is empty
    if [[ $line == 'CASE' ]]
    then
        # echo "empty line"
        # echo 'NEW CASE'
        # echo $name
        # runs test case from array
        array[$counter]=$name
        let "counter++"
        name=""
        # run test on array
    else
        # echo $line
        name=$name"$line\n"
        # echo "Name read from file - $line"   
    fi
    array[$counter]=$name   # Adding in last test case
done < "$input_file"

echo --- Compiling java files... ---
cd ../java-test/$2/    # gets into correct folder directory with test files
javac *.java            # compiles all java files into class file
# java $java_runner       # runs the java class that runs everything else

> $output_file    # Clears output file

echo --- Running tests... ---
array=("${array[@]:1}")     # removing first element from array because problems
for input in "${array[@]}"
do  
    #pipes input from shell into java file 
    echo Running Test Case $count...    #prints out counter for array
    # echo "$input"                     # test cases
    echo "CASE $count" >> $output_file
    echo "$input" | java $java_runner $input>> $output_file
    let "count++"
done
rm *.class;
# mv $output_file ../../user-output-files/$output_file

echo --- Verifying Test Cases... ---
diff output.txt expected-output.txt >> $diff_file
echo --- Terminating coffee shell script ---