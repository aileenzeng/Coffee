# Coffee

Coffee is an autograder for basic Java programs built with Shell/Python 3. This is our team's hack for BrickHack4 (2018).
Currently, it only works for specific types of problems, but we are working to expand its capabilities!

## Getting Started

- Clone git repository
- Run the following commands to check that requirements are met

Run:
```
$ python3
```

And:
```
$ bash --version
```

### Requirements
- Python 3
- Bash (3.2 or higher)


### Installing
- Open command line, navigate to the project folder
- Navigate to the scripts folder
```
$ cd scripts/
```

Run coffee shell

```
$ ./coffee.sh
```

## Running the tests
Unfortunately, the test files are hard coded into the coffee.sh. Modifying which files coffee.sh and coffee-check runs needs to run different tests needs be done manually for now (we're working on improving this!). All the file variables are currently at the top of our shell/python files.

To modify which tests are run, make the following changes:

- coffee.sh
```
java_file="JAVA_FILE"               # Java file to be tested (no .java afterwards)
input_file="INPUT_FILE.txt"         # Text case inputs Java file reads in
output_file="OUTPUT_FILE.txt"       # Text file that logs Java console output for each case (same name as user_output)
```
- coffee-check.py
```
expected_output="EXPECTED_OUTPUT_FILE.txt"     # Text file containing expected solutions to test cases
user_output = "OUTPUT.txt"                     # Text containing logs from Java console input (same name as output_file)
```
- Make sure that each file is located in the appropriate directory as well!
```
java-files > Directory containing java files to be tested
input-files > Directory containing txt files with tests for a java-file
user-output-files > Directory containing txt files of java console logs
expected-output-files > Directory containing txt files of solutions to java tests
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Aileen Zeng** - *Initial work (Python/Bash)* - [PurpleBooth](https://github.com/PurpleBooth)
* **Frank Gonzalez Rojas** - *Initial work (HTML/CSS)* - [That1Handyman](https://github.com/That1Handyman)
* **Lizeth Rogel** - *Initial work (PHP)* - [xlzth](https://github.com/xlzth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* BrickHack and RIT for sponsoring a great hackathon
* RocHack for having amazing people :)

