'''wxmtusaxs_properties: setup the advanced properties pane/window

########### SVN repository information ###################
# $Date: 2014-05-24 16:40:34 -0500 (Sat, 24 May 2014) $
# $Author: jemian $
# $Revision: 1017 $
# $URL: https://subversion.xray.aps.anl.gov/small_angle/USAXS/wxmtusaxs/trunk/wxmtusaxs_properties_josh.py $
# $Id: wxmtusaxs_properties_josh.py 1017 2014-05-24 21:40:34Z jemian $
########### SVN repository information ###################
'''

import wx

class USAXSproperties(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(310, 455))

        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
    
        #wx.StaticBox(panel, -1, 'USAXS', (5, 5), (300, 140))
	
        #self.doUSAXS = wx.CheckBox(panel, -1, 'Do USAXS Scan?', (15, 30))
	self.doUSAXS = wx.Menu('FlyScan/StepScan?', (15, 30))
	self.doUSAXS.Append('FlyScan')
	self.doUSAXS.Append('StepScan')
        #self.CHG_NPTS = wx.CheckBox(panel, -1, 'Set # of points to: ', (30, 55))
        #self.NPTS = wx.TextCtrl(panel, -1, '', (215, 55))      
        #self.CHG_CTIME = wx.CheckBox(panel, -1, 'Set count time (s) to: ', (30, 80))
        #self.CTIME = wx.TextCtrl(panel, -1, '', (215, 80))     
        #self.CHG_QMAX = wx.CheckBox(panel, -1, 'Set max q (A^-1) to: ', (30, 105))
        #self.QMAX = wx.TextCtrl(panel, -1, '', (215, 105))     
	#fly scan
	#self.doFUSAXS = wx.CheckBox(panel, -1, 'Do Fly Scan?', (15, 30))
	#self.param1 = wx.TextCtrl(panel, -1, '', (215, 55)) 
	#self.param2 = wx.TextCtrl(panel, -1, '', (215, 55)) 
	#self.param3 = wx.TextCtrl(panel, -1, '', (215, 55)) 
	#end

        wx.StaticBox(panel, -1, 'Pinhole SAXS', (5, 150), (300, 120))
        self.doPinhole = wx.CheckBox(panel, -1, 'Do Pinhole SAXS Exposure?', (15, 180))
        self.CHG_EXPTIME = wx.CheckBox(panel, -1, 'Set exposure time to: ', (30, 205))
        self.EXPTIME = wx.TextCtrl(panel, -1, '', (215, 205))     
        self.CHG_NOEXP = wx.CheckBox(panel, -1, 'Set # of exposures to: ', (30, 230))
        self.NOEXP = wx.TextCtrl(panel, -1, '', (215, 230))     
 
        wx.StaticBox(panel, -1, 'WAXS', (5, 295), (300, 120))
        self.doWAXS = wx.CheckBox(panel, -1, 'Do WAXS Exposure?', (15,325))
        self.CHG_WEXPTIME = wx.CheckBox(panel, -1, 'Set exposure time to: ', (30, 350))
        self.WEXPTIME = wx.TextCtrl(panel, -1, '', (215, 350))     
        self.CHG_WNOEXP = wx.CheckBox(panel, -1, 'Set # of exposures to: ', (30, 375))
        self.WNOEXP = wx.TextCtrl(panel, -1, '', (215, 375))     
       
        self.SETALL = wx.CheckBox(panel, -1, 'Use for all samples in this set?', (5,425))
        
        #fill in existing values
        try:
            self.doUSAXS.SetValue(parent.doUSAXS)
            self.CHG_NPTS.SetValue(parent.CHG_NPTS)
            self.NPTS.SetValue(parent.NPTS)
            self.CHG_CTIME.SetValue(parent.CHG_CTIME)
            self.CTIME.SetValue(parent.CTIME)        
            self.CHG_QMAX.SetValue(parent.CHG_QMAX)
            self.QMAX.SetValue(parent.QMAX) 
            self.doPinhole.SetValue(parent.doPinhole)
            self.CHG_EXPTIME.SetValue(parent.CHG_EXPTIME)
            self.EXPTIME.SetValue(parent.EXPTIME) 
            self.CHG_NOEXP.SetValue(parent.CHG_NOEXP)
            self.NOEXP.SetValue(parent.NOEXP) 
            self.doWAXS.SetValue(parent.doWAXS)
            self.CHG_WEXPTIME.SetValue(parent.CHG_WEXPTIME)
            self.WEXPTIME.SetValue(parent.WEXPTIME) 
            self.CHG_WNOEXP.SetValue(parent.CHG_WNOEXP)
            self.WNOEXP.SetValue(parent.WNOEXP) 
        except (AttributeError,UnboundLocalError):
            pass

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        #closeButton = wx.Button(self, -1, 'Done', size=(70, 30))
        #self.advanced.Bind(wx.EVT_BUTTON, self.OnAdvancedButton, id=wxID_ROWADVANCED)
        #hbox.Add(closeButton, 1, wx.CENTER, 5)

        vbox.Add(panel)
        vbox.Add(hbox, 1, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)

        self.SetSizer(vbox)
        
#    def OnDoneButton:(self,event)
        
