#Boa:FramePanel:Row

#*************************************************************************
# Copyright (c) 2009-2010 The University of Chicago, as Operator of Argonne
#     National Laboratory.
# Copyright (c) 2009-2010 The Regents of the University of California, as
#     Operator of Los Alamos National Laboratory.
# This file is distributed subject to a Software License Agreement found
# in the file LICENSE that is included with this distribution. 
#*************************************************************************

'''
Define the GUI elements and interface for one row of the table

@version: 
########### SVN repository information ###################
# $Date: 2014-05-24 16:40:34 -0500 (Sat, 24 May 2014) $
# $Author: jemian $
# $Revision: 1017 $
# $URL: https://subversion.xray.aps.anl.gov/small_angle/USAXS/wxmtusaxs/trunk/wxmtusaxs_row.py $
# $Id: wxmtusaxs_row.py 1017 2014-05-24 21:40:34Z jemian $
########### SVN repository information ###################
'''

import wx
import inspect
import os
from wxmtusaxs_properties import USAXSproperties
import re
import pickle

[wxID_ROW, wxID_ROWDELETE, wxID_ROWGO, wxID_ROWLABEL, wxID_ROWSET, wxID_ROWX, 
 wxID_ROWY,  wxID_ROWTHICKNESS, wxID_ROWADVANCED,
] = [wx.NewId() for _init_ctrls in range(9)]

