pyxml-objector
==============

A python class that creates a nested object that follows the structure of the xml document and its content.

Version 1.0.0c

Objects files provided:
  
  parse.xml -> parses the supplied xml file into an elementobject
  elemobj.py -> the nested xml data object returned by parse.py
  log.py -> logging object that logs to a text file and/or to the console
  tests -> nosetest compatible tests

Usage instructions:

Include parse.xml in your python file and instantiate a new parse object:

		import parse.py
		
		parser = parse.Parse()

	Now use your new parse object:

		parser.set_file('xml.xml')
		parser.parse()

	After running the parse command you can access the elemobj object via

		myobj = parser.data


Intended Updates:
	1. Streamline parse object creation, parsing, and return of elemobj to a single command.
	2. Update elemobj to be more self-aware and itterable.
	3. Add tests for the elmeobj
