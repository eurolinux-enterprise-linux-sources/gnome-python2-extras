dnl -*- mode: autoconf -*-
AC_PREREQ(2.52)

dnl the gnome-python version number
m4_define(gnome_python_extras_major_version, 2)
m4_define(gnome_python_extras_minor_version, 25)
m4_define(gnome_python_extras_micro_version, 3)
m4_define(gnome_python_extras_version, gnome_python_extras_major_version.gnome_python_extras_minor_version.gnome_python_extras_micro_version)

dnl required versions of other packages
m4_define(pygtk_required_major_version, 2)
m4_define(pygtk_required_minor_version, 4)
m4_define(pygtk_required_micro_version, 0)
m4_define(pygtk_required_version, pygtk_required_major_version.pygtk_required_minor_version.pygtk_required_micro_version)
m4_define(glib_required_version,              2.6.0)
m4_define(gtk_required_version,               2.4.0)
m4_define(gnome_python_required_version,      2.10.0)
m4_define(gtkhtml2_required_version,          2.3.1)
m4_define(mozilla_required_version,           1.2b)
m4_define(firefox_required_version,           1.0)
m4_define(xulrunner_required_version,         1.8)
m4_define(libgda_required_version,            3.99.11)
m4_define(gksu_required_version,              1.2.5)
m4_define(gksu2_required_version,             2.0.4)
m4_define(gksuui_required_version,            1.0.3)

AC_INIT(gnome-python-extras, gnome_python_extras_version,
        [http://bugzilla.gnome.org/enter_bug.cgi?product=gnome-python])
dnl AC_CONFIG_SRCDIR([gnome/uimodule.c])
AM_CONFIG_HEADER(config.h)

AM_INIT_AUTOMAKE

AC_DEFINE(GNOME_PYTHON_EXTRAS_MAJOR_VERSION, gnome_python_extras_major_version,
                                            [Gnome-Python-Extras major version])
AC_DEFINE(GNOME_PYTHON_EXTRAS_MINOR_VERSION, gnome_python_extras_minor_version,
                                            [Gnome-Python-Extras minor version])
AC_DEFINE(GNOME_PYTHON_EXTRAS_MICRO_VERSION, gnome_python_extras_micro_version,
                                            [Gnome-Python-Extras macro version])

dnl AC_ARG_BINDING(NAME, DEFAULT [, MODULENAME])
AC_DEFUN([AC_ARG_BINDING],
[AC_ARG_ENABLE([$1],
             AC_HELP_STRING([--ifelse([$2], [YES], dis, en)able-[$1]],
                            [build ifelse([$3], , [$1], [$3]) bindings (default is [$2])]),
             [if test "$enable_[$1]" = "yes"; then 
	     		build_[$1]=true
			  else
				build_[$1]=false
			 fi])
])

GNOME_COMMON_INIT
AC_CANONICAL_HOST

dnl Copied from the official gtk+-2 configure.in
AC_MSG_CHECKING([for some Win32 platform])
case "$host" in
  *-*-mingw*|*-*-cygwin*)
    platform_win32=yes
    ;;
  *)
    platform_win32=no
    ;;
esac
AC_MSG_RESULT([$platform_win32])
AM_CONDITIONAL(PLATFORM_WIN32, test "$platform_win32" = "yes")

AC_MSG_CHECKING([for native Win32])
case "$host" in
  *-*-mingw*)
    os_win32=yes
    ;;
  *)
    os_win32=no
    ;;
esac
AC_MSG_RESULT([$os_win32])
AM_CONDITIONAL(OS_WIN32, test "$os_win32" = "yes")

AC_DISABLE_STATIC
AC_LIBTOOL_WIN32_DLL
AC_PROG_LIBTOOL

dnl check for python
AM_PATH_PYTHON(2.3)
AM_CHECK_PYTHON_HEADERS(,[AC_MSG_ERROR(could not find Python headers)])

