#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Name:        To-do List
# Purpose:     Maintain a command-line to-do list
# Author:      Naveen Unnikrishnan
# Created:     03/07/2018
#-------------------------------------------------------------------------------

__author__ = 'Naveen Unnikrishnan'
__version__ = 1.0

import argparse
import json
import os

def makeBlankTodo():
	'''
	Makes an empty to-do list file.
	'''
	with open(todoFile,'w') as file:
		json.dump(todo,file)

def printTodo(todoList):
	'''
	Prints the todo list.
	'''
	print()
	print("TO-DO LIST".center(os.get_terminal_size().columns))
	print('='*os.get_terminal_size().columns)
	print()
	if len(todoList) == 0:
		print('\tYour todo list is empty!')
	else :
		for item in todoList:
			for i in item:
				print('\t'+i + ') ' + item[i])
	print('\n')

def addItem(todoFile, todo, item):
	'''
	Adds an item to the todo list
	'''
	try:
		with open(todoFile,'w') as jsonFile:
			todo['list'].append({str(len(todo['list'])+1):' '.join(item)})
			json.dump(todo, jsonFile, indent=4)
	except:
		print('Oops! Something went wrong when adding that to your todo list.')

def deleteItem(todoFile, todo, idx):
	'''
	Delete item from todo list
	'''
	length = len(todo['list'])
	try:
		if idx > length:
			raise ValueError
		with open(todoFile,'w') as jsonFile:
			for i in range(idx-1,length-1):
				todo['list'][i][str(i+1)] = todo['list'][i+1][str(i+2)]
			del(todo['list'][length-1])
			json.dump(todo, jsonFile, indent=4)
	except:
		print('Oops! Something went wrong when deleting that entry.')


if __name__ == '__main__':
	# Setting up command-line arguments
	parser = argparse.ArgumentParser(prog = 'todo', description = 'Create and maintain a to-do list.')
	parser.add_argument('-s', '--suppress', help = "Don't display todo-list after action.", action = 'store_true')
	subparsers = parser.add_subparsers(dest = 'command')

	parser_a = subparsers.add_parser('add', help = 'Add a new item to to-do list.')
	parser_a.add_argument('item', nargs='*', help = 'Item to be added to to-do list.')

	parser_d = subparsers.add_parser('del', help = 'Delete item from to-do list.')
	parser_d.add_argument('id', type = int, help='S.No. of item to be deleted from to-do list.')	

	parser_c = subparsers.add_parser('clear', help = 'Clear to-do list.')
	
	args = parser.parse_args()

	# Initializing variables
	todoFile = os.path.join(os.environ['HOME'],'.todo.json')
	todo = {}
	todo['list'] = []

	# Check if todo file exists
	if os.path.isfile(todoFile) is False:
		makeBlankTodo()

	# Clear command
	if args.command == 'clear':
		makeBlankTodo()

	# Reading current to-do list
	try:
		with open(todoFile,'r') as jsonFile:
			todo = json.load(jsonFile)
	except:
		print('Oops! Looks like someone has messed up your todo file. All your existing data will be lost!')
		makeBlankTodo()

	# Add an item
	if args.command == 'add' and args.item != []:
		addItem(todoFile, todo, args.item)

	# Delete an item
	if args.command == 'del' and args.id > 0:
		deleteItem(todoFile, todo, args.id)

	# Supress display after adding/deleting/clearing
	if args.suppress is None or args.suppress is False:
		printTodo(todo['list'])