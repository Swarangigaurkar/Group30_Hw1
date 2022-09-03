Tests are written in Python using Pytest 5.0 testing framework.

**Install Pytest** </br>
To run these tests install Pytest latest version onto your local machine.
```
>>> pip install pytest
```

**Running the tests** </br>
This project uses pytest so running pytest at the root folder will execute all tests on current environment.
```
>>> pytest
```  
OR </br>
Run the test file
```
>>> test_sample.py
``` 

**Results** </br>

If all the test cases are passed, no error is shown.

If any of the test cases mentioned fails, it shows the error in red.

```
ERROR collecting test/test_sample.py - assert 6.0 == 3
!!!!!!!!!!!! Interrupted 1 error during collection !!!!!!!!!!!!!!!!!!!
```

 
