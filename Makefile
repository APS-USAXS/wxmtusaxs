
# Makefile
#*************************************************************************
# Copyright (c) 2009-2010 The University of Chicago, as Operator of Argonne
#     National Laboratory.
# Copyright (c) 2009-2010 The Regents of the University of California, as
#     Operator of Los Alamos National Laboratory.
# This file is distributed subject to a Software License Agreement found
# in the file LICENSE that is included with this distribution. 
#*************************************************************************


########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################

HOST   := $(shell uname -n)
PYTHON := $(shell which python)
PYDOC := $(shell which pydoc)
ifeq ("$(HOST)", "como")
  # como runs cygwin
  # the python supplied with Cygwin does not have wx
  # wx is a package installed in Enthought Python
  PYTHON := /cygdrive/c/Python26/python.exe
endif
ifeq ("$(HOST)", "usaxscontrol.xor.aps.anl.gov")
  # usaxscontrol.xor.aps.anl.gov needs APSshare version
  PYTHON := /APSshare/bin/python
  PYDOC := /APSshare/bin/pydoc
endif
ifeq ("$(HOST)", "gov.aps.anl.gov")
  # gov.aps.anl.gov needs APSshare version
  PYTHON := /APSshare/bin/python
  PYDOC := /APSshare/bin/pydoc
endif


all :: sdist

rebuild :: clean all

clean ::
	/bin/rm -rf build/ dist/ MANIFEST *.pyc

sdist ::
	$(PYTHON) ./setup.py sdist

run ::
	$(PYTHON) ./wxmtxy.py

pydoc ::
	$(PYDOC) -w ./
	/bin/mv -f wxmtxy*.html pydoc/
	/bin/mv -f pvConnect.html pydoc/
	/bin/mv -f setup.html pydoc/
	/bin/mv -f menuLauncher.html pydoc/
