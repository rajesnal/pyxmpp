#!/usr/bin/python -u

import libxml2
import time
import sys
import traceback
import socket

from pyxmpp import ClientStream,JID,Iq,Presence,Message,StreamError
from pyxmpp.jabberd import ComponentStream

class Stream(ComponentStream):
	def state_change(self,state,arg):
		print "*** State changed: %s %r ***" % (state,arg)

if len(sys.argv)<5:
	print "Usage:"
	print "\t%s name secret server port" % (sys.argv[0])
	sys.exit(1)

print "creating stream..."
s=Stream(JID(sys.argv[1]),sys.argv[2],sys.argv[3],int(sys.argv[4]))

print "connecting..."
s.connect()

print "looping..."
try:
	s.loop(1)
except KeyboardInterrupt:
	s.close()
	pass

print "exiting..."