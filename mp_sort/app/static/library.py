from org.transcrypt.stubs.browser import *
import random, time

def gen_random_int(number, seed):
	rand_array = [num for num in range(number)]
	random.shuffle(rand_array)
	return rand_array

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array

	array = gen_random_int(number, seed)
	# convert the items into one single string
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = None

	array_str = ",".join(str(num) for num in array)
	array_str += "."

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	array_str = document.getElementById("generate").innerHTML
	array_str = array_str.split(",")
	array_str[len(array_str) - 1] = array_str[len(array_str) - 1].split(".")[0]
	sortedarray = [int(num) for num in array_str]
	n = len(sortedarray)
	swapped = True
	new_n = 0
	while swapped:
		swapped = False
		for si in range(1, n):
			if sortedarray[si - 1] > sortedarray[si]:
				sortedarray[si - 1], sortedarray[si] = sortedarray[si], sortedarray[si - 1]
				swapped = True
				new_n = si
		n = new_n
	array_str = ",".join(str(num) for num in sortedarray)
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	pass

	array_str = None

	document.getElementById("sorted").innerHTML = array_str


