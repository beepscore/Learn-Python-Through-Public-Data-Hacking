# Purpose
Do tutorial Learn Python Through Public Data Hacking by David Beazley.  

## bus
Practice using Python to download bus locations xml,
write it to a file, parse it, find a bus.

## potholes
Manually download pothole data csv.
Parse it, rank street addresses by potholiness.

# food_inspections
Manually download food inspection data csv.
https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5

# References

## Learn Python Through Public Data Hacking by David Beazley
https://www.youtube.com/watch?v=RrPZza_vZ3w  
http://www.dabeaz.com/pydata
http://www.dabeaz.com/pydata/LearnPyData.pdf

## DigitalMockingbird
Nicely organinzed repo based on Beazley's tutorial.  
Could fork this, but I wanted to learn more by doing it myself!  
https://github.com/DigitalMockingbird/Learn-Python-Through-Public-Data-Hacking

## defusedxml
Python standard xml library is vulnerable to attacks (xml 'bombs') such as billion laughs.  
use defusedxml instead  
https://pypi.python.org/pypi/defusedxml/

# Procedure

## .gitignore
The project expects data will be located in data/input and data/output but these
files are ignored by github.

## run program
The program downloads bus locations.

cd project root directory

activate virtual environment  

    python3 -m main

## output file
Note the xml output file has one line, then many blank lines, then data.

## Unit tests
To run tests, open terminal shell.  
cd to project directory. Run tests via python command or bash script.

### python command
This command lists and tests all modules

    python3 -m unittest discover -s tests/

alternatively, can supply test module names as args

    python3 -m unittest tests.test_bus tests.test_potholes tests.test_food_inspections
    
    python3 -m unittest tests.test_bus
    python3 -m unittest tests.test_potholes
    python3 -m unittest tests.test_food_inspections
    

# Appendix virtual environment and requirements

## venv create and activate virtual environment

### create virtual environment
In project root directory  
python3 -m venv ./venv

### activate virtual environment
cd project root directory  
activate virtual environment

#### macOS

    source venv/bin/activate
    
#### Windows

    venv\Scripts\activate

venv should show at beginning of command prompt  

## install items in requirements file
with virtual environment active

    pip3 install -r requirements.txt

## Appendix Anaconda create and activate virtual environment

### create virtual environment
In project root directory  

If using Anaconda, python3 -m venv ./venv may throw error  

Error: Command '['/Users/stevebaker/Documents/projects/pythonProjects/Learn-Python-Through-Public-Data-Hacking/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.  
http://stackoverflow.com/questions/41857088/new-python-3-6-venv-giving-error-on-macos  
http://stackoverflow.com/questions/41412876/how-do-you-activate-an-anaconda-environment-in-the-terminal-with-mac-os-x?noredirect=1&lq=1  

So instead use anaconda command  

    conda create -n <project_name> python=3.6
e.g.
    conda create -n lptpdh python=3.6

### activate virtual environment
cd project root directory  
activate virtual environment

#### macOS, linux

    source activate <project_name>
    
(<project_name>) should show at beginning of command prompt  

    source deactivate <project_name>

#### defusedxml
I deleted directory venv, left file requirements.txt  
Pycharm showed requirement not met for defusedxml  

package was not available for macos in channels defaults or anaconda-fusion  
In Anaconda navigator add channel conda-forge.  
Then with environment lptpdh active, in Anaconda navigator install defusedxml  
