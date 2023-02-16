# exercise_v

A testing framework for financial software.

To run the test suite, build a virtual environment from the requirements.txt file and run the pytest command 
from the project root directory.

When run from the command line, reports will be generated as reports/report.hmtl 
Otherwise, the "--html=reports/report.html" option needs to be added in order to generate reports.

A .env file with valid credentials needs to be created in the project root directory 
"default_user" and "default_password" will need to be set in this file. This file will be excluded from github.