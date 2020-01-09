INCLUDES = -I$(top_srcdir) $(PYTHON_INCLUDES) $(GTKSPELL_CFLAGS)

common_ldflags = -module -avoid-version

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

pkgpyexec_LTLIBRARIES = gtkspell.la

gtkspell_la_SOURCES = gtkspellmodule.c
gtkspell_la_LDFLAGS = $(common_ldflags) $(GTKSPELL_LIBS) -export-symbols-regex initgtkspell
