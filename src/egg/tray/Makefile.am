## Process this file with automake to produce Makefile.in

INCLUDES = $(PYTHON_INCLUDES) $(PYGTK_CFLAGS)  -DEGG_COMPILATION

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = trayicon.defs
EXTRA_DIST = $(defs_DATA)

common_ldflags = -module -avoid-version

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0
pyeggdir = $(pkgpythondir)/egg
pyeggexecdir = $(pkgpyexecdir)/egg


pyeggexec_LTLIBRARIES = trayicon.la
trayicon_la_CFLAGS = $(EGGTRAY_CFLAGS)
trayicon_la_LDFLAGS = $(common_ldflags) -export-symbols-regex inittrayicon
trayicon_la_LIBADD = $(EGGTRAY_LIBS)
trayicon_la_SOURCES = trayiconmodule.c eggtrayicon.c eggtrayicon.h
nodist_trayicon_la_SOURCES = trayicon.c
CLEANFILES = trayicon.c
EXTRA_DIST += trayicon.override  
trayicon.c: trayicon.defs trayicon.override

.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --override $*.override \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c
