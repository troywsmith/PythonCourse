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

### Chapter 2: Variables, expressions, and statements

assignment: A statement that assigns a value to a variable.

concatenate: To join two operands end to end.

comment: Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.

evaluate: To simplify an expression by performing the operations in order to yield a single value.

expression: A combination of variables, operators, and values that represents a single result value.

floating point: A type that represents numbers with fractional parts.

integer: A type that represents whole numbers.

keyword: A reserved word that is used by the compiler to parse a program; you cannot use keywords like if, def, and while as variable names.

mnemonic: A memory aid. We often give variables mnemonic names to help us
remember what is stored in the variable.

modulus operator: An operator, denoted with a percent sign (%), that works on integers and yields the remainder when one number is divided by another.

operand: One of the values on which an operator operates.

operator: A special symbol that represents a simple computation like addition, multiplication, or string concatenation.

rules of precedence: The set of rules governing the order in which expressions involving multiple operators and operands are evaluated.

statement: A section of code that represents a command or action. So far, the statements we have seen are assignments and print expression statement.

string A: type that represents sequences of characters.

type A: category of values. The types we have seen so far are integers (type int), floating-point numbers (type float), and strings (type str).

value: One of the basic units of data, like a number or string, that a program manipulates.

variable: A name that refers to a value

### Chapter 3: Conditional Execution

body: The sequence of statements within a compound statement.

boolean expression: An expression whose value is either True or False.

branch: One of the alternative sequences of statements in a conditional statement.

chained conditional: A conditional statement with a series of alternative branches.

comparison operator: One of the operators that compares its operands: ==, !=, >, <, >=, and <=.

conditional statement: A statement that controls the flow of execution depending on some condition.

condition: The boolean expression in a conditional statement that determines which branch is executed.

compound statement A statement that consists of a header and a body. The header ends with a colon (:). The body is indented relative to the header.

guardian pattern: Where we construct a logical expression with additional comparisons to take advantage of the short-circuit behavior.

logical operator: One of the operators that combines boolean expressions: and, or, and not.

nested conditional: A conditional statement that appears in one of the branches of another conditional statement.

traceback: A list of the functions that are executing, printed when an exception occurs.

short circuit: When Python is part-way through evaluating a logical expression and stops the evaluation because Python knows the final value for the expression without needing to evaluate the rest of the expression.

### Chapter 4: Functions