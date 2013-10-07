#!/usr/bin/env python
__metaclass__ = type

from xml.etree import ElementTree as ET
import os
import log
import elemobj


class Parse:

	"""
	Created on 2013-06-27
	@author: James Johnson
	@Copyright: ExcellentInGenuity LLC
	@name: Parse Obeject for Smart Control Device Updater
	@description: XML file parser
	@license:
	Copyright (c) 2013, James Johnson - Excellent InGenuity LLC
	All rights reserved.

	Redistribution and use in source and binary forms, with or without modification,
	are permitted provided that the following conditions are met:

	  Redistributions of source code must retain the above copyright notice, this
	  list of conditions and the following disclaimer.

	  Redistributions in binary form must reproduce the above copyright notice, this
	  list of conditions and the following disclaimer in the documentation and/or
	  other materials provided with the distribution.

	  Neither the name of the Excellent InGenuity LLC nor the names of its
	  contributors may be used to endorse or promote products derived from
	  this software without specific prior written permission.

	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
	DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
	ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
	ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
	http://excellentingenuity.com
	"""
	
	__version__ = "Version: 1.0.0e"


	def __init__(self, afile=''):
		""" Initialize parse object """
		self.version = '1.0.0e'
		self.mylog = log.Log(console=True)
		self.thefile = None
		self.doc_root = None
		self.xml = None
		self.data = ''
	
	def set_file(self, afile):
		""" Set self.thefile to value of afile if not null or '' """
		if afile is None:
			return False
		elif afile == '':
			return False
		elif os.path.exists(afile):
			self.thefile = afile
			return True
		else:
			return False

	def open(self):
		# TODO: write test for open function
		try:
			self.xml = ET.parse(open(self.thefile, 'r'))
			return True
		except IOError:
			print "Unable to open xml file"
			self.mylog.write_log("Unable to open xml file")
			return False

	def parse(self):
		""" parse the file into an xml tree """
		# TODO: write test for parse function
		self.open()
		self.doc_root = self.xml.getroot()
		self.data = self.elem_parse(self.doc_root)
		self.mylog.write_log(vars(self.data))


	def elem_parse(self, element):
		""" recursive parsing of element and its children into elemobj's """
		d = elemobj.Elemobj(element.tag, element.text, element.attrib)
		for child in element:
			self.mylog.write_log(vars(child))
			d.children.append(self.elem_parse(child))

		return d
