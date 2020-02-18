#!/usr/bin/env python
#Boa:Frame:root

#*************************************************************************
# Copyright (c) 2009-2010 The University of Chicago, as Operator of Argonne
#     National Laboratory.
# Copyright (c) 2009-2010 The Regents of the University of California, as
#     Operator of Los Alamos National Laboratory.
# This file is distributed subject to a Software License Agreement found
# in the file LICENSE that is included with this distribution. 
#*************************************************************************

'''wxmtusaxs_root: Define the GUI elements and interface (this is the main code)

########### SVN repository information ###################
# $Date: 2017-06-15 10:03:36 -0500 (Thu, 15 Jun 2017) $
# $Author: jemian $
# $Revision: 1410 $
# $URL: https://subversion.xray.aps.anl.gov/small_angle/USAXS/wxmtusaxs/trunk/wxmtusaxs_root.py $
# $Id: wxmtusaxs_root.py 1410 2017-06-15 15:03:36Z jemian $
########### SVN repository information ###################

@note: for an undo example, see: http://wiki.wxpython.org/AnotherTutorial
'''


import os, datetime, copy, inspect, wx
from wx.lib.wordwrap import wordwrap
import wxmtusaxs_pair
import wxmtusaxs_tab
import wxmtusaxs_row
import wxmtusaxs_xml
import wxmtusaxs_pvsetup
import wxmtusaxs_version
import wxmtusaxs_htmlview
from wxmtusaxs_strings import USAXSStrings, SAXSStrings


def create(parent):
    '''created by Boa-constructor'''
    return root(parent)

#################################
###       added methods       ###
#################################


[wxID_ROOT, wxID_ROOTPAGEBOOK, wxID_ROOTSTATUSBAR1, 
] = [wx.NewId() for _init_ctrls in range(3)]

[wxID_ROOTMENUFILECLOSE, wxID_ROOTMENUFILEEXIT, wxID_ROOTMENUFILEEXPORT, 
 wxID_ROOTMENUFILEIMPORT, wxID_ROOTMENUFILENEW, wxID_ROOTMENUFILEOPEN, 
 wxID_ROOTMENUFILEPREFERENCES, wxID_ROOTMENUFILESAVE, wxID_ROOTMENUFILESAVEAS,
wxID_ROOTMENUFILEEXPORTUSAXS, wxID_ROOTMENUFILEEXPORTSAXS,
] = [wx.NewId() for _init_coll_menuFile_Items in range(11)]

[wxID_ROOTMENUABOUTABOUT, wxID_ROOTMENUABOUTHELP, 
] = [wx.NewId() for _init_coll_menuAbout_Items in range(2)]

 
[wxID_ROOTMENUPAGECHOICECHANGETABTITLE, 
 wxID_ROOTMENUPAGECHOICEDELETETAB, wxID_ROOTMENUPAGECHOICENEWROW, 
 wxID_ROOTMENUPAGECHOICENEWTAB, 
] = [wx.NewId() for _init_coll_menuPage_Items in range(4)]

[wxID_ROOTMENUPAGECHOICECHANGEPAIRTITLE, 
 wxID_ROOTMENUPAGECHOICEDELETEPAIR, 
wxID_ROOTMENUPAGECHOICEEPICSCONFIG, 
 wxID_ROOTMENUPAGECHOICENEWPAIR, 
] = [wx.NewId() for _init_coll_menuStaff_Items in range(4)]

[wxID_TOOLBARNEWTAB, 
 wxID_TOOLBARCHANGETABTITLE, 
wxID_TOOLBARDELETETAB, 
 wxID_TOOLBARSAVE,
 wxID_TOOLBAREXPORTUSAXS, 
  wxID_TOOLBAREXPORTSAXS,
 wxID_TOOLBARNEWROW, 
] = [wx.NewId() for _init_coll_toolbar_Items in range(7)]

