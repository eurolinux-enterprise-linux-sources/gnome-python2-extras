# require automake-1.7
AUTOMAKE_OPTIONS=1.7

INCLUDES = $(PYTHON_INCLUDES)

EXTRA_DIST = gksu.defs gksu.override gksuui.defs gksuui.override

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

gksudir = $(pkgpyexecdir)/gksu
gksu_PYTHON = __init__.py

gksu_LTLIBRARIES =
CLEANFILES = 

if BUILD_GKSU
  gksu_LTLIBRARIES += _gksu.la
endif

if BUILD_GKSUUI
  gksu_LTLIBRARIES += ui.la
endif

# _gksu module
_gksu_la_LDFLAGS = -module -avoid-version -export-symbols-regex init_gksu
_gksu_la_LIBADD = $(GKSU_LIBS)
_gksu_la_CFLAGS = $(GKSU_CFLAGS)
_gksu_la_SOURCES = gksumodule.c 
nodist__gksu_la_SOURCES = gksu.c
gksu.c: gksu.defs gksu.override
CLEANFILES += gksu.c

# ui module
ui_la_LDFLAGS = -module -avoid-version -export-symbols-regex initui
ui_la_LIBADD = $(GKSUUI_LIBS)
ui_la_CFLAGS = $(GKSUUI_CFLAGS)
ui_la_SOURCES = gksuuimodule.c 
nodist_ui_la_SOURCES = gksuui.c
gksuui.c: gksuui.defs gksuui.override
CLEANFILES += gksuui.c


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
