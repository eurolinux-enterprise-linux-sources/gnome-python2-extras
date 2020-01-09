## Process this file with automake to produce Makefile.in

## libeggrecent
noinst_LTLIBRARIES = libeggrecent.la

libeggrecent_la_LIBADD = $(EGG_RECENT_LIBS)

libeggrecent_la_CFLAGS = \
	$(EGG_RECENT_CFLAGS)		\
	-DEGG_COMPILATION

libeggrecent_la_SOURCES =		\
	egg-recent.h			\
	egg-recent-item.h		\
	egg-recent-item.c		\
	egg-recent-model.c		\
	egg-recent-model.h		\
	egg-recent-view.c		\
	egg-recent-view.h		\
	egg-recent-view-gtk.c		\
	egg-recent-view-gtk.h		\
	egg-recent-view-bonobo.c	\
	egg-recent-view-bonobo.h	\
	egg-recent-view-uimanager.c	\
	egg-recent-view-uimanager.h	\
	egg-recent-util.c		\
	egg-recent-util.h

egg_public_h_sources =  \
	egg-recent.h			\
	egg-recent-item.h		\
	egg-recent-model.h		\
	egg-recent-view.h		\
	egg-recent-view-gtk.h		\
	egg-recent-view-bonobo.h


## python wrapper module
pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0
pyeggdir = $(pkgpythondir)/egg
pyeggexecdir = $(pkgpyexecdir)/egg


pyeggexec_LTLIBRARIES = recent.la
recent_la_LIBADD = libeggrecent.la

recent_la_CFLAGS =				\
	$(PYTHON_INCLUDES)			\
	$(PYGTK_CFLAGS)				\
	$(EGG_RECENT_CFLAGS)

recent_la_LDFLAGS = -module -avoid-version -export-symbols-regex initrecent
recent_la_SOURCES = eggrecentmodule.c
nodist_recent_la_SOURCES = eggrecent.c
CLEANFILES = eggrecent.c
EXTRA_DIST = eggrecent.override eggrecent.defs
eggrecent.c: eggrecent.defs eggrecent.override



.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --override $*.override \
	    --load-types $(GNOME_PYTHON_ARGTYPES_DIR)/bonobo-arg-types.py \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --register $(GNOME_PYTHON_DEFSDIR)/bonobo-types.defs \
	    --register $(GNOME_PYTHON_DEFSDIR)/bonoboui-types.defs \
	    --register $(GNOME_PYTHON_DEFSDIR)/ui.defs \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c


BUILT_SOURCES = eggtypebuiltins.h

eggtypebuiltins.h: stamp-eggtypebuiltins.h
	@true

DISTCLEANFILES = stamp-eggtypebuiltins.h eggtypebuiltins.c eggtypebuiltins.h

stamp-eggtypebuiltins.h: $(egg_public_h_sources) Makefile
	( cd $(srcdir) && glib-mkenums \
			--fhead "#ifndef __EGG_TYPE_BUILTINS_H__\n#define __EGG_TYPE_BUILTINS_H__\n\n#include <glib-object.h>\n\nG_BEGIN_DECLS\n" \
			--fprod "/* enumerations from \"@filename@\" */\n" \
			--vhead "GType @enum_name@_get_type (void);\n#define EGG_TYPE_@ENUMSHORT@ (@enum_name@_get_type())\n" \
			--ftail "G_END_DECLS\n\n#endif /* __EGG_TYPE_BUILTINS_H__ */" \
		$(egg_public_h_sources) ) >> xgen-gtbh \
	&& (cmp -s xgen-gtbh eggtypebuiltins.h || cp xgen-gtbh eggtypebuiltins.h ) \
	&& rm -f xgen-gtbh \
	&& echo timestamp > $(@F)
eggtypebuiltins.c: $(egg_public_h_sources) Makefile
	( cd $(srcdir) && glib-mkenums \
			--fhead "#include \"egg-recent.h\"\n#include \"egg-recent-item.h\"\n#include \"egg-recent-model.h\"\n#include \"egg-recent-view.h\"\n#include \"egg-recent-view-bonobo.h\"\n#include \"egg-recent-view-gtk.h\"" \
			--fprod "\n/* enumerations from \"@filename@\" */" \
			--vhead "GType\n@enum_name@_get_type (void)\n{\n  static GType etype = 0;\n  if (etype == 0) {\n    static const G@Type@Value values[] = {" \
			--vprod "      { @VALUENAME@, \"@VALUENAME@\", \"@valuenick@\" }," \
			--vtail "      { 0, NULL, NULL }\n    };\n    etype = g_@type@_register_static (\"@EnumName@\", values);\n  }\n  return etype;\n}\n" \
		$(egg_public_h_sources) ) > xgen-gtbc \
	&& cp xgen-gtbc eggtypebuiltins.c  \
	&& rm -f xgen-gtbc

libeggrecent_la_SOURCES += eggtypebuiltins.c eggtypebuiltins.h