dnl check for pygtk
PKG_CHECK_MODULES(PYGTK, pygtk-2.0 >= pygtk_required_version)
AC_SUBST(PYGTK_CFLAGS)
AC_PATH_PROG(PYGTK_CODEGEN, pygtk-codegen-2.0, no)
if test "x$PYGTK_CODEGEN" = xno; then
  AC_MSG_ERROR(could not find pygtk-codegen-2.0 script)
fi

AC_MSG_CHECKING([for conflicting pygtk versions])
pygtk_version=`$PKG_CONFIG --modversion pygtk-2.0`
case $pygtk_version in
     2.9.0|2.9.1)
        AC_MSG_RESULT([found $pygtk_version])
        AC_MSG_ERROR([invalid pygtk version found; please upgrade])
        ;;
     *)
        AC_MSG_RESULT([none])
        ;;
esac

AC_MSG_CHECKING(for pygtk defs)
PYGTK_DEFSDIR=`$PKG_CONFIG --variable=defsdir pygtk-2.0`
AC_SUBST(PYGTK_DEFSDIR)
AC_MSG_RESULT($PYGTK_DEFSDIR)

AC_MSG_CHECKING(for gnome-python defs)
GNOME_PYTHON_DEFSDIR=`$PKG_CONFIG --variable=defsdir gnome-python-2.0`
AC_SUBST(GNOME_PYTHON_DEFSDIR)
AC_MSG_RESULT($GNOME_PYTHON_DEFSDIR)

AC_MSG_CHECKING(for gnome-python argtypes dir)
GNOME_PYTHON_ARGTYPES_DIR=`$PKG_CONFIG --variable=argtypesdir gnome-python-2.0`
AC_SUBST(GNOME_PYTHON_ARGTYPES_DIR)
AC_MSG_RESULT($GNOME_PYTHON_ARGTYPES_DIR)

dnl get rid of the -export-dynamic stuff from the configure flags ...
export_dynamic=`(./libtool --config; echo eval echo \\$export_dynamic_flag_spec) | sh`

dnl check for glib
AM_PATH_GLIB_2_0(glib_required_version,,[AC_MSG_ERROR(maybe you want the gtk-gnome-1-2 branch?)],$extras_mods)
if test -n "$export_dynamic"; then
  GLIB_LIBS=`echo $GLIB_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl check to make sure we can find gtk
AM_PATH_GTK_2_0(gtk_required_version,,[AC_MSG_ERROR(maybe you want the gtk-gnome-1-2 branch?)],$extras_mods)
if test -n "$export_dynamic"; then
  GTK_LIBS=`echo $GTK_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl default bindings to build:
default_bindings_on="eggtray eggrecent gda gdl gksu gksu2 gtkhtml2 gtkmozembed gtkspell"
default_bindings_off=""
default_bindings_all="$default_bindings_on $default_bindings_off"

AC_ARG_ENABLE([allbindings],
             AC_HELP_STRING([--disable-allbindings],
                            [Changes all the bindings default values to be either enabled or disabled, overridden by any explicit bindings on the commandline.]),
             [if test "$enable_allbindings" = "no"; then
			   default_bindings_off="$default_bindings_all"
			   default_bindings_on=""
		  	 else
			   default_bindings_off=""
			   default_bindings_on="$default_bindings_all"
		     fi])
for binding in $default_bindings_on; do
	eval build_$binding=true
done
for binding in $default_bindings_off; do
	eval build_$binding=false
done

dnl Building documentation
AC_ARG_ENABLE(docs,
  AC_HELP_STRING([--enable-docs], [Enable documentation building]),enable_docs=$enableval,
  enable_docs=no)
if test "${enable_docs}" != no; then
  dnl Check for xsltproc
  AC_PATH_PROG([XSLTPROC], [xsltproc])
  if test -z "$XSLTPROC"; then
    enable_docs=no
  fi
fi

AM_CONDITIONAL(ENABLE_DOCS, test x$enable_docs != xno)

