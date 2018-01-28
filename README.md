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
$ ./coffee.sh [java file name]
```

## Running the tests
Run coffee shell, modify the command line argument as necessary.
For example, to run the Java program ScannerTest.java, do:
```
$ ./coffee.sh ScannerTest
```

To create tests for a Java program, edit the input-files and expected-output files corresponding to the name of the Java file. 

EX: The appropriate test files for ScannerTest *must* adhere to the following naming and storage conventions:
```
Coffee
|- scripts
    |- java-files
        |- ScannerText.java
    |- input-files
        |- ScannerTest-input.txt
    |- expected-output-files
        |- ScannerTest-eo.txt
```
To add test cases, edit the appropriate input-files and expected-output text files.

Alternatively, you may find it helpful to use coffee-eo.sh to auto-generate your expected-output text files. You must have an input file already generated.

Run:
```
$ ./coffee-eo.sh [java file name]
```
EX: To create the expected test file for ScannerTest2, run:
```
$ ./coffee-eo.sh ScannerTest2
```

Make sure that each file is located in the correct directory!
```
java-files > Directory containing java files to be tested
input-files > Directory containing txt files with tests for a java-file
user-output-files > Directory containing txt files of java console logs
expected-output-files > Directory containing txt files of solutions to java tests
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/aileenzeng/Coffee/tags). 

## Authors

* **Aileen Zeng** - *Initial work (Python/Bash)* - [aileenzeng](https://github.com/aileenzeng)
* **Frank Gonzalez Rojas** - *Initial work (HTML/CSS)* - [That1Handyman](https://github.com/That1Handyman)
* **Lizeth Rogel** - *Initial work (PHP)* - [xlzth](https://github.com/xlzth)

See also the list of [contributors](https://github.com/aileenzeng/Coffee/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* BrickHack and RIT for sponsoring a great hackathon
* RocHack for having amazing people :)

