#!/usr/bin/env python

import log

"""
Created on 2013-08-27
 
@author: James Johnson
@copyright: ExcellentInGenuity LLC
@name: Element Object for XML elements
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
class Elemobj:

	def __init__(self, name='', text='', attributes={}, children=[]):
		self.myversion = '1.0.0b'
		self.mylog = log.Log()
		self.name = name
		self.text = text
		self.attributes = attributes
		self.children = children

	def set_name(self, aname):
		if aname != '' or None:
			self.name = aname

	def get_name(self):
		return self.name

	def add_attribute(self, aname, avalue):
		if aname != '' or None:
			if avalue != '' or None:
				self.attributes.update({aname:avalue})