class root(wx.Frame):
    '''wxmtusaxs: Define the GUI elements and interface'''

    # see:  http://wiki.wxpython.org/BoaFAQ    
    _custom_classes = {'wx.Panel': ['XYpair']} 

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'File')
        parent.Append(menu=self.menuEdit, title=u'Edit')
        parent.Append(menu=self.menuPage, title=u'Page')
        parent.Append(menu=self.menuAbout, title=u'About')
        parent.Append(menu=self.menuStaff, title=u'Staff')

    def _init_coll_menuStaff_Items(self, parent):
        parent.Append(help='Create settings for a new X,Y pair of EPICS motors',
              id=wxID_ROOTMENUPAGECHOICENEWPAIR, kind=wx.ITEM_NORMAL,
              text='Create New X,Y pair\tCtrl+p')
        parent.Append(help=u'Delete settings for a new X,Y pair of EPICS motors',
              id=wxID_ROOTMENUPAGECHOICEDELETEPAIR, kind=wx.ITEM_NORMAL,
              text='Delete this X,Y pair\tCtrl+Shift+p')
        parent.Append(help=u'Change the title for this X,Y pair',
              id=wxID_ROOTMENUPAGECHOICECHANGEPAIRTITLE, kind=wx.ITEM_NORMAL,
              text='Change X,Y pair title\tCtrl+Shift+m')
        parent.AppendSeparator()
        parent.Append(help='Configure the EPICS PVs for this X,Y pair',
              id=wxID_ROOTMENUPAGECHOICEEPICSCONFIG, kind=wx.ITEM_NORMAL,
              text=u'EPICS configuration')
        parent.AppendSeparator()
        parent.Append(help=u'Import Row data (label, x, y) from a tab-separated file',
              id=wxID_ROOTMENUFILEIMPORT, kind=wx.ITEM_NORMAL,
              text=u'Import Rows ...\tCtrl+i')
        parent.Append(help=u'Export Row data (label, x, y) to a tab-separated file',
              id=wxID_ROOTMENUFILEEXPORT, kind=wx.ITEM_NORMAL,
              text=u'Export Rows ...\tCtrl+e')
        parent.Append(help='Manage the program defaults',
              id=wxID_ROOTMENUFILEPREFERENCES, kind=wx.ITEM_NORMAL,
              text='Preferences ...\tAlt+p')
        parent.AppendSeparator()
        self.Bind(wx.EVT_MENU, self.OnMenuPageChoicenewpairMenu,
              id=wxID_ROOTMENUPAGECHOICENEWPAIR)
        self.Bind(wx.EVT_MENU, self.OnMenuPageChoicedeletepairMenu,
              id=wxID_ROOTMENUPAGECHOICEDELETEPAIR)
        self.Bind(wx.EVT_MENU, self.OnMenuPageChoicechangetitleMenu,
              id=wxID_ROOTMENUPAGECHOICECHANGEPAIRTITLE)
        self.Bind(wx.EVT_MENU, self.OnMenuPageChoiceepicsconfigMenu,
              id=wxID_ROOTMENUPAGECHOICEEPICSCONFIG)        
        self.Bind(wx.EVT_MENU, self.OnMenuFilePreferencesMenu,
              id=wxID_ROOTMENUFILEPREFERENCES)
        self.Bind(wx.EVT_MENU, self.OnMenuFileExportMenu,
              id=wxID_ROOTMENUFILEEXPORT)
        self.Bind(wx.EVT_MENU, self.OnMenuFileImportMenu,
              id=wxID_ROOTMENUFILEIMPORT)
    def _init_coll_menuPage_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='Create a new tab of settings for this X,Y pair of EPICS motors',
              id=wxID_ROOTMENUPAGECHOICENEWTAB, kind=wx.ITEM_NORMAL,
              text='Create new tab\tCtrl+t')
        parent.Append(help='Delete this tab of settings for this X,Y pair of EPICS motors',
              id=wxID_ROOTMENUPAGECHOICEDELETETAB, kind=wx.ITEM_NORMAL,
              text='Delete tab\tCtrl+Shift+t')
        parent.Append(help='', id=wxID_ROOTMENUPAGECHOICECHANGETABTITLE,
              kind=wx.ITEM_NORMAL, text='Change tab title\tCtrl+m')
        parent.AppendSeparator()
        parent.Append(help='Create a new row for settings for this X,Y pair of EPICS motors',
              id=wxID_ROOTMENUPAGECHOICENEWROW, kind=wx.ITEM_NORMAL,
              text='Create new row\tCtrl+r')
        self.Bind(wx.EVT_MENU, self.OnMenuPageChoicenewrowMenu,
              id=wxID_ROOTMENUPAGECHOICENEWROW)
        self.Bind(wx.EVT_MENU, self.OnMenuPageChoicenewtabMenu,
              id=wxID_ROOTMENUPAGECHOICENEWTAB)
        self.Bind(wx.EVT_MENU, self.OnMenuPageChoicedeletetabMenu,
              id=wxID_ROOTMENUPAGECHOICEDELETETAB)
        self.Bind(wx.EVT_MENU, self.OnMenuPageChoicechangetabtitleMenu,
              id=wxID_ROOTMENUPAGECHOICECHANGETABTITLE)

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        #parent.Append(help=u'Create a new set', id=wxID_ROOTMENUFILENEW,
        #      kind=wx.ITEM_NORMAL, text=u'New\tCtrl+n')
        parent.Append(help=u'Open a configuration file',
              id=wxID_ROOTMENUFILEOPEN, kind=wx.ITEM_NORMAL,
              text=u'Open ...\tCtrl+o')
        parent.Append(help=u'Close the current file', id=wxID_ROOTMENUFILECLOSE,
              kind=wx.ITEM_NORMAL, text=u'Close\tCtrl+w')
        parent.AppendSeparator()
        parent.Append(help=u'Record the settings to the current file',
              id=wxID_ROOTMENUFILESAVE, kind=wx.ITEM_NORMAL,
              text=u'Save\tCtrl+s')
        parent.Append(help=u'Choose a file to record the settings',
              id=wxID_ROOTMENUFILESAVEAS, kind=wx.ITEM_NORMAL,
              text=u'Save As ...\tCtrl+Shift+s')
        parent.AppendSeparator()
        parent.Append(help=u'Export usaxs.mac file',
	      id=wxID_ROOTMENUFILEEXPORTUSAXS, kind=wx.ITEM_NORMAL,
	      text=u'Export usaxs macro ...\tCtrl+Shift+e')
        parent.Append(help=u'Export saxs.py file',
          id=wxID_ROOTMENUFILEEXPORTSAXS, kind=wx.ITEM_NORMAL,
          text=u'Export saxs Python ...\tCtrl+Alt+Shift+e')
	parent.AppendSeparator()
        parent.Append(help=u'Quit the wxmtusaxs application',
              id=wxID_ROOTMENUFILEEXIT, kind=wx.ITEM_NORMAL, text=u'Exit')
        self.Bind(wx.EVT_MENU, self.OnMenuFileExitMenu,
              id=wxID_ROOTMENUFILEEXIT)
        # 2018-04-21,prj:  remove ^W due to user mistake
	# self.Bind(wx.EVT_MENU, self.OnMenuFileCloseMenu,
        #       id=wxID_ROOTMENUFILECLOSE)
        self.Bind(wx.EVT_MENU, self.OnMenuFileNewMenu, id=wxID_ROOTMENUFILENEW)
        self.Bind(wx.EVT_MENU, self.OnMenuFileOpenMenu,
              id=wxID_ROOTMENUFILEOPEN)
        self.Bind(wx.EVT_MENU, self.OnMenuFileSaveMenu,
              id=wxID_ROOTMENUFILESAVE)
        self.Bind(wx.EVT_MENU, self.OnMenuFileSaveasMenu,
              id=wxID_ROOTMENUFILESAVEAS)
        self.Bind(wx.EVT_MENU, self.OnMenuFileExportUsaxsMenu,
	      id=wxID_ROOTMENUFILEEXPORTUSAXS)
        self.Bind(wx.EVT_MENU, self.OnMenuFileExportSaxsMenu,
          id=wxID_ROOTMENUFILEEXPORTSAXS)

    def _init_coll_menuAbout_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Not ready yet', id=wxID_ROOTMENUABOUTHELP,
              kind=wx.ITEM_NORMAL, text=u'Help')
        parent.Append(help=u'General information about wxmtusaxs',
              id=wxID_ROOTMENUABOUTABOUT, kind=wx.ITEM_NORMAL,
              text=u'About ...')
        self.Bind(wx.EVT_MENU, self.ShowAbout, id=wxID_ROOTMENUABOUTABOUT)
        self.Bind(wx.EVT_MENU, self.OnMenuAboutHelpMenu,
              id=wxID_ROOTMENUABOUTHELP)

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'status')

        parent.SetStatusWidths([-1])

    def _init_coll_toolbar_Items(self, parent):

        parent.AddLabelTool(wxID_TOOLBARNEWTAB, 'New Tab',wx.ArtProvider.GetBitmap(wx.ART_NEW),wx.NullBitmap,0,'New Tab')
        parent.AddLabelTool(wxID_TOOLBARCHANGETABTITLE, 'Change Tab Title',wx.Bitmap('graphics/rename.png'),wx.NullBitmap,0,'Change Current Tab Title')
        parent.AddLabelTool(wxID_TOOLBARDELETETAB, 'Delete Current Tab',wx.ArtProvider.GetBitmap(wx.ART_DELETE),wx.NullBitmap,0,'Delete Current Tab')
        parent.AddSeparator();
        parent.AddLabelTool(wxID_TOOLBARSAVE, 'Save',wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE),wx.NullBitmap,0,'Save Settings')
        parent.AddLabelTool(wxID_TOOLBAREXPORTUSAXS, 'Export usaxs.mac',wx.Bitmap('graphics/export.png'),wx.NullBitmap,0,'Export Current Tab as usaxs.mac')
        #parent.AddLabelTool(wxID_TOOLBAREXPORTSAXS, 'Export saxs.py',wx.Bitmap('graphics/export.png'),wx.NullBitmap,0,'Export Current Tab as saxs.py')
        parent.AddSeparator();
        parent.AddLabelTool(wxID_TOOLBARNEWROW, 'New Row', wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW),wx.NullBitmap,0,'Create new sample row')
        self.Bind(wx.EVT_TOOL, self.OnMenuPageChoicenewtabMenu,
              id=wxID_TOOLBARNEWTAB)
        self.Bind(wx.EVT_TOOL, self.OnMenuPageChoicedeletetabMenu,
              id=wxID_TOOLBARDELETETAB)
        self.Bind(wx.EVT_TOOL, self.OnMenuPageChoicechangetabtitleMenu,
              id=wxID_TOOLBARCHANGETABTITLE)
        self.Bind(wx.EVT_TOOL, self.OnMenuFileSaveMenu,
              id=wxID_TOOLBARSAVE)
        self.Bind(wx.EVT_TOOL, self.OnMenuFileExportUsaxsMenu,
          id=wxID_TOOLBAREXPORTUSAXS)
        self.Bind(wx.EVT_TOOL, self.OnMenuFileExportSaxsMenu,
          id=wxID_TOOLBAREXPORTSAXS)        
        self.Bind(wx.EVT_TOOL, self.OnMenuPageChoicenewrowMenu,
              id=wxID_TOOLBARNEWROW)
        
        #self.Create(self,parent,1)
    def _init_utils(self):
        # generated method, don't edit
        self.menuFile = wx.Menu(title='')

        self.menuEdit = wx.Menu(title='')

        self.menuPage = wx.Menu(title='')

        self.menuStaff = wx.Menu(title='')

        self.menuAbout = wx.Menu(title='')

        self.menuBar1 = wx.MenuBar()
        
        toolbar = self.CreateToolBar()

        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuStaff_Items(self.menuStaff)
        self._init_coll_menuPage_Items(self.menuPage)
        self._init_coll_menuAbout_Items(self.menuAbout)
        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_toolbar_Items(toolbar)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_ROOT, name=u'root', parent=prnt,
              pos=wx.Point(312, 25), size=wx.Size(500, 504),
              style=wx.DEFAULT_FRAME_STYLE, title=u'wxmtusaxs')
        self._init_utils()
        self.SetClientSize(wx.Size(568, 470))
        self.SetMinSize(wx.Size(568, 550))
        self.SetMenuBar(self.menuBar1)
        
        self.statusBar1 = wx.StatusBar(id=wxID_ROOTSTATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.pagebook = wx.Notebook(id=wxID_ROOTPAGEBOOK, name=u'pagebook',
              parent=self, pos=wx.Point(80, 0), size=wx.Size(488, 427), style=0)
        self.pagebook.SetToolTipString(u'Each "page" describes a different X,Y pair of EPICS motors')

    def __init__(self, parent, settingsFile = None):
        '''This is the main application window and class.
            @param parent: object that owns this window
            @param settingsFile: [string] name of the XML file'''
        self.paircounter = 0  # incrementing index to create page names
        self._init_ctrls(parent)
        self.title = self.GetTitle()
        self._dirty(False)    # settings need to be saved to a file if True
        self.pwd = os.getcwd()
        self.settingsFile = settingsFile
        if self.settingsFile == None:
            self.NewPair()        # by default, make a starting space
        else:
            self.SetStatusText('opening: %s' % self.settingsFile)
            self.OpenSettingsFile(self.settingsFile)
        # disable these menu items until they are implemented
        #self.menuAbout.FindItemById(wxID_ROOTMENUABOUTHELP).Enable(False)
        self.menuStaff.FindItemById(wxID_ROOTMENUFILEEXPORT).Enable(False)
        self.menuStaff.FindItemById(wxID_ROOTMENUFILEPREFERENCES).Enable(False)


# ################################
# ##       added methods       ###
# ################################

    def PairHandler(self, thePair, theTab, theRow, command):
        '''Callback function to handle a command from a pair
            @param thePair: wxmtusaxs_pair.XYpair object
            @param theTab: wxmtusaxs_tab.Tab object
            @param theRow: wxmtusaxs_row.Row object
            @param command: [string] action from Row button'''
        commandSet = ['delete', 'set', 'go', 'stop']
        if command not in commandSet:
            self.SetStatusText('Unknown command: %s' % command)
            return
        if command == 'delete':
            self.DeleteRow(thePair, theTab, theRow)
        if command == 'set':
            self.SetRow(thePair, theTab, theRow)
        if command == 'go':
            self.GoRow(thePair, theTab, theRow)
        if command == 'stop':
            self.StopPair(thePair)

    def _dirty(self, state=True):
        '''Declare the settings dirty (means that changes are unsaved)
            @param state: [Boolean] True means there are unsaved changes'''
        self.dirty = state
        title = self.title
        if state == True:
            title = '* ' + title + ' *'
        self.SetTitle(title)

    def NewPair(self, newtab=True):
        '''Create a page for a new X,Y pair
            @param newtab: [Boolean] option to create a first tab'''
        self.paircounter += 1   # unique for each new page
        name = 'panel' + repr(self.paircounter)
        text = 'pair ' + repr(self.paircounter)
        panel = wxmtusaxs_pair.XYpair(name=name, parent=self.pagebook,
                   root=self, rootCallback=self.PairHandler, newtab=newtab)
        self.pagebook.AddPage(imageId=-1, page=panel, select=True, text=text)
        panel.SetPageTitle(text)
        self.SetStatusText('Created page titled: %s' % text)
        self.Layout()
        self._dirty()
        return panel

    def GetPairText(self, pairnum):
        '''@param pairnum: [int] index number of the XY_pair
            @return: text of the pair numbered pairnum'''
        return self.pagebook.GetPageText(pairnum)

    def SetPairText(self, pairnum, text):
        '''set the text of the pair numbered pairnum
            @param pairnum: [int] index number of the XY_pair
            @param text: [string] name of the XYpair'''
        self.pagebook.SetPageText(pairnum, text)
        panel = self.pagebook.GetPage(pairnum)
        panel.SetPageTitle(text)

    def DeletePairnum(self, pairnum):
        '''Delete the selected X,Y pair and settings
            @param pairnum: [int] index number of the XY_pair'''
        try:
            self.pagebook.DeletePage(pairnum)
        except:
            self.SetStatusText('Could not delete that pair')

    def GetEpicsConfig(self, pairnum):
        '''Return the EPICS PV configuration for the indexed X,Y pair
            @param pairnum: [int] index number of the XY_pair'''
        panel = self.pagebook.GetPage(pairnum)
        config = panel.GetEpicsConfig()
        return config

    def SetEpicsConfig(self, pairnum, config):
        '''Define the EPICS PVs for the indexed X,Y pair
            @param pairnum: [int] index number of the XY_pair
            @param config: Python dictionary of EPICS PV configuration'''
        panel = self.pagebook.GetPage(pairnum)
        panel.SetEpicsConfig(config)
        panel.ConnectEpics()

    def RequestConfirmation(self, command, text):
        '''Present a dialog asking user to confirm step
            @param command: [string] action to be confirmed
            @param text: [string] message to user'''
        # confirm this step
        self.SetStatusText('Request Confirmation')
        dlg = wx.MessageDialog(self, text, 
                'Confirm %s' % command, 
                wx.YES|wx.NO)
        result = dlg.ShowModal()
        dlg.Destroy()           # destroy first
        if result == wx.ID_YES:
            self.SetStatusText('accepted request: %s' % command)
        else:
            self.SetStatusText('canceled request: %s' % command)
        return result

    def DeleteRow(self, thePair, theTab, theRow):
        '''Process a 'delete' command from a row button
            @param thePair: wxmtusaxs_pair.XYpair object
            @param theTab: wxmtusaxs_tab.Tab object
            @param theRow: wxmtusaxs_row.Row object'''
        text = 'Delete row labeled: %s' % theRow.GetLabel()
        # confirm this step
        result = self.RequestConfirmation('Delete Row', text + '?')
        if result != wx.ID_YES:
            return
        self.SetStatusText(text)
        theTab.DeleteRow(theRow)
        self._dirty()

    def SetRow(self, thePair, theTab, theRow):
        '''Process a 'set' command from a row button
            @param thePair: wxmtusaxs_pair.XYpair object
            @param theTab: wxmtusaxs_tab.Tab object
            @param theRow: wxmtusaxs_row.Row object'''
        text = theRow.GetLabel()
        self.SetStatusText('Set X, Y on row labeled: %s' % text)
        x, y = thePair.GetRbvXY()
        theRow.SetXY(x, y)
        if len(theRow.GetLabel().strip()) == 0:
            t = datetime.datetime.now()
            yyyymmdd = t.strftime("%Y-%m-%d")
            hhmmss = t.strftime("%H:%M:%S")
            theRow.SetLabel(yyyymmdd + ',' + hhmmss)
        self._dirty()

    def GoRow(self, thePair, theTab, theRow):
        '''Process a 'go' command from a row button
            @param thePair: wxmtusaxs_pair.XYpair object
            @param theTab: wxmtusaxs_tab.Tab object
            @param theRow: wxmtusaxs_row.Row object'''
        text = theRow.GetLabel()
        self.SetStatusText('Move EPICS motors on row labeled: %s' % text)
        x_txt, y_txt = theRow.GetXY()
        try:
            x = float(x_txt)
            y = float(y_txt)
        except:
            self.SetStatusText('X or Y not a number, will not move')
            return
        # identify EPICS motors and send them the move commands
        thePair.MoveAxes(x, y)
        title = thePair.GetPageTitle()
        self.SetStatusText('Move %s to (%s, %s)' % (title, x_txt, y_txt))

    def StopPair(self, thePair):
        '''Process a 'stop' command from a stop button.
           Need to stop the two associated positioners.
            @param thePair: wxmtusaxs_pair.XYpair object'''
        thePair.StopAxes()
        title = thePair.GetPageTitle()
        self.SetStatusText('Stop ' + title)

    def ImportRows(self, rowfile):
        '''Import a row file into the current tab (make a tab if none exists)
            @param rowfile: [string] name of the 3-column tab-separated file'''
        self.SetStatusText('file: %s' % rowfile)
        try:
            fp = open(rowfile, 'r')
            buf = fp.read()
            fp.close()
        except:
            self.SetStatusText('Could not read file: %s' % rowfile)
            return
        #
        if self.pagebook.GetSelection() < 0:
            self.NewPair(newtab=False)  # need to make a new page
        pagenum = self.pagebook.GetSelection()
        pair = self.pagebook.GetPage(pagenum)
        if pair.GetSelection() < 0:
            pair.NewTab(newrow=False)
        tabnum = pair.GetSelection()
        tab = pair.table.GetPage(tabnum)
        linenum = 0
        for line in buf.strip().split('\n'):
            linenum += 1
            try:
                label, x, y = line.strip().split('\t')
                row = tab.NewRow()
                row.SetLabel(label)
                row.SetXY(x, y)
            except:
                self.SetStatusText('Problem with row: %d' % linenum)
        tab.Remap()     # adjust for changes

    def OpenSettingsFile(self, settingsFile):
        '''Open the named settings file and replace all the current settings
            @param settingsFile: [string] name of the XML file'''
        try:
            rc = wxmtusaxs_xml.Settings(settingsFile)
            result = rc.ReadXmlFile()
            if result != None:
                return result
        except:
            self.SetStatusText('Could not open: %s' % settingsFile)
            return
        # safe to proceed now
        self.SetStatusText('Opened: %s' % settingsFile)
        self.pagebook.DeleteAllPages()
        self.settingsFile = settingsFile
        selectedpairnum = rc.GetSelectedPair()
        for pairnum in range(rc.CountPairs()):
            pairnode = self.NewPair(newtab=False)
            self.SetPairText(pairnum, rc.GetPairTitle(pairnum))
            self.SetEpicsConfig(pairnum, rc.GetEpicsConfig(pairnum))
            selectedtabnum = rc.GetSelectedTab(pairnum)
            for tabnum in range(rc.CountTabs(pairnum)):
                tabnode = pairnode.NewTab(newrow=False)
                pairnode.SetTabText(tabnum, rc.GetTabTitle(pairnum, tabnum))
                selectedrownum = rc.GetSelectedRow(pairnum, tabnum)
                for rownum in range(rc.CountRows(pairnum, tabnum)):
                    label = rc.GetRowTitle(pairnum, tabnum, rownum)
                    x, y = rc.GetRowXY(pairnum, tabnum, rownum)
                    thickness = rc.GetRowThickness(pairnum,tabnum,rownum)
                    usaxsModeString = rc.GetRowUSAXSMode(pairnum, tabnum, rownum)
                    rownode = tabnode.NewRow()
                    rownode.SetLabel(label)
                    rownode.SetXY(x, y)
                    rownode.SetThickness(thickness)
                    rownode.SetUSAXSMode(usaxsModeString)
                tabnode.Remap()
                if selectedrownum >= 0:
                    # none of these work correctly in ScrolledPanel
                    #tabnode.ChangeSelection(selectedrownum)
                    #tabnode.Scroll(1, 1+selectedrownum*25)
                    #row = tabnode.sizer.GetItem(rownum).GetWindow()
                    #tabnode.ScrollChildIntoView(row)
                    pass
            if selectedtabnum >= 0:
                pairnode.table.ChangeSelection(selectedtabnum)
        if selectedpairnum >= 0:
            self.pagebook.ChangeSelection(selectedpairnum)
        self._dirty(False)

    def SaveSettingsFile(self, settingsFile):
        '''Save the current settings to the named settings file
            @param settingsFile: [string] name of the XML file'''
        rc = wxmtusaxs_xml.Settings(settingsFile)
        selectedpair = self.pagebook.GetSelection()
        for pairnum in range(self.pagebook.GetPageCount()):
            rc.NewPair(self.GetPairText(pairnum))
            if selectedpair == pairnum:
                rc.SelectPair(pairnum)
            pair = self.pagebook.GetPage(pairnum)
            config = self.GetEpicsConfig(pairnum)
            rc.SetEpicsConfig(pairnum, config)
            selectedtab = pair.GetSelection()
            for tabnum in range(pair.table.GetPageCount()):
                rc.NewTab(pairnum, pair.GetTabText(tabnum))
                if selectedtab == tabnum:
                    rc.SelectTab(pairnum, tabnum)
                tab = pair.table.GetPage(tabnum)
                #selectedrow = tab.GetSelection()
                for rownum in range(len(tab.GetChildren())):
                    rc.NewRow(pairnum, tabnum, tab.GetRowLabel(rownum))
                    x, y = tab.GetRowXY(rownum)
                    rc.SetRowXY(pairnum, tabnum, rownum, x, y)
                    thickness = tab.GetRowThickness(rownum)
                    rc.SetRowThickness(pairnum, tabnum, rownum, thickness)
                    usaxsModeString = tab.GetRowUSAXSMode(rownum)
                    rc.SetRowUSAXSMode(pairnum, tabnum, rownum, usaxsModeString)
        rc.SetSettingsFile(settingsFile)
        rc.SaveXmlFile()
        self.settingsFile = settingsFile
        self._dirty(False)

    def is_number(self,s):
    	try:
            float(s)
            return True
    	except ValueError:
            return False

    
    def SaveUsaxsMacro(self, settingsFile):
        '''Save the current tab to a USAXS spec macro
            @param settingsFile: [string] name of the file'''
        selectedpair = self.pagebook.GetSelection()
        pair = self.pagebook.GetPage(selectedpair)
        selectedtab = pair.GetSelection()
        tab = pair.table.GetPage(selectedtab)
        tabTitle = pair.GetTabText(selectedtab);

        stringSet = USAXSStrings()

        usaxsScanMacroHeader = stringSet.GetMacroHeaderPart1()
        usaxsScanMacroHeader = usaxsScanMacroHeader + 'CURRENT_EXPERIMENT_NAME "' + tabTitle + '"'
        usaxsScanMacroHeader = usaxsScanMacroHeader + stringSet.GetMacroHeaderPart2()

        usaxsSwitchover = stringSet.GetMacroUSAXSPinSwitch()

        usaxsScanMacroFooter = stringSet.GetMacroFooter()
    
        """ PAB -- fix requested by JIL to make generated macro human readable.
                    stores last parameters and does not repeat them if not needed.....
                    """
        lastExpTime = 0
        lastNumExp = 0
        lastUsaxsTime = 0
        lastNumPnts = 0
        lastFinish = 0
    
        macroFile = open(settingsFile,'w')
        macroFile.write(usaxsScanMacroHeader);
        for rownum in range(len(tab.GetChildren())):
            x, y = tab.GetRowXY(rownum);
            name = tab.GetRowLabel(rownum);
            thickness = tab.GetRowThickness(rownum);
            if thickness == "":
                thickness = "1"
            if tab.GetRowDoPinhole(rownum):
                if self.is_number(x) and self.is_number(y) and name != "":
                    if tab.GetRowExpTime(rownum) and tab.GetRowExpTime(rownum) != lastExpTime:
                    	macroFile.write("\n          set_PIN_EXP_TIME " + tab.GetRowExpTime(rownum) + "\n")
                    	lastExpTime = tab.GetRowExpTime(rownum)
                    if tab.GetRowNoExp(rownum) and tab.GetRowNoExp(rownum) != lastNumExp:
                    	macroFile.write("\n          set_PIN_NUMEXP " + tab.GetRowNoExp(rownum) + "\n")
                    	lastNumExp = tab.GetRowNoExp(rownum)
               	    macroFile.write("\n          saxsExp     " + x + "     " + y + "    " + thickness + "    \"" + name + "\"\n"); 
        #macroFile.write(usaxsSwitchover)
        macroFile.write("\n          #End of SAXS, next is WAXS  \n")
        for rownum in range(len(tab.GetChildren())):
            x, y = tab.GetRowXY(rownum);
            name = tab.GetRowLabel(rownum);
            thickness = tab.GetRowThickness(rownum);
            if thickness == "":
                thickness = "1"
            if tab.GetRowDoWAXS(rownum):
                if self.is_number(x) and self.is_number(y) and name != "":
                    if tab.GetRowWExpTime(rownum) and tab.GetRowWExpTime(rownum) != lastExpTime:
                        macroFile.write("\n          set_WAXS_EXP_TIME " + tab.GetRowWExpTime(rownum) + "\n")
                        lastExpTime = tab.GetRowWExpTime(rownum)
                    if tab.GetRowWNoExp(rownum) and tab.GetRowWNoExp(rownum) != lastNumExp:
                        macroFile.write("\n          set_WAXS_NUMEXP " + tab.GetRowWNoExp(rownum) + "\n")
                        lastNumExp = tab.GetRowWNoExp(rownum)
                    macroFile.write("\n          waxsExp     " + x + "     " + y + "    " + thickness + "    \"" + name + "\"\n"); 
        #macroFile.write(usaxsSwitchover)
  



	# If we are running any USAXS, insert a preUSAXStune before the first USAXS scan
	for rownum in range(len(tab.GetChildren())):
		if tab.GetRowDoUSAXS(rownum):
			macroFile.write("\n          #End of WAXS, next is USAXS  \n")
	    		macroFile.write("\n          preUSAXStune \n")
			break




        for rownum in range(len(tab.GetChildren())):
             x, y = tab.GetRowXY(rownum);
             name = tab.GetRowLabel(rownum);
             thickness = tab.GetRowThickness(rownum);
             if thickness == "":
                 thickness = "1"
             if tab.GetRowDoUSAXS(rownum):
                if self.is_number(x) and self.is_number(y) and name != "":
                    if tab.GetRowCountTime(rownum) and tab.GetRowCountTime(rownum)!= lastUsaxsTime:
                    	macroFile.write("\n          set_USAXS_TIME " + tab.GetRowCountTime(rownum) + "\n")
                    	lastUsaxsTime = tab.GetRowCountTime(rownum)
                    if tab.GetRowNumPts(rownum) and tab.GetRowNumPts(rownum) != lastNumPnts:
                    	macroFile.write("\n          set_NUMPNTS " + tab.GetRowNumPts(rownum) + "\n")
                    	lastNumPnts = tab.GetRowNumPts(rownum)
                    if tab.GetRowMaxQ(rownum) and tab.GetRowMaxQ(rownum) != lastFinish:
                    	macroFile.write("\n          set_FINISH " + tab.GetRowNumPts(rownum) + "\n")
                    	lastFinish = tab.GetRowMaxQ(rownum)
                    macroFile.write("\n          USAXSscan     " + x + "     " + y + "    " + thickness + "    \"" + name + "\"\n"); 
        macroFile.write(usaxsScanMacroFooter);
        macroFile.close(); 

    def PostNotice(self, title, message, flags):
        '''post a message dialog box
            @param title: [string] window title bar
            @param message: [string] message message text
            @param flags: dialog box flags (such as wx.OK | wx.ICON_INFORMATION)'''
        dlg = wx.MessageDialog(None, message, title, flags)
        dlg.ShowModal()
        dlg.Destroy()

# ################################
# ##  event handling routines  ###
# ################################

    def ShowAbout(self, event):
        '''describe this application
           @param event: wxPython event object'''
        # derived from http://wiki.wxpython.org/Using%20wxPython%20Demo%20Code
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = wxmtusaxs_version.__summary__
        info.Version = wxmtusaxs_version.__version__
        info.Copyright = wxmtusaxs_version.__copyright__
        description = ''
        for line in wxmtusaxs_version.__documentation__.strip().splitlines():
            item = line.strip()
            if len(item) > 0:
                description += ' ' + line.strip()
            else:
                description += '\n\n'
        info.Description = wordwrap(description, 400, wx.ClientDC(self))
        URL = wxmtusaxs_version.__url__
        info.WebSite = (URL, wxmtusaxs_version.__svndesc__)
        author = wxmtusaxs_version.__author__
        author += ", " + wxmtusaxs_version.__author_email__
        others = [ "author: ", author ]
        others.extend(wxmtusaxs_version.__contributor_credits__)
        info.Developers = others
        info.License = wxmtusaxs_version.__license__
        # Then we call wx.AboutBox giving it the info object
        wx.AboutBox(info)

    def OnMenuFileNewMenu(self, event):
        '''Requested new settings
           @param event: wxPython event object'''
        self.SetStatusText('Requested new settings')
        if self.dirty:
            # confirm this step
            result = self.RequestConfirmation('New',
                  'There are unsaved changes.  Create new settings anyway?')
            if result != wx.ID_YES:
                return
        self.pagebook.DeleteAllPages()
        self.NewPair()
        self._dirty(False)
        self.settingsFile = None

    def OnMenuFileOpenMenu(self, event):
        '''Requested to open XML settings file
           @param event: wxPython event object'''
        if self.dirty:
            # confirm this step
            result = self.RequestConfirmation('Open ...',
                  'There are unsaved changes.  Open anyway?')
            if result != wx.ID_YES:
                return
        #---
        self.SetStatusText('Requested to open XML settings file')
        wildcard = "XML files (*.xml)|*.xml|" \
                   "All files (*)|*"
        instruction = "Choose an XML file with full settings." \
            " (The selected file will be verified before it is loaded.)"
        dlg = wx.FileDialog(None, instruction, 
            self.pwd, "", wildcard, wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.pwd = os.path.dirname(dlg.GetPath())
            self.OpenSettingsFile(dlg.GetPath())
        dlg.Destroy()

    def OnMenuFileSaveMenu(self, event):
        '''Requested to save settings to XML file
           @param event: wxPython event object'''
        if self.settingsFile == None:
            self.OnMenuFileSaveasMenu(event)
        else:
            self.SaveSettingsFile(self.settingsFile)

    def OnMenuFileSaveasMenu(self, event):
        '''Requested to save settings to new XML file
           @param event: wxPython event object'''
        self.SetStatusText('Save current settings to XML file')
        wildcard = "XML files (*.xml)|*.xml|" \
                   "All files (*)|*"
        instruction = "Save current settings to XML file" \
            " (either existing or new)"
        dlg = wx.FileDialog(None, instruction, 
            self.pwd, "", wildcard, wx.SAVE|wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            self.pwd = os.path.dirname(filename)
            self.SaveSettingsFile(filename)
        dlg.Destroy()
        self._dirty(False)

    def OnMenuFileExportUsaxsMenu(self,event):
    	'''Requested to save current tab to a usaxs.mac file
    	   @param event: wxPython event object'''
    	self.SetStatusText('Export current tab to spec macro')
    	wildcard = "spec macros (*.mac)|*.mac|" \
    		   "All files (*) |*"
    	instruction = "Export current tab as USAXS spec macro"
    	now = datetime.datetime.now()
    	dlg=wx.FileDialog(None,instruction,"/share1/USAXS_data/"+str(now.year)+"-"+str(now.month).zfill(2)+"/","usaxs.mac",wildcard,wx.SAVE|wx.OVERWRITE_PROMPT)
    	if dlg.ShowModal() == wx.ID_OK:
    	   filename = dlg.GetPath()
    	   self.pwd = os.path.dirname(filename)
    	   self.SaveUsaxsMacro(filename)
    	dlg.Destroy()

    def OnMenuFileExportSaxsMenu(self,event):
        '''Requested to save current tab to a saxs.py file
       @param event: wxPython event object'''
        self.SetStatusText('Export current tab to spec macro')
        wildcard = "python files (*.py)|*.py|" \
               "All files (*) |*"
        instruction = "Export current tab as SAXS python script"
        now = datetime.datetime.now()
        dlg=wx.FileDialog(None,instruction,"/data/SAXS/"+str(now.year)+"-"+str(now.month).zfill(2)+"/","saxs.py",wildcard,wx.SAVE|wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
           filename = dlg.GetPath()
           self.pwd = os.path.dirname(filename)
           self.SaveSaxsMacro(filename)
        dlg.Destroy()

    def OnMenuFileCloseMenu(self, event):
        '''User requested to close the settings file
           @param event: wxPython event object'''
        if self.pagebook.GetPageCount() > 0:
            if self.dirty:
                # confirm this step
                result = self.RequestConfirmation('Close All',
                      'There are unsaved changes.  Close All anyway?')
                if result != wx.ID_YES:
                    return
            self.SetStatusText('Close All requested')
            self.pagebook.DeleteAllPages()
        else:
            self.SetStatusText('Nothing to close')
        self._dirty(False)

    def OnMenuFileImportMenu(self, event):
        '''user requested to import a table of settings from a file
           @param event: wxPython event object'''
        wildcard = "text files (*.txt)|*.txt|" \
                   "All files (*)|*"
        instruction = "Choose a file with row settings"
        dlg = wx.FileDialog(None, instruction, 
            self.pwd, "", wildcard, wx.OPEN)
            # what about changing self.pwd here?
        if dlg.ShowModal() == wx.ID_OK:
            self.pwd = os.path.dirname(dlg.GetPath())
            self.ImportRows(dlg.GetPath())
        dlg.Destroy()

    def OnMenuFileExportMenu(self, event):
        '''user requested to export a Tab
           @param event: wxPython event object
           @note: Not implemented yet'''
        event.Skip()

    def OnMenuFilePreferencesMenu(self, event):
        '''user requested to view/edit preferences
           @param event: wxPython event object
           @note: Not implemented yet'''
        self.SetStatusText('Requested to edit Preferences')
        self.PostNotice("Construction Zone!",
                "'Preferences ...' menu item not implemented yet.",
                wx.OK | wx.ICON_INFORMATION)

    def OnMenuFileExitMenu(self, event):
        '''User requested to quit the application
           @param event: wxPython event object'''
        if self.dirty:
            # confirm this step
            result = self.RequestConfirmation('Exit (Quit)',
                  'There are unsaved changes.  Exit (Quit) anyway?')
            if result != wx.ID_YES:
                return
        self.Close()

    def OnMenuPageChoicenewpairMenu(self, event):
        '''User requested a new X,Y pair
           @param event: wxPython event object'''
        self.NewPair()
        self._dirty()

    def OnMenuPageChoicedeletepairMenu(self, event):
        '''User requested to delete the X,Y pair
           @param event: wxPython event object'''
        pagenum = self.pagebook.GetSelection()
        if pagenum < 0:
            self.SetStatusText('no page to delete')
            return
        text = self.pagebook.GetPageText(pagenum)
        # confirm this step
        requestText = 'Delete X,Y page [%s]?' % text
        result = self.RequestConfirmation('Delete X,Y page?',
              requestText)
        if result == wx.ID_YES:
            self.DeletePairnum(pagenum)
            self.SetStatusText('page was deleted')
            self._dirty()

    def OnMenuPageChoicechangetitleMenu(self, event):
        '''User requested to change the page title
           @param event: wxPython event object'''
        pagenum = self.pagebook.GetSelection()
        if pagenum >= 0:
            self.SetStatusText('requested X,Y page name change')
            response = wx.GetTextFromUser(parent=self,
                message='Rename this page of settings:', 
                caption='Rename this page',
                default_value=self.pagebook.GetPageText(pagenum))
            if len(response) > 0:
                self.SetStatusText('New page title: %s' % response)
                self.SetPairText(pagenum, response)
                self._dirty()
            else:
                self.SetStatusText('Rename was canceled')
        else:
            self.SetStatusText('no page to rename')

    def OnMenuPageChoicenewtabMenu(self, event):
        '''user requested a new tab
           @param event: wxPython event object'''
        pagenum = self.pagebook.GetSelection()
        if pagenum < 0:
            self.SetStatusText('No pages now!  Cannot create a tab.')
            return      # early
        pair = self.pagebook.GetPage(pagenum)
        pair.NewTab()
        self.SetStatusText('Created new tab.')
        self._dirty()

    def OnMenuPageChoicedeletetabMenu(self, event):
        '''user requested to delete a tab
           @param event: wxPython event object'''
        pagenum = self.pagebook.GetSelection()
        if pagenum < 0:
            self.SetStatusText('No pages now!  Cannot delete a tab.')
            return      # early
        pair = self.pagebook.GetPage(pagenum)
        tabnum = pair.GetSelection()
        if tabnum < 0:
            self.SetStatusText('No tab to delete.')
            return
        text = pair.GetTabText(tabnum)
        # confirm this step
        requestText = 'Delete tab [%s]?' % text
        result = self.RequestConfirmation('Delete tab?',
              requestText)
        if result == wx.ID_YES:
            self.SetStatusText(pair.DeleteTab())
            self._dirty()

    def OnMenuPageChoicechangetabtitleMenu(self, event):
        '''user requested to rename tab
           @param event: wxPython event object'''
        pagenum = self.pagebook.GetSelection()
        if pagenum < 0:
            self.SetStatusText('No pages now!  Cannot rename a tab.')
            return      # early
        pair = self.pagebook.GetPage(pagenum)
        tabnum = pair.GetSelection()
        if tabnum < 0:
            self.SetStatusText('No tab to rename.')
            return
        text = pair.GetTabText(tabnum)
        self.SetStatusText('requested tab name change')
        response = wx.GetTextFromUser(parent=self,
            message='Rename this tab:', 
            caption='Rename this tab',
            default_value=text)
        if len(response) > 0:
            self.SetStatusText('New tab name: %s' % response)
            pair.SetTabText(tabnum, response)
            self._dirty()
        else:
            self.SetStatusText('Rename tab was canceled')

    def OnMenuPageChoicenewrowMenu(self, event):
        '''user requested to create a new row of settings in the current table
           @param event: wxPython event object'''
        pagenum = self.pagebook.GetSelection()
        if pagenum < 0:
            self.SetStatusText('No pages now!  Cannot create a row.')
            return      # early
        pair = self.pagebook.GetPage(pagenum)
        tabnum = pair.GetSelection()
        if tabnum < 0:
            self.SetStatusText('No tabs now!  Cannot create a row.')
            return
        tab = pair.table.GetPage(tabnum)
        tab.NewRow()
        tab.Remap()
        self.SetStatusText('Created new row.')
        self._dirty()

    def OnMenuAboutHelpMenu(self, event):
        '''user requested help
           @param event: wxPython event object
           @note: Not implemented yet'''
        self.SetStatusText('starting HTML Help Viewer ...')
        page = 'index.html'
        root_dir = os.path.split(inspect.getsourcefile(root))[0]
        fullname = os.path.join(root_dir, page)
        wxmtusaxs_htmlview.HtmlView(parent=None, 
            homepage=fullname, id=-1, 
            title='HtmlView: '+page).Show()

    def OnMenuPageChoiceepicsconfigMenu(self, event):
        '''user requested to view/change EPICS PV configuration
           @param event: wxPython event object'''
        self.SetStatusText('Modifying EPICS PV configuration details')
        pagenum = self.pagebook.GetSelection()
        if pagenum < 0:
            self.SetStatusText('No pages now!  Cannot modify EPICS PV configuration.')
            return      # early
        orig_cfg = copy.deepcopy(self.GetEpicsConfig(pagenum))
        dlg = wxmtusaxs_pvsetup.PvDialog(None, orig_cfg)
        try:
            result = dlg.ShowModal()
        finally:
            if result == wx.ID_OK:
                new_cfg = copy.deepcopy(dlg.GetConfiguration())
                # smarter way is to compare orig_cfg and new_fg
                self._dirty()
                self.SetEpicsConfig(pagenum, new_cfg)
            dlg.Destroy()
