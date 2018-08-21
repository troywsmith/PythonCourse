# Programming for Everybody (Getting Started with Python)

### Generic Computer
Central Processing Unit (CPU): runs the programs 
Input Devices: keyboard, mouse, touch screen
Output devices: screen, speakers, printer, DVD burner
Main Memory (RAM): fast, small temporary storage, lost on reboot
Secondary Memory: slower large permanent storage, lasts until deleted
Network Connection: very slow place to store/retrieve data

### Python 
Author: Guido van Rossum
Overview: High-level language intended to be relatively straightforward for humans to read/write and for computer to read/process

### Chapter 1: Why we program
Reserved words: cannot use as variable names/identifiers
False,	class,	finally,	is,	return, None,	continue,	for, lambda,	try, True,	def,	from,	nonlocal,	while, and,	del,	global,	not,	with, as,	elif,	if,	or,	yield, assert,	else, import,	pass, break,	except,	in,	raise

Interactive vs Script:
interactive - you type directly to python one line at a time and it responds
script - you enter a sequence of statements (lines) into a file using a text editor and tell python to execute the statements in the file

CONVERSING WITH PYTHON:
 python3 [filename] : runs python on a file
 quit() : exits out of python in interactive mode

Machine language: the language the computer understands that is represented all in zeros and ones. Not portable across different types of hardware.

Programming Language Translators
Interpreter: reads the source code of the program, parses it, and interprets the instructions on the fly. Python is an interpreter.
Compiler: Needs to be handed the whole program in a file and then run it as a process to translate the high-level source code into machine language and then the compiler puts the resulting machine language into a file for later execution

Variable: the labels we use to refer to this stored data

input: get data from the outside world. ex: reading data from a file or some kind of sensor like a microphone/GPA

output: display the results of the program on a screen or store them in a file or even write them to a device like a speaker 

sequential execution: perform statements one after another 

repeated execution: perform some set of statements repeatesly

reuse: write a set of instructions once and give them a name and then reuse those instructions as needed

Type of Errors:
syntax errors: violation of python grammar rules
logic errors: violation of order of the statements/how they relate to each other
semantic errors: mistake in the program

#### Glossary

bug: An error in a program.

central processing unit: The heart of any computer. It is what runs the software
that we write; also called “CPU” or “the processor”.

compile: To translate a program written in a high-level language into a low-level language all at once, in preparation for later execution.

high-level language: A programming language like Python that is designed to be easy for humans to read and write.

interactive mode: A way of using the Python interpreter by typing commands and expressions at the prompt.

interpret: To execute a program in a high-level language by translating it one line at a time.

low-level language: A programming language that is designed to be easy for a computer to execute; also called “machine code” or “assembly language”.

machine code: The lowest-level language for software, which is the language that is directly executed by the central processing unit (CPU).

main memory: Stores programs and data. Main memory loses its information when the power is turned off.

parse: To examine a program and analyze the syntactic structure.

portability: A property of a program that can run on more than one kind of computer.

print function: An instruction that causes the Python interpreter to display a value on the screen.

problem solving: The process of formulating a problem, finding a solution, and expressing the solution.

program: A set of instructions that specifies a computation.
prompt When a program displays a message and pauses for the user to type some input to the program.

secondary memory: Stores programs and data and retains its information even when the power is turned off. Generally slower than main memory. Examples of secondary memory include disk drives and flash memory in USB sticks.

semantics: The meaning of a program.

semantic error: An error in a program that makes it do something other than what the programmer intended.

source code: A program in a high-level language.

#### Exercises
Exercise 1: What is the function of the secondary memory in a computer?
c) Store information for the long term, even beyond a power cycle

Exercise 2: What is a program?
A list of instructions 

Exercise 3: What is the difference between a compiler and an interpreter?
compiler translates a program written in a high-level language into a low-level language all at once, in preparation for later execution.
interpreter executes a program in a high-level language by translating it one line at a time.

Exercise 4: Which of the following contains “machine code”?
a) The Python interpreter

Exercise 5: What is wrong with the following code:
the print is spelled wrong and there is no () for the print function

Exercise 6: Where in the computer is a variable such as “x” stored after the following Python line finishes?
b) Main Memory

Exercise 7: What will the following program print out:
b) 44

Exercise 8: Explain each of the following using an example of a human capability: 
(1) Central processing unit: brain 
(2) Main Memory: brain
(3) Secondary Memory: brain
(4) Input Device: eyes
(5) Output Device: mouth

Exercise 9: How do you fix a “Syntax Error”?
start by check the line that python points to for grammar mistakes
