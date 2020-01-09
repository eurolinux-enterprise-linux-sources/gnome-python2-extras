/* -*- Mode: C; c-basic-offset: 4 -*- */
#include <Python.h>
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif
#include <libgtkhtml/gtkhtml.h>

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>

void pygtkhtml2_register_classes(PyObject *d);
extern PyMethodDef pygtkhtml2_functions[];

DL_EXPORT(void)
initgtkhtml2 (void)
{
	PyObject *m, *d;

	init_pygobject ();

	/* gtkhtml2 calls this lazily, but only if you create a
	 * context first.  We call it to avoid segfaulting */
	html_atom_list_initialize();

	m = Py_InitModule ("gtkhtml2", pygtkhtml2_functions);
	d = PyModule_GetDict (m);

	pygtkhtml2_register_classes (d);
}
