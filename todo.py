#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Name:        To-do List
# Purpose:     Maintain a command-line to-do list
# Author:      Naveen Unnikrishnan
# Created:     03/07/2018
#-------------------------------------------------------------------------------

__author__ = 'Naveen Unnikrishnan'
__coauthor__ = 'Swarup N'
__version__ = 1.3

import argparse
import json
import os
import datetime
import re
import random

from lolcat import LolCat

def makeBlankTodo():
	'''
	Makes an empty to-do list file.
	'''
	with open(todoFile,'w') as file:
		json.dump(todo,file)

def printTodo(todo, ids, options, enable_lolcat=False):
	'''
	Prints the todo list.
	'''
	print()
	to_print = "TO-DO LIST".center(os.get_terminal_size().columns) + '\n' + '='*os.get_terminal_size().columns + '\n' + '\n'
	if len(todo['list']) == 0:
		to_print = to_print + '\tYour todo list is empty!\n'
	else:
		searchTags = options.tag_main
		j = 1
		for i in ids:
			skip = False
			if searchTags is not None:
				for tag in searchTags:
					tag = tag.lower()
					if tag not in todo['tags'][i[1]]:
						skip = True
						break
			if skip:
				continue
			if i[0] == 1:
				s = '\t\u2757 \u2B50\t'
			elif i[0] == 2:
				s = '\t\u2757\t'
			elif i[0] == 3:
				s = '\t\u2B50\t'
			else:
				s = '\t\t'
			s += str(j) + ') '
			if options.verbose and todo['tags'][i[1]] != []:
				s += ', '.join(todo['tags'][i[1]])
				s += ' : '
			s += todo['list'][i[1]]
			to_print = to_print + s + '\n'
			j = j+1

	if not enable_lolcat:
		print(to_print)
	else:
		lolcat = LolCat(options)
		to_print_list = to_print.split('\n')
		lolcat.cat(to_print_list)

def addItem(todoFile, todo, item, priority, tags):
	'''
	Add item(s) to the todo list
	'''
	try:
		with open(todoFile,'w') as jsonFile:
			item = ' '.join(item)
			item = item.split('^')
			for i in item:
				i = i.strip()
				timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
				todo['list'][timestamp] = i
				todo['priority'][timestamp] = priority
				todo['tags'][timestamp] = []
				if tags is not None:
					todo['tags'][timestamp] = [x.lower() for x in tags]
					todo['tags'][timestamp] = sorted(todo['tags'][timestamp])
			json.dump(todo, jsonFile, indent=4)
	except:
		print('Oops! Something went wrong when adding that to your todo list.')

