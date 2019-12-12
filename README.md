About this software
===================
This loan calculator software take input which contains interest rate, loan amount, term length(in years) and down payment then calculates
 and displays the monthly payment and interest paid.


Requirements
============
Python 3.0+


How to use
==========
This software can be run via command line

From your command line/terminal, navigate to the main project directory. Run the code below
$ python calculate.py -t <""" enter loan details text here""">  -f path_to_file -o payment.txt .


-t lets you add the input text via the command line
-f lets you read input from a file
-o lets you specify path to save output.

Please note that your input data also be in the main directory, and you can specify either of the input flags (-t, -f) and not both. 


Run Tests
=========
Navigate to the main project directory, using your command line. Enter the code below:   
$ python -m unittest discover


Help
====
For help option, run the following code:   
$ python calculate.py -h