PYGOBJECT_INCLUDEDIR=`$PKG_CONFIG --variable=pygtkincludedir pygobject-2.0`
AC_SUBST(PYGOBJECT_INCLUDEDIR)

PYGOBJECT_DATADIR=`$PKG_CONFIG --variable=datadir pygobject-2.0`
AC_SUBST(PYGOBJECT_DATADIR)

PYGOBJECT_FIXXREF="$PYTHON `$PKG_CONFIG --variable=fixxref pygobject-2.0`"
AC_SUBST(PYGOBJECT_FIXXREF)

PYGOBJECT_PYGDOCS="`$PKG_CONFIG --variable=pygdocs pygobject-2.0`"
AC_SUBST(PYGOBJECT_PYGDOCS)

dnl should we build the gtkhtml2 module?
AC_ARG_BINDING([gtkhtml2], [ON])
if $build_gtkhtml2; then
  PKG_CHECK_MODULES(GTKHTML2, libgtkhtml-2.0 >= gtkhtml2_required_version,
    build_gtkhtml2=true,
    build_gtkhtml2=false)
fi
AC_SUBST(GTKHTML2_CFLAGS)
AC_SUBST(GTKHTML2_LIBS)
AM_CONDITIONAL(BUILD_GTKHTML2, $build_gtkhtml2)
if test -n "$export_dynamic"; then
  GTKHTML2_LIBS=`echo $GTKHTML2_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the egg.trayicon module?
AC_ARG_BINDING([eggtray], [ON], [egg.tray])
if $build_eggtray; then
  PKG_CHECK_MODULES(EGGTRAY, [gtk+-2.0 >= 2.2.0],
    build_eggtray=true,
    build_eggtray=false)
fi
AM_CONDITIONAL(BUILD_EGGTRAY, $build_eggtray)
if test -n "$export_dynamic"; then
  EGGTRAY_LIBS=`echo $EGGTRAY_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the egg.recent module?
AC_ARG_BINDING([eggrecent], [ON], [egg.recent])
if $build_eggrecent; then
  PKG_CHECK_MODULES(EGG_RECENT, [gtk+-2.0 >= 2.0.0 gnome-vfs-2.0
                                 libbonoboui-2.0 libgnomeui-2.0
                                 gnome-python-2.0 >= gnome_python_required_version],
    build_eggrecent=true,
    build_eggrecent=false)
fi
AM_CONDITIONAL(BUILD_EGGRECENT, $build_eggrecent)
if test -n "$export_dynamic"; then
  EGGRECENT_LIBS=`echo $EGGRECENT_LIBS | sed -e "s/$export_dynamic//"`
fi

AM_CONDITIONAL(BUILD_EGG, $build_eggrecent || $build_eggtray)

dnl should we build the gtkmozembed module?
AC_ARG_BINDING([gtkmozembed], [ON], [gtkmozembed])
AC_ARG_WITH(gtkmozembed, AS_HELP_STRING(
                         [--with-gtkmozembed=mozilla|firefox|xulrunner],
                         [package that provides libgtkmozembed]),
            [mozpackage=$withval], [mozpackage=any])

if "$build_gtkmozembed"; then
if test $mozpackage = any ; then

PKG_CHECK_MODULES(GTKMOZEMBED, [xulrunner-gtkmozembed >= xulrunner_required_version
                                gtk+-2.0              >= gtk_required_version],
  [build_gtkmozembed=true; mozpackage=xulrunner],
  [
PKG_CHECK_MODULES(GTKMOZEMBED, [firefox-gtkmozembed >= firefox_required_version
                                gtk+-2.0            >= gtk_required_version],
  [build_gtkmozembed=true; mozpackage=firefox],
  [
PKG_CHECK_MODULES(GTKMOZEMBED, [mozilla-gtkmozembed >= mozilla_required_version
                                gtk+-2.0            >= gtk_required_version],
  [build_gtkmozembed=true; mozpackage=mozilla],
  build_gtkmozembed=false)
  ])
  ])

else

