/* -*- Mode: C; c-basic-offset: 4 -*- */

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>

void pyeggrecent_register_classes (PyObject *d);
void pyeggrecent_add_constants(PyObject *module, const gchar *strip_prefix);

extern PyMethodDef pyeggrecent_functions[];

DL_EXPORT(void)
initrecent(void)
{
    PyObject *m, *d;

    if (!g_thread_supported ())
        g_thread_init (NULL);
    init_pygobject();

    m = Py_InitModule("egg.recent", pyeggrecent_functions);
    d = PyModule_GetDict(m);

    pyeggrecent_register_classes(d);
    pyeggrecent_add_constants(m, "EGG_");

    PyErr_Warn(PyExc_DeprecationWarning, "the module egg.recent is deprecated;"
               " equivalent functionality can now be found in pygtk 2.10");
}
