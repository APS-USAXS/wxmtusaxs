#!/usr/bin/env python

#*************************************************************************
# Copyright (c) 2009-2010 The University of Chicago, as Operator of Argonne
#     National Laboratory.
# Copyright (c) 2009-2010 The Regents of the University of California, as
#     Operator of Los Alamos National Laboratory.
# This file is distributed subject to a Software License Agreement found
# in the file LICENSE that is included with this distribution. 
#*************************************************************************

'''
configuration for the distutils installation method

########### SVN repository information ###################
# $Date: 2013-10-27 10:40:32 -0500 (Sun, 27 Oct 2013) $
# $Author: jemian $
# $Revision: 860 $
# $URL: https://subversion.xray.aps.anl.gov/small_angle/USAXS/wxmtusaxs/trunk/setup.py $
# $Id: setup.py 860 2013-10-27 15:40:32Z jemian $
########### SVN repository information ###################

  for more help, see:
  http://wiki.python.org/moin/Distutils/Tutorial
  http://www.py2exe.org/index.cgi/Tutorial
  http://www.linux.com/feature/118439
  http://wiki.python.org/moin/Distutils

'''

import wxmtxy_version
import pydoc
from distutils.core import setup


graphics_dir = "graphics"
graphics = [
	"graphics/delete.bmp",
	"graphics/set.bmp",
	"graphics/go.bmp"
]

examples_dir = "examples"
examples = [
	"examples/USAXS_XY.xml",
	"examples/standard-paddle.txt",
	"examples/test-settings.xml"
]
data_files = [
	(examples_dir, examples),
	(graphics_dir, graphics),
	('.', 'LICENSE')
]
packages = []
scripts = [
    'wxmtxy.py',
    'wxmtxy_root.py',
    'wxmtxy_pair.py',
    'wxmtxy_tab.py',
    'wxmtxy_row.py',
    'wxmtxy_xml.py',
    'wxmtxy_pvsetup.py',
    'wxmtxy_axis.py',
    'wxmtxy_version.py',
    'wxmtxy_htmlview.py',
    'pvConnect.py'
]
py2exe_options = {
    "compressed": 1,
    "optimize": 2,
    "ascii": 1,
    "bundle_files": 1
}
# write the Python documentation to HTML files
pydoc.writedocs('.')

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.name = wxmtxy_version.__target_name__
        self.version = wxmtxy_version.__version__
        self.company_name = wxmtxy_version.__company_name__
        self.copyright = wxmtxy_version.__copyright__
        self.license = wxmtxy_version.__license__


# see: http://wiki.python.org/moin/Distutils/Tutorial
setup(
    name = wxmtxy_version.__target_name__,
    version = wxmtxy_version.__version__,
    description = wxmtxy_version.__summary__,
    long_description = wxmtxy_version.__long_description__,
    author = wxmtxy_version.__author__,
    author_email = wxmtxy_version.__author_email__,
    license = wxmtxy_version.__license__,
    url = wxmtxy_version.__url__,
    scripts = scripts,
    data_files = data_files,
)