case $mozpackage in
     xulrunner) mozpackage_required_version=xulrunner_required_version ;;
     firefox) mozpackage_required_version=firefox_required_version ;;
     mozilla)
         mozpackage_required_version=mozilla_required_version
         AC_MSG_CHECKING([for extra gtkmozembed code generation flags])
         PKG_CHECK_MODULES(XUL19, mozilla-gtkmozembed >= 0.21 gtk+-2.0,
                           GTKMOZEMBED_CODEGEN_DEFINES="-DHAVE_XUL19",
                           GTKMOZEMBED_CODEGEN_DEFINES="")
         AC_MSG_RESULT([$GTKMOZEMBED_CODEGEN_DEFINES])
         ;;
     *) AC_MSG_ERROR([--with-gtkmozembed argument must be either 'mozilla', 'firefox', or 'xulrunner'])
esac
AC_SUBST(GTKMOZEMBED_CODEGEN_DEFINES)

PKG_CHECK_MODULES(GTKMOZEMBED, [$mozpackage-gtkmozembed >= $mozpackage_required_version,
                                gtk+-2.0                >= gtk_required_version],
  build_gtkmozembed=true,
  build_gtkmozembed=false)

fi

AM_CONDITIONAL(BUILD_GTKMOZEMBED, $build_gtkmozembed)
if test -n "$export_dynamic"; then
  GTKMOZEMBED_LIBS=`echo $GTKMOZEMBED_LIBS | sed -e "s/$export_dynamic//"`
fi
MOZILLA_HOME="`$PKG_CONFIG --variable=libdir $mozpackage-gtkmozembed`"
if test -z "$MOZILLA_HOME"; then
   MOZILLA_HOME="`$PKG_CONFIG --variable=sdkdir $mozpackage-gtkmozembed`/lib"
fi
AC_SUBST(MOZILLA_HOME)

fi # if build_gtkmozembed

AM_CONDITIONAL(BUILD_GTKMOZEMBED, $build_gtkmozembed)
if test -n "$export_dynamic"; then
  GTKMOZEMBED_LIBS=`echo $GTKMOZEMBED_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the gtkspell module?
AC_ARG_BINDING([gtkspell], [ON])
if $build_gtkspell; then
  PKG_CHECK_MODULES(GTKSPELL, [gtkspell-2.0 >= 2.0.0 pygtk-2.0 >= pygtk_required_version],
    build_gtkspell=true,
    build_gtkspell=false)
fi
AM_CONDITIONAL(BUILD_GTKSPELL, $build_gtkspell)
if test -n "$export_dynamic"; then
  GTKSPELL_LIBS=`echo $GTKSPELL_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gdl module?
AC_ARG_BINDING([gdl], [ON])
if $build_gdl; then
  have_gdl07=false
  PKG_CHECK_MODULES(GDL, [gdl-1.0 >= 0.7.1 gdl-gnome-1.0 >= 0.7.1 pygtk-2.0 >= pygtk_required_version], dnl
                    [build_gdl=true; have_gdl07=true], build_gdl=false)

  dnl try again with no gnome and older version
  if ! $build_gdl; then
    PKG_CHECK_MODULES(GDL, [gdl-1.0 >= 0.6.1 pygtk-2.0 >= pygtk_required_version], dnl
                      build_gdl=true, build_gdl=false)
  fi
fi

AM_CONDITIONAL(BUILD_GDL, $build_gdl)
if test -n "$export_dynamic"; then
  GDL_LIBS=`echo $GDL_LIBS | sed -e "s/$export_dynamic//"`
fi

if $have_gdl07; then
  AC_DEFINE([HAVE_GDL_0_7], [], [If GDL >= 0.7 was found])
fi

AC_SUBST([PYGTK_CODEGEN_DEFINES])
if $have_gdl07; then
  PYGTK_CODEGEN_DEFINES="-DHAVE_GDL_0_7 $PYGTK_CODEGEN_DEFINES";
fi


