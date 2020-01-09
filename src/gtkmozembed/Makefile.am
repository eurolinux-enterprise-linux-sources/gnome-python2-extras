# require automake-1.5
AUTOMAKE_OPTIONS = 1.5

INCLUDES = $(PYTHON_INCLUDES) $(PYGTK_CFLAGS) $(GTKMOZEMBED_CFLAGS)

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = gtkmozembed.defs

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

# gtkmozembed module
pkgpyexec_LTLIBRARIES = gtkmozembed.la
gtkmozembed_la_LDFLAGS = -module -avoid-version	\
	-export-symbols-regex initgtkmozembed	\
	-R$(MOZILLA_HOME) -L$(MOZILLA_HOME)
gtkmozembed_la_LIBADD = $(GTKMOZEMBED_LIBS)
gtkmozembed_la_SOURCES = gtkmozembedmodule.c
nodist_gtkmozembed_la_SOURCES = gtkmozembed.c
gtkmozembed.c: gtkmozembed.defs gtkmozembed.override
CLEANFILES = gtkmozembed.c
EXTRA_DIST = gtkmozembed.override gtkmozembed.defs

.defs.c:
	(cd $(srcdir)\
	 && $(PYGTK_CODEGEN) \
	    $(GTKMOZEMBED_CODEGEN_DEFINES) \
	    --override $*.override \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c

