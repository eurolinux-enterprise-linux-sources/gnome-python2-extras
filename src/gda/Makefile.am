INCLUDES = $(PYTHON_INCLUDES) $(PYGTK_CFLAGS)

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = gda.defs

EXTRA_DIST = $(defs_DATA)

#Install these utility function headers:
pkgincludedir = $(includedir)/pygda-4.0
pkginclude_HEADERS = pygdavalue_conversions.h

#Let other software discover the location of these headers:
pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = \
	pygda-4.0.pc



common_ldflags = -module -avoid-version -no-undefined

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

#common_ldflags = -module -avoid-version

# libgda binding
if BUILD_GDA
pkgpyexec_LTLIBRARIES = gda.la
endif

gda_la_CFLAGS = $(GDA_CFLAGS)

# We want to export the utility functions too:
gda_la_LDFLAGS = $(common_ldflags)
# gda_la_LDFLAGS = $(common_ldflags) -export-symbols-regex initgda

gda_la_LIBADD = $(GDA_LIBS) $(PYTHON_LDFLAGS)
gda_la_SOURCES = gdamodule.c pygdavalue_conversions.c pygdavalue_conversions.h gdaglue.h

argtypesdir = $(datadir)/pygtk/2.0/argtypes
argtypes_PYTHON = gda-arg-types.py

nodist_gda_la_SOURCES = gda.c
CLEANFILES = gda.c
EXTRA_DIST += gda.override
gda.c: gda.defs gda.override $(argtypes_PYTHON)


# generic rule
.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --load-types gda-arg-types.py \
	    --register gda.defs \
	    --override $*.override \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c

if PLATFORM_WIN32
# Python .pyd modules are simply DLLs, but they have to be called .pyd for
# python to find them, and libtool only creates .dll.
install-exec-hook:
	mv $(pkgpyexecdir)/gda.dll $(pkgpyexecdir)/gda.pyd
endif
