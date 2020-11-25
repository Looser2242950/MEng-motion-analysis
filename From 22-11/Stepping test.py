# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:14:47 2020

@author: johan
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import btk
import sqlite3
"""Test Extracting Dta about events from C3d"""

trial1c3d = 'TRIT 076 Stepping 11.c3d'


reader = btk.btkAcquisitionFileReader()
reader.SetFilename(trial1c3d) # set a filename to the reader
reader.Update()
trial_1 = reader.GetOutput()
subject = trial_1.GetEventNumber()


# #Get full dataset of column "LKneeAngles" in x, y, and z
# trial_1 = reader.GetOutput() # is the btk aquisition object
# lknee = trial_1.GetPoint("LKneeAngles")
# lkneevalues = lknee.GetValues() 

# # returns a "btkEventCollectionIterator object"?
# #<btk.btkEventCollectionIterator; proxy of <Swig Object of type 'btkAcquisition_impl::EventIterator *' at 0x00000154F5CF3C90> >
# event = (trial_1.FindEvent("Foot Strike"))
# print(event)

# #Returns number of events ex. Left heelstrike, left foot off, etc
# event2 = (trial_1.GetEventNumber())
# print(event2)

# #Returns a btkEvent 
# #<btk.btkEvent; proxy of <Swig Object of type 'btkEventCollection_impl::ItemPointer *' at 0x00000154F5CF3990> >
# event3 = (trial_1.GetEvents()).GetItem(1)
# print(event3)

# #Returns a btk Event
# event3a = trial_1.GetEvent(0)

# #Returns frame number of that event (100 frames per second)
# event4=event3a.GetFrame()

# #Returns Left or Right
# event4a = event3a.GetContext()

# #Returns description of event
# event4b = event3a.GetDescription()

# #Returns event name (Foot strike of Foot Off)
# event4c = event3a.GetLabel()

# #Returns exact time of event (sismilar to Frame number/100)
# event4d = event3a.GetTime()

# #Returns time stamp?????
# event4e = event3a.GetTimestamp()

# #Returns ID???
# event4f = event3a.GetId()

# #Returns Subject (patient ID? ex MB 022)
# event4g = event3a.GetSubject()