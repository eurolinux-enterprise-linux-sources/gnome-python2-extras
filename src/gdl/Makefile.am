AUTOMAKE_OPTIONS=1.7

INCLUDES = $(PYTHON_INCLUDES) $(GDL_CFLAGS)

EXTRA_DIST = gdl.defs gdl.override

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

# gdl module
pkgpyexec_LTLIBRARIES = gdl.la
gdl_la_LDFLAGS = -module -avoid-version -export-symbols-regex initgdl
gdl_la_LIBADD = $(GDL_LIBS)
gdl_la_SOURCES = gdlmodule.c 
nodist_gdl_la_SOURCES = gdl.c
gdl.c: gdl.defs gdl.override
CLEANFILES = gdl.c

.defs.c:
	(cd $(srcdir)\
	 && $(PYGTK_CODEGEN) \
		--override $*.override \
	    $(PYGTK_CODEGEN_DEFINES) \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --register $(PYGTK_DEFSDIR)/pango-types.defs \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
		--prefix py$* $*.defs) > gen-$*.c \
	    && cp gen-$*.c $*.c \
	    && rm -f gen-$*.c
