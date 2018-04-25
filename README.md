# Coffee

Coffee is an autograder for basic Java programs built with Shell/Python 3. This is our team's hack for BrickHack4 (2018).

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
- Open command line, navigate to the project directory
- Navigate to the scripts directory
```
$ cd scripts/
```

Run coffee shell 

```
$ ./coffee.sh [java test file name] [java problem name]
```

## Running the tests
Run the coffee shell in command line. Coffee takes in two commands: the name of the file you want to check and the name of the file you want to test your file against.

Any differences in input/expected output will be indicated under the 'Verifying Test Cases' line. If it is empty, all test cases passed!

Sample run (all test cases passed)
```
$ ./coffee.sh Problem1Demo1 Problem1
```

Sample run (two test cases failed)
```
$ ./coffee.sh Problem1Demo2 Problem1
```

To create tests for a Java program, edit the input-files and expected-output files corresponding to the name of the Java file. 

EX: The appropriate test files for Problem1 *must* adhere to the following naming and storage conventions:
```
Coffee
|- scripts
    |- input-files
        |- Problem1-input.txt
    |- java-test
        |- Problem1
            |- Problem1Demo1.java
            |- Problem1Demo1Runner.java
```
To add/remove test cases, edit the appropriate input-files and expected-output text files.

Make sure that each file is located in the correct directory!
```
java-test > Directory containing java files to be tested
input-files > Directory containing txt files with tests for a java-file
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/aileenzeng/Coffee/tags). 

## Authors

* **Aileen Zeng** - *Project Lead (Shell/Python/Java)* - [aileenzeng](https://github.com/aileenzeng)
* **Frank Gonzalez Rojas** - *Initial work (HTML/CSS)* - [That1Handyman](https://github.com/That1Handyman)
* **Lizeth Rogel** - *Initial work (PHP)* - [xlzth](https://github.com/xlzth)

See also the list of [contributors](https://github.com/aileenzeng/Coffee/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* BrickHack and RIT for sponsoring a great hackathon
* RocHack for having amazing people :)

