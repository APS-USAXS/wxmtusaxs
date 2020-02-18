#!/usr/bin/env python

# full contents of __file_license__ appear at the top of each file
__file_license__ = '''
#*************************************************************************
# Copyright (c) 2009-2010 The University of Chicago, as Operator of Argonne
#     National Laboratory.
# Copyright (c) 2009-2010 The Regents of the University of California, as
#     Operator of Los Alamos National Laboratory.
# This file is distributed subject to a Software License Agreement found
# in the file LICENSE that is included with this distribution. 
#*************************************************************************
'''

'''
version information for wxmtusaxs

########### SVN repository information ###################
# $Date: 2013-10-27 10:40:32 -0500 (Sun, 27 Oct 2013) $
# $Author: jemian $
# $Revision: 860 $
# $URL: https://subversion.xray.aps.anl.gov/small_angle/USAXS/wxmtusaxs/trunk/wxmtusaxs_version.py $
# $Id: wxmtusaxs_version.py 860 2013-10-27 15:40:32Z jemian $
########### SVN repository information ###################
'''


__author__ = "Peter Beaucage and Pete R. Jemian"
__author_email__ = "pbeaucage@aps.anl.gov"
__contributor_credits__ = [
       "",
       "other contributors:",
       "Geoff Savage/FNAL and John Hammonds/APS for CaChannel", 
       "Tim Mooney/APS for ca_util"]
__company_name__ = "Advanced Photon Source"
__version__ = "0.5"
__copyright__ = "(c) 2009, 2010"
#fp = open('LICENSE', 'r')
#__license__ = fp.read()
#fp.close()
__license__ = "APS extensions license.  See LICENSE file for details"
__long_description__ = '''wxmtusaxs is an EPICS GUI tool to assist users in operation of the USAXS instrument sample positioner''' 
__main_script__ = "wxmtusaxs.py"
__summary__ = "wxmtusaxs: a GUI for usaxs.mac"
__target_name__ = "wxmtusaxs"
__url__ = "https://subversion.xor.aps.anl.gov/trac/bcdaext/wiki/wxmtusaxs"
__urlsvn__ = "https://subversion.xor.aps.anl.gov/bcdaext/wxmtusaxs"
__svndesc__ = 'wxmtusaxs SVN repo page'
__documentation__ = '''
    *wxmtusaxs* is a modification to *wxmtusaxs*, which provides support for an X,Y     positioner (motor) pair by allowing users to define a table of known positi     ons and providing a one-button click to drive a chosen X,Y pair to a specif     ic table setting.  Also can record current position into a setting.
    
     *wxmtusaxs* introduces the ability to export to a usaxs.mac spec macro, a
     simplified user interface, and the ability to record a thickness for each
     row/sample, to be used in later absolute intensity calculation.
'''

