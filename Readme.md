[![Python application](https://github.com/kitkay/zzcoding/actions/workflows/python-app-test.yml/badge.svg)](https://github.com/kitkay/zzcoding/actions/workflows/python-app-test.yml)

Applying TDD(test driven development) on plaindrome scripts.
Python 3.9.7, unittest, pytest

Documents:

    1st test:
        file: palindromChecker.py
        tester: test_palindrome.py

Running the scripts:

    1st: Assumed that you already have installed python.
            if not then go to python website, download and install.

    2nd: Open command prompt.

    3rd: CD to directory to where this scripts are located to your computer.
            e.g.
                cd drive_letter:/path_to_dir_of_scripts 
    
    4th:
        On your command prompt type 'python' then 'name_of_script.py':

        e.g.
            python name_of_script.py

Testing the scripts:

    1st: Open command prompt.

    2nd: CD to directory to where this scripts are located to your computer.
            e.g.
                cd drive_letter:/path_to_dir_of_scripts/test

    3rd: On your command prompt test the scripts:
            e.g.
                python unittest -m test.test_palindrome
                                OR
                python -m unittest 
                    ~to run all test if any...

    4th: Github Actions:

        Go to Actions tab in github and click 'Create python-app-test.yml'
        You could re-run jobs or just click 'build' to check the test.