dnl should we buuild the gda module?
AC_ARG_BINDING([gda], [ON])
if $build_gda; then
  PKG_CHECK_MODULES(GDA, [libgda-4.0 >= libgda_required_version pygtk-2.0 >= pygtk_required_version],
    build_gda=true,
    build_gda=false)
fi
AM_CONDITIONAL(BUILD_GDA, $build_gda)
if test -n "$export_dynamic"; then
  GDA_LIBS=`echo $GDA_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gksu2 module?
AC_ARG_BINDING([gksu2], [ON])
if $build_gksu2; then
  PKG_CHECK_MODULES(GKSU2, [libgksu2 >= gksu2_required_version
                           pygtk-2.0 >= pygtk_required_version
                           gtk+-2.0  >= gtk_required_version],
    build_gksu2=true,
    build_gksu2=false)
fi
AM_CONDITIONAL(BUILD_GKSU2, $build_gksu2)
if test -n "$export_dynamic"; then
  GKSU2_LIBS=`echo $GKSU2_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gksu module?
AC_ARG_BINDING([gksu], [ON])
if $build_gksu; then
  PKG_CHECK_MODULES(GKSU, [libgksu1.2 >= gksu_required_version
                           pygtk-2.0 >= pygtk_required_version],
    build_gksu=true,
    build_gksu=false)
fi
AM_CONDITIONAL(BUILD_GKSU, $build_gksu)
if test -n "$export_dynamic"; then
  GKSU_LIBS=`echo $GKSU_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gksu.ui module?
AC_ARG_BINDING([gksuui], [ON], [gksu.ui])
if $build_gksuui; then
  PKG_CHECK_MODULES(GKSUUI, [libgksuui1.0 >= gksuui_required_version
                             pygtk-2.0 >= pygtk_required_version],
    build_gksuui=true,
    build_gksuui=false)
fi
AM_CONDITIONAL(BUILD_GKSUUI, $build_gksuui)
if test -n "$export_dynamic"; then
  GKSUUI_LIBS=`echo $GKSUUI_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl add required cflags ...
JH_ADD_CFLAG([-Wall])
dnl commented because it causes compilation problems in egg/recent
dnl JH_ADD_CFLAG([-std=c9x])
JH_ADD_CFLAG([-fno-strict-aliasing])


AC_CONFIG_FILES(
  Makefile
  gtkhtml2/Makefile
  egg/Makefile
  egg/tray/Makefile
  egg/recent/Makefile
  gtkmozembed/Makefile
  gtkspell/Makefile
  gdl/Makefile
  gda/Makefile
  gda/pygda-4.0.pc
  gksu2/Makefile
  gksu/Makefile
  gnome-python-extras-2.0.pc
  tests/Makefile
  docs/gtkmozembed/Makefile
  docs/gtkspell/Makefile
  docs/gtkmozembed/entities.docbook
  docs/gtkspell/entities.docbook
)
AC_OUTPUT

echo
echo "The following modules will be built:"
echo
$build_gtkhtml2          && echo     gtkhtml2
$build_eggtray           && echo     egg.trayicon
$build_eggrecent         && echo     egg.recent
$build_gtkmozembed       && echo     gtkmozembed	"(linking to $mozpackage)"
$build_gtkspell          && echo     gtkspell
$build_gdl               && echo     gdl
$build_gda               && echo     gda
$build_gksu2             && echo     gksu2
$build_gksu              && echo     gksu
$build_gksuui            && echo     gksu.ui
echo

echo "The following modules will NOT be built:"
echo
$build_gtkhtml2          || echo     gtkhtml2
$build_eggtray           || echo     egg.trayicon
$build_eggrecent         || echo     egg.recent
$build_gtkmozembed       || echo     gtkmozembed
$build_gtkspell          || echo     gtkspell
$build_gdl               || echo     gdl
$build_gda               || echo     gda
$build_gksu2             || echo     gksu2
$build_gksu              || echo     gksu
$build_gksuui            || echo     gksu.ui
