#!/usr/bin/env python
# encoding: utf-8
"""
buzzkiller.py

Created by Michael Dory on 2011-03-05.
Copyright (c) 2011 DxM. All rights reserved.
"""

import argparse
import sys
# import shlex # the next step is to do better multi-word phrase checking

# this is where the magic happens
def main(arguments=None):
		
	# create the parser
	parser = arguments(
			description='Chomp you up some buzzwords.'
	)

	# check the command line for incoming words
	parser.add_argument(
			'checkWords', metavar='str', type=str, nargs='*',
			help='words you want to check against from the command line'
	)

	# allow folks to check a file instead of against the command line
	parser.add_argument(
			'--file', metavar='open', type=open, nargs='?',
			help='words you want to check against from a file'
	)

	# allow folks to check a file instead of against the command line
	parser.add_argument(
			'-v', dest='verbose', action='store_true',
			help='verbose mode'
	)

	# make a seperate log file, if that's your sort of thing
	parser.add_argument(
			'--log', type=argparse.FileType('w'), default=sys.stdout,
			help='the file where the sum should be written '
					 '(default: write the sum to stdout)'
	)
	
	# parse the command line
	args = parser.parse_args()

	# open the files to compare against
	weaselwords = readFile("./textfiles/weaselwords.txt")
	buzzwords = readFile("./textfiles/buzzwords.txt")
	officewords = readFile("./textfiles/officewords.txt")
	
	# define the document to search through
	document = []

	# if there is a file specified, let's search that
	if (args.file is not None):
		newFile = fileToList(args.file, True)
		document.extend(newFile)
	
	# if there are additional words on the end, let's search them too
	if (args.checkWords is not None):
		document.extend(args.checkWords)

	# if we've actually got something, let's check it!
	if (document is not None):
		args.log.write('\nAlrighty, let\'s see what you\'ve got here: \n\n')

		# log the weasel, buzz and office words when they are found
		for line in document:
				line = line.strip()
				for token in line.split(" "):
				
					# call out the weasels
					if token in weaselwords:
						args.log.write('WEASELWORD: ' + token + '\n')

					# call out the buzzwords
					if token in buzzwords:
						args.log.write('BUZZWORD: ' + token + '\n')

					# call out the office jargron terms
					if token in officewords:
						args.log.write('OFFICEWORD: ' + token + '\n')

	# if someone set the -v verbose flag, tell them about the arguments they used
	if (args.verbose is not False):
		args.log.write('\n--------------------------- \n\n')
		args.log.write('These were your test words: \n')
		args.log.write('\n--------------------------- \n\n')

		# log(out the list of words you checked against
		args.log.write('%s \n' % (document))
		args.log.write('\n--------------------------- \n\n')

		# if there was a file used, print its name
		if (args.file is not None):
			args.log.write('And we looked through a file called: %s\n\n' % args.file.name)
			args.log.write('\n --------------------------- \n\n')

	# close up shop
	args.log.write('\nHey, that was fun, right? \n')
	args.log.close()


# handy funciton for opening files and returning lists
def readFile(fileHandle): 

		print('- checking file named %s' % fileHandle)

		fileContents = open(fileHandle)
		wordList = fileToList(fileContents)

		return wordList

# make the incoming file a list
# optional: split up the file by spaces
def fileToList(file,split=False):
	inputList = []

	# grab the file
	with file as f:

		# go line-by-line with it
		for line in f:
			line = line.strip()

			# if we asked for a split, split it up by spaces
			if (split == True):
				for l in line.split(" "):
					inputList.append(l)
			else:
				inputList.append(line)

		# fire it back
		return inputList

	
# do that thang!
if __name__ == "__main__":
	print '\nHere goes some parse magic...\n'
	theMain = main(argparse.ArgumentParser)
	sys.exit(theMain)

