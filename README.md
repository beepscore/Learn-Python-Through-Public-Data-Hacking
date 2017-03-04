# Purpose
Do tutorial Learn Python Through Public Data Hacking by David Beazley.  
Practice using Python to download bus locations xml,
write it to a file, parse it, find a bus.

# References

## Learn Python Through Public Data Hacking by David Beazley
https://www.youtube.com/watch?v=RrPZza_vZ3w  
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

cd <project root directory>

activate virtual environment  

python3 -m main

## output file
Note the xml output file has one line, then many blank lines, then data.

# Appendix virtual environment
### install virtual environment
cd <project root directory>
python3 -m venv ./venv

## activate virtual environment
cd <project root directory>

### on macOS  
source venv/bin/activate
venv should show at beginning of command prompt

### on Windows  
venv\Scripts\activate


# Appendix requirements
## install items in requirements file
First activate virtual environment  
Then  

pip3 install -r requirements.txt

