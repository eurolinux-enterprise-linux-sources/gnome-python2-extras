BUILDDIR = $(top_builddir)/docs/gtkspell

REF_VERSION = $(GNOME_PYTHON_EXTRAS_MAJOR_VERSION).$(GNOME_PYTHON_EXTRAS_MINOR_VERSION)
FULL_VERSION = $(REF_VERSION).$(GNOME_PYTHON_EXTRAS_MICRO_VERSION)

HTML_STYLE = $(PYGOBJECT_DATADIR)/pygobject/xsl/ref-html-style.xsl
PDF_STYLE = $(PYGOBJECT_DATADIR)/pygobject/xsl/pdf-style.xsl

XMLFILES =			\
	gtkspell-classes.xml	\
	gtkspell-gtkspell.xml

HTMLdir = $(datadir)/gtk-doc/html/pygtkspell
HTML_DATA =					\
	html/class-gtkspell.html		\
	html/gtkspell-class-reference.html	\
	html/pygtkspell.devhelp		        \
	html/index.html				\
	html/index.sgml

CSS_FILES = $(PYGOBJECT_PYGDOCS)/style.css
CSSdir = $(HTMLdir)
CSS_DATA = $(CSS_FILES)

BUILT_SOURCES = 	\
	build_stamp	\
	builddate.xml	\
	$(HTML_DATA)

CLEANFILES = 		\
	build_stamp	\
	builddate.xml	\
	$(HTML_DATA)

EXTRA_DIST = 		\
	$(XMLFILES) 	\
	$(XSLFILES)	\
	$(FIX_XREF)

REFERENCE_DEPS = 	\
	$(XMLFILES)	\
	$(XSLFILES)

$(HTML_DATA): build_stamp

if ENABLE_DOCS

builddate.xml: $(REFERENCE_DEPS)
	$(PYTHON) -c 'import datetime; print datetime.date.today()' > $@

build_stamp: $(REFERENCE_DEPS)builddate.xml
	xsltproc --nonet --xinclude -o $(BUILDDIR)/html/ \
		 --path $(BUILDDIR):$(srcdir)/gtkspell \
                 --stringparam gtkdoc.bookname "pygtkspell" \
                 --stringparam gtkdoc.version ${REF_VERSION} \
                 $(HTML_STYLE) $(srcdir)/gtkspell/gtkspell-classes.xml
	$(PYGOBJECT_FIXXREF) -i /usr/share/gtk-doc/html/pygtk/ $(BUILDDIR)/html/
	touch $@
endif
