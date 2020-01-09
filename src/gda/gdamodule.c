#include <pygobject.h>
#include <libgda/libgda.h>

/* These functions are auto-generated in gda.c */
void pygda_register_classes (PyObject*);
void pygda_add_constants(PyObject *module, const gchar *strip_prefix);
extern PyMethodDef pygda_functions[];

DL_EXPORT (void)
initgda (void) {
    PyObject *m, *d;
    PyObject *av = 0;
    int argc, i = 0;
    char **argv = 0;

    init_pygobject();

    /* initialise gda, for which we need the argc and argv command-line arguments: */
    /* This is based on code I found in pygtk/gtk/gtkmodule.c. murrayc */
    av = PySys_GetObject("argv");
    if (av != NULL) {
	if (!PyList_Check(av)) {
	    PyErr_Warn(PyExc_Warning, "ignoring sys.argv: it must be a list of strings");
	    av = NULL;
	} else {
	    argc = PyList_Size(av);
	    for (i = 0; i < argc; i++)
		if (!PyString_Check(PyList_GetItem(av, i))) {
		    PyErr_Warn(PyExc_Warning, "ignoring sys.argv: it must be a list of strings");
		    av = NULL;
		    break;
		}
	}
    }
    if (av != NULL) {
	argv = g_new(char *, argc);
	for (i = 0; i < argc; i++)
	    argv[i] = g_strdup(PyString_AsString(PyList_GetItem(av, i)));
    } else {
	    argc = 0;
	    argv = NULL;
    }

    gda_init();



    m = Py_InitModule ("gda", pygda_functions);\
    d = PyModule_GetDict (m);

    pygda_register_classes (d);
    pygda_add_constants (m, "GDA_");

    if (PyErr_Occurred()) {
    	Py_FatalError ("Can't initialise gda module");
    }
}
