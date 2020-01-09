SUBDIRS = tests

if BUILD_EGG
  SUBDIRS += egg
endif

if BUILD_GKSU
  SUBDIRS += gksu
endif

if BUILD_GKSU2
  SUBDIRS += gksu2
endif

if BUILD_GTKHTML2
  SUBDIRS += gtkhtml2
endif

if BUILD_GTKMOZEMBED
  SUBDIRS += gtkmozembed
if ENABLE_DOCS
  SUBDIRS += docs/gtkmozembed
endif
endif

if BUILD_GTKSPELL
  SUBDIRS += gtkspell
if ENABLE_DOCS
  SUBDIRS += docs/gtkspell
endif
endif

if BUILD_GDL
  SUBDIRS += gdl
endif

if BUILD_GDA
  SUBDIRS += gda
endif


pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = gnome-python-extras-2.0.pc

EXTRA_DIST = \
  MAINTAINERS \
  COPYING.GPL COPYING.LGPL \
  gnome-python-extras-2.0.pc.in \
  ltihooks.py \
  examples/egg/trayicon.py \
  examples/egg/recent/populate-recent.py \
  examples/egg/recent/gtk-view.py \
  examples/egg/recent/bonobo-view.py \
  examples/egg/recent/Bonobo_Sample_Hello.xml \
  examples/gksu2/simple.py \
  examples/gtkhtml2/simple-browser.py \
  examples/gtkspell/test.py \
  examples/gtkspell/spell.py \
  examples/gdl/gdl_test.py \
  examples/gdl/gdl_combo_button.py \
  examples/gdl/gdl_dock.py
