INCLUDES = $(PYTHON_INCLUDES) $(PYGTK_CFLAGS)

defsdir = $(datadir)/pygtk/2.0/defs

defs_DATA = gtkhtml2.defs

EXTRA_DIST = $(defs_DATA)

common_ldflags = -module -avoid-version

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

# gtkhtml2 binding

if BUILD_GTKHTML2
pkgpyexec_LTLIBRARIES = gtkhtml2.la
endif
gtkhtml2_la_CFLAGS = $(GTKHTML2_CFLAGS)
gtkhtml2_la_LDFLAGS = $(common_ldflags) -export-symbols-regex initgtkhtml2
gtkhtml2_la_LIBADD = $(GTKHTML2_LIBS)
gtkhtml2_la_SOURCES = gtkhtml2module.c
nodist_gtkhtml2_la_SOURCES = gtkhtml2.c
CLEANFILES = gtkhtml2.c
EXTRA_DIST += gtkhtml2.override  
gtkhtml2.c: gtkhtml2.defs gtkhtml2.override

.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --override $*.override \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c
