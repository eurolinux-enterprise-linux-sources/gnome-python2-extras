# require automake-1.7
AUTOMAKE_OPTIONS=1.7

INCLUDES = $(PYTHON_INCLUDES)

EXTRA_DIST = gksu2.defs gksu2.override

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

gksu2dir = $(pkgpyexecdir)/gksu2
gksu2_PYTHON = __init__.py

gksu2_LTLIBRARIES =
CLEANFILES = 

if BUILD_GKSU2
  gksu2_LTLIBRARIES += _gksu2.la
endif


# _gksu2 module
_gksu2_la_LDFLAGS = -module -avoid-version -export-symbols-regex init_gksu2
_gksu2_la_LIBADD = $(GKSU2_LIBS)
_gksu2_la_CFLAGS = $(GKSU2_CFLAGS)
_gksu2_la_SOURCES = gksu2module.c 
nodist__gksu2_la_SOURCES = gksu2.c
gksu2.c: gksu2.defs gksu2.override
CLEANFILES += gksu2.c

.defs.c:
	(cd $(srcdir)\
	 && $(PYGTK_CODEGEN) \
		--override $*.override \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --register $(PYGTK_DEFSDIR)/pango-types.defs \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
		--prefix py$* $*.defs) > gen-$*.c \
	    && cp gen-$*.c $*.c \
	    && rm -f gen-$*.c