class Row(wx.Panel):
    '''One row of settings in a wxmtusaxs table'''
    _custom_classes = {'wx.Dialog': ['USAXSproperties']} 
    def _init_coll_sizer_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.delete, 0, border=0, flag=0)
        parent.AddWindow(self.label, 0, border=0, flag=0)
        parent.AddWindow(self.set, 0, border=0, flag=0)
        parent.AddWindow(self.x, 0, border=0, flag=0)
        parent.AddWindow(self.y, 0, border=0, flag=0)
        parent.AddWindow(self.go, 0, border=0, flag=0)
        parent.AddWindow(self.thickness, 0, border=0, flag=0)
        parent.AddWindow(self.advanced, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        self._init_coll_sizer_Items(self.sizer)

        self.SetSizer(self.sizer)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_ROW, name='Row', parent=prnt,
              pos=wx.Point(51, 84), size=wx.Size(312, 25),
              style=wx.TAB_TRAVERSAL)
        self.SetClientSize(wx.Size(312, 25))
        self.SetMinSize(wx.Size(312, 25))

        self.delete = wx.BitmapButton(
              id=wxID_ROWDELETE, name='delete',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(24, 24),
              style=wx.BU_AUTODRAW)
        self.delete.Bind(wx.EVT_BUTTON, self.OnDeleteButton, id=wxID_ROWDELETE)
        self.delete.SetToolTipString(u'delete this sample')

        self.label = wx.TextCtrl(id=wxID_ROWLABEL, name='label', parent=self,
              pos=wx.Point(24, 0), size=wx.Size(80, 25), style=0, value='')
        self.label.SetMinSize(wx.Size(80, 25))
        self.label.SetToolTipString(u'description of this sample')

        self.set = wx.BitmapButton(
              id=wxID_ROWSET, name='set', parent=self,
              pos=wx.Point(104, 0), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.set.Bind(wx.EVT_BUTTON, self.OnSetButton, id=wxID_ROWSET)
        self.set.SetToolTipString(u'save current x,y values in this row')

        self.x = wx.TextCtrl(id=wxID_ROWX, name='x', parent=self,
              pos=wx.Point(128, 0), size=wx.Size(80, 25), style=0, value='')
        self.x.SetMinSize(wx.Size(80, 25))
        self.x.SetToolTipString(u'x position of sample')

        self.y = wx.TextCtrl(id=wxID_ROWY, name='y', parent=self,
              pos=wx.Point(208, 0), size=wx.Size(80, 25), style=0, value='')
        self.y.SetMinSize(wx.Size(80, 25))
        self.y.SetToolTipString(u'y position of sample')

        self.go = wx.BitmapButton(
              id=wxID_ROWGO, name='go', parent=self,
              pos=wx.Point(288, 0), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.go.Bind(wx.EVT_BUTTON, self.OnGoButton, id=wxID_ROWGO)
        self.go.SetToolTipString(u'drive to this sample')

        self.thickness = wx.TextCtrl(id=wxID_ROWTHICKNESS, name='thickness', parent=self,
              pos=wx.Point(220, 0), size=wx.Size(80, 25), style=0, value='')
        self.thickness.SetMinSize(wx.Size(80, 25))
        self.thickness.SetToolTipString(u'sample thickness')

        self.advanced = wx.Button(
              id=wxID_ROWADVANCED, name='more', label='more', parent=self,
              pos=wx.Point(300, 0), size=wx.Size(50, 24), style=wx.BU_AUTODRAW)
        self.advanced.Bind(wx.EVT_BUTTON, self.OnAdvancedButton, id=wxID_ROWADVANCED)
        self.advanced.SetToolTipString(u'Set Additional Parameters')


        self._init_sizers()

    def __init__(self, tab, tabCallback):
        '''initialize the row
            @param tab: parent object (Tab object that owns this Row object)
            @param tabCallback: callback function that takes two arguments
        '''
        # first, find the directory where this code is installed
        # so the bitmaps can be found
        # Note that this breaks edit ability of BoaConstructor
        root_dir = os.path.split(inspect.getsourcefile(Row))[0]
        self.bmp = {}
        for item in ['delete', 'set',  'go']:
            file = os.path.join(root_dir,  'graphics',  item + '.bmp')
            self.bmp[item] = wx.Bitmap(file, wx.BITMAP_TYPE_BMP)
        self._init_ctrls(tab)
        self.delete.SetBitmapLabel(self.bmp['delete'])
        self.set.SetBitmapLabel(self.bmp['set'])
        self.go.SetBitmapLabel(self.bmp['go'])
        self.tab = tab
        self.tabCallback = tabCallback
        # sizes keep getting botched in Boa, fix them here
        self._fix_sizer(self.label, wx.GROW, 2)
        self._fix_sizer(self.x, wx.GROW, 1)
        self._fix_sizer(self.y, wx.GROW, 1)
        self._fix_sizer(self.thickness, wx.GROW, 1)
        
        self.doUSAXS = True
	#josh add
	self.doFUSAXS = True
	#
        self.CHG_NPTS = False
        self.NPTS = "0"
        self.CHG_CTIME = False
        self.CTIME = "0"
        self.CHG_QMAX = False
        self.QMAX = "0"
        self.doPinhole = True
        self.CHG_EXPTIME = False
        self.EXPTIME = "0"
        self.CHG_NOEXP = False
        self.NOEXP = "0"
        self.doWAXS = True
        self.CHG_WEXPTIME = False
        self.WEXPTIME = "0"
        self.CHG_WNOEXP = False
        self.WNOEXP = "0"
# ################################
# ##       added methods       ###
# ################################

    def _fix_sizer(self, widget, flag, proportion):
        '''sizes keep getting botched in Boa, fix them here
            @param widget: GUI object to be adjusted
            @param flag: usually wx.GROW
            @param proportion: [int]'''
        item = self.sizer.GetItem(widget)
        item.SetFlag(flag)
        item.SetProportion(proportion)

    def GetLabel(self):
        '''@return row label'''
        return self.label.GetValue()

    def SetLabel(self, text):
        '''Define the label
            @param text: [string] user description of this row'''
        self.label.SetValue(text)

    def GetXY(self):
        '''@return X, Y values as a tuple'''
        x = self.x.GetValue()
        y = self.y.GetValue()
        return x, y

    def SetXY(self, x, y):
        '''Define the values
            @param x: [float] X axis position to remember
            @param y: [float] Y axis position to remember'''
        self.x.SetValue(x)
        self.y.SetValue(y)
        
    def GetThickness(self):
        '''@return row thickness'''
        return self.thickness.GetValue()

    def SetThickness(self, thickness):
        '''Define the thickness
            @param text: [string] thickness of this sample'''
        self.thickness.SetValue(thickness)

    def GetUSAXSMode(self):
        '''@return row parameters'''
        #new method, pickle the parameters object.
        # advantages: simpler, standard, works around bug
        # disadvantage: not very human readable
        # you can say that again!
        #as-yet-unimplemented
        #return pickle.dumps(self.properties)
        
        # old method, custom object serialization
        modestring = ""
        if self.doUSAXS:
            modestring += "U:"
            if self.CHG_NPTS:
                modestring += ("[NPTS:" + self.NPTS + "]") 
            if self.CHG_CTIME:
                modestring += ("[CTIME:" + self.CTIME + "]")
            if self.CHG_QMAX:
                modestring += ("[QMAX:" + self.QMAX + "]")
        if self.doPinhole:
            modestring += "P:"
            if self.CHG_EXPTIME:
                modestring += ("[EXPTIME:" + self.EXPTIME + "]") 
            if self.CHG_NOEXP:
                modestring += ("[NOEXP:" + self.NOEXP + "]")
        if self.doWAXS:
            modestring += "W:"
            if self.CHG_WEXPTIME:
                modestring += ("[WEXPTIME:" + self.WEXPTIME + "]") 
            if self.CHG_WNOEXP:
                modestring += ("[WNOEXP:" + self.WNOEXP + "]")
        return modestring

    def SetUSAXSMode(self, mode):
        '''Define the parameters
            @param text: [string] mode string for this sample'''

        tempmode = mode.partition("U:")
        mode = tempmode[0] + tempmode [2]
        if tempmode[1] != "":
            self.doUSAXS = True
        else:
            self.doUSAXS = False
        tempmode = mode.partition("P:")    
        mode = tempmode[0] + tempmode[2]
        if tempmode[1] != "":
            self.doPinhole = True
        else:
            self.doPinhole = False
        tempmode = mode.partition("W:")    
        mode = tempmode[0] + tempmode[2]
        if tempmode[1] != "":
            self.doWAXS = True
        else:
            self.doWAXS = False
        mode = re.sub("]", "",mode)
        parameters = mode.split("[")
        for param in parameters:
            test = param.partition("NPTS:")
            if test[1] != "":
                self.CHG_NPTS = True
                self.NPTS = test[2]
            test = param.partition("CTIME:")
            if test[1] != "":
                self.CHG_CTIME = True
                self.CTIME = test[2]  
            test = param.partition("QMAX:")
            if test[1] != "":
                self.CHG_QMAX = True
                self.QMAX = test[2]                
            test = param.partition("EXPTIME:")
            if test[1] != "":
                self.CHG_EXPTIME = True
                self.EXPTIME = test[2] 
            test = param.partition("NOEXP:")
            if test[1] != "":
                self.CHG_NOEXP = True
                self.NOEXP = test[2] 
            test = param.partition("WEXPTIME:")
            if test[1] != "":
                self.CHG_WEXPTIME = True
                self.WEXPTIME = test[2] 
            test = param.partition("WNOEXP:")
            if test[1] != "":
                self.CHG_WNOEXP = True
                self.WNOEXP = test[2] 
    #def setFUSAXSmode(self,mode):
    	             
    def DeleteRow(self, parent):
        '''Tell parent to delete this row (may be tricky)
           @param parent: object of Tab that owns this Row'''
        self.tabCallback(self, 'delete')

    def SetPositions(self, parent):
        '''Tell parent to set positions on this row
           @param parent: object of Tab that owns this Row'''
        self.tabCallback(self, 'set')

    def Go(self, parent):
        '''Tell parent to move motors to this X,Y
           @param parent: object of Tab that owns this Row'''
        self.tabCallback(self, 'go')

# ################################
# ##  event handling routines  ###
# ################################    

    def OnDeleteButton(self, event):
        '''Delete button pressed
           @param event: wxPython event object'''
        self.DeleteRow(self.tab)

    def OnSetButton(self, event):
        '''Set button pressed
           @param event: wxPython event object'''
        self.SetPositions(self.tab)

    def OnGoButton(self, event):
        '''Go button pressed
           @param event: wxPython event object'''
        self.Go(self.tab)
    
    def OnAdvancedButton(self, event):
        '''More button pressed
            @param event: wxPython event object'''
        self.properties = USAXSproperties(self, -1, self.GetLabel())
        self.properties.ShowModal()
        #save properties locally
        self.doUSAXS = self.properties.doUSAXS.GetValue()
        self.CHG_NPTS = self.properties.CHG_NPTS.GetValue()
        self.NPTS = self.properties.NPTS.GetValue()
        self.CHG_CTIME = self.properties.CHG_CTIME.GetValue()
        self.CTIME = self.properties.CTIME.GetValue()
        self.CHG_QMAX = self.properties.CHG_QMAX.GetValue()
        self.QMAX = self.properties.QMAX.GetValue()
        self.doPinhole = self.properties.doPinhole.GetValue()
        self.CHG_EXPTIME = self.properties.CHG_EXPTIME.GetValue()
        self.EXPTIME = self.properties.EXPTIME.GetValue()
        self.CHG_NOEXP = self.properties.CHG_NOEXP.GetValue()
        self.NOEXP = self.properties.NOEXP.GetValue()
        self.doWAXS = self.properties.doWAXS.GetValue()
        self.CHG_WEXPTIME = self.properties.CHG_WEXPTIME.GetValue()
        self.WEXPTIME = self.properties.WEXPTIME.GetValue()
        self.CHG_WNOEXP = self.properties.CHG_WNOEXP.GetValue()
        self.WNOEXP = self.properties.WNOEXP.GetValue()

        if self.properties.SETALL.GetValue():
            self.tabCallback(self, 'setall')
        
        self.properties.Destroy()               