def deleteItem(todoFile, todo, idx, ids, delTags):
	'''
	Delete item(s) from todo list
	'''
	length = len(todo['list'])
	idx = ' '.join(idx)
	if re.search(r'[^\s0-9-]', idx) is not None:
		x = input("Your contains characters that are not numbers, white spaces or dashes. Continuing might result in unexpected behaviour. Continue? [y/n]\t")
		if(x == 'n'):
			return
	idx = re.split(r"[^-0-9]", idx)
	idx = list(filter(None, idx))
	result = []
	for part in idx:
		try:
			if '-' in part:
				a, b = part.split('-')
				if representsInt(a) and representsInt(b):
					a, b = int(a), int(b)
					result.extend(range(a, b + 1))
				elif representsInt(a):
					a = int(a)
					result.append(a)
				elif representsInt(b):
					b = int(b)
					result.append(b)
			else:
				a = int(part)
				result.append(a)
		except:
			print('Oops! Something went wrong when processing '+ str(part) +'.')
	idx = result
	if delTags is not None:
		for tag in delTags:
			for i in range(len(ids)):
				if tag in todo['tags'][ids[i][1]]:
					if i+1 not in idx:
						idx.append(i+1)
	idx = sorted(idx, key=int, reverse=True)
	for i in idx:
		try:
			i = int(i)
			if i > length:
				continue
			del(todo['list'][ids[i-1][1]])
			del(todo['priority'][ids[i-1][1]])
			del(todo['tags'][ids[i-1][1]])
			del(ids[i-1])
		except:
	 		print('Oops! Something went wrong when deleting entry ' + str(i) +'.')
	with open(todoFile,'w') as jsonFile:
		json.dump(todo, jsonFile, indent=4)

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
	# Setting up command-line arguments
	parser = argparse.ArgumentParser(prog = 'todo', description = 'Create and maintain a to-do list.')
	parser.add_argument('--suppress', '-s', help = "Don't display todo-list after action.", action = 'store_true')
	parser.add_argument('--verbose', '-v', help = "Display tags along with items in todo-list.", action = 'store_true')	
	parser.add_argument('--tag', '-t', nargs='*', help = 'Tag(s) to be searched for.', dest = 'tag_main')
	subparsers = parser.add_subparsers(dest = 'command')

	parser_a = subparsers.add_parser('add', help = 'Add new item(s) to to-do list.')
	parser_a.add_argument('item', nargs='*', help = 'Item(s) to be added to to-do list.')
	parser_a.add_argument('--urgent', '-u', help = "Flag the item as urgent.", action = 'store_true')
	parser_a.add_argument('--important', '-i', help = "Flag the item as important.", action = 'store_true')
	parser_a.add_argument('--tag', '-t', nargs='*', help = 'Tag(s) to be added to item(s).', dest = 'tag_add')

	parser_b = subparsers.add_parser('del', help = 'Delete item(s) from to-do list.')
	parser_b.add_argument('id', nargs='*', help='S.no(s). of item(s) to be deleted from to-do list.')
	parser_b.add_argument('--tag', '-t', nargs='*', help = 'Tag(s) to be deleted.', dest = 'tag_del')

	parser_c = subparsers.add_parser('clear', help = 'Clear to-do list.')

	parser_d = subparsers.add_parser('lolcat', help = 'Display message as lolcat',)
	parser_d.add_argument('--seed', '-S', help = "Rainbow seed", type = int, default = 0, dest = 'seed')
	parser_d.add_argument('--spread', '-p', help = "Rainbow spread", type = float, default = 3.0, dest = 'spread')
	parser_d.add_argument('--frequency', '-F', help = "Rainbow frequency", type = float, default = 0.1, dest = 'freq')
	parser_d.add_argument('--force', '-f', help = "Force colour even when stdout is not a tty", action = 'store_false')
	parser_d.add_argument('-3', action = 'store_const', dest = 'mode', const = 8, help = 'Force 3 bit colour mode')
	parser_d.add_argument('-4', action = 'store_const', dest = 'mode', const = 16, help = 'Force 4 bit colour mode')
	parser_d.add_argument('-8', action = 'store_const', dest = 'mode', const = 256, help = 'Force 8 bit colour mode')

	args = parser.parse_args()

	# Initializing variables
	todoFile = os.path.join(os.environ['HOME'],'.todo.json')
	todo = {}
	todo['list'] = {}
	todo['priority'] = {}
	todo['tags'] = {}
	ids = []

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
		print('Awww snap! Looks like someone has messed up your todo file. All your existing data will be lost!')
		makeBlankTodo()

	# Add item(s)
	if args.command == 'add' and args.item != []:
		priority = 4
		if args.urgent == True:
			priority -= 2
		if args.important == True:
			priority -= 1
		addItem(todoFile, todo, args.item, priority, args.tag_add)

	# Get IDs and sort
	for i in todo['priority']:
		ids.append((todo['priority'][i],i))
	ids = sorted(ids, key=lambda x: x[1])
	ids = sorted(ids, key=lambda x: x[0])

	# Delete item(s)
	if args.command == 'del' and (args.id != [] or args.tag_del != []):
		deleteItem(todoFile, todo, args.id, ids, args.tag_del)

	# Supress display after adding/deleting/clearing
	if args.suppress is None or args.suppress is False:
		printTodo(todo, ids, args, enable_lolcat=(args.command == 'lolcat'))
