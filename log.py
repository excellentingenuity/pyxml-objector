#!/usr/bin/env python

__metaclass__ = type

import datetime



class Log:

	"""
	Created on 2013-06-27
	 
	@author: James Johnson
	@Copyright: ExcellentInGenuity LLC
	@name:Update Log Object
	@description: Logs program information to a log file with optional 
		console output
	@license:
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
	
	__version__ = "Version: 1.0.0a"

	def __init__(self, thisfile='', console=False):
		self.my_version = '1.0.0a'
		self.myfile = None
		self.logpath = "./log/"
		if thisfile != '' or None:
			self.set_file(thisfile)
		else:
			self.set_log_file_name()


		if console != '' or None:
			self.console = console
		

	def set_file(self, thisfile):
		if thisfile != '' or None:
			tfile = self.logpath + str(thisfile)
			try:
				self.myfile = open(tfile, 'a')
			except IOError:
					print "Unable to open file"

	def write_log(self, message):
		if message != '' or None:
			now = datetime.datetime.now()
			mymessage = now.strftime("%Y%m%d%H%M")+': '+str(message)+'\n'
			#print(self.myfile)
			try:
				self.myfile.write(str(mymessage))
			except IOError:
				print "Unable to write message to logfile"

			if self.console == True:
				print(str(mymessage))	

	def close_log(self):
		self.myfile.close()

	def set_log_path(self, thispath):
		if thispath != '' or None:
			self.logpath = thispath

	def set_log_file_name(self):
		now = datetime.datetime.now() 
		self.set_file(now.strftime("%Y%m%d%H%M")+".txt")

	def set_console(self, console):
		if console != '' or None:
			self.console = console
