## Process this file with automake to produce Makefile.in

SUBDIRS =

if BUILD_EGGTRAY
  SUBDIRS += tray
endif

if BUILD_EGGRECENT
  SUBDIRS += recent
endif

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

pyeggdir = $(pkgpythondir)/egg
pyegg_PYTHON = __init__.py


