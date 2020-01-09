/* PyGkSu2 - Python bindings for GkSu2.
   Copyright (C) 2007 - Gian Mario Tagliaretti <gianmt@gnome.org>
   
   This program is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public License
   as published by the Free Software Foundation;
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU Lesser General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
*/

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <pygobject.h>
#include <pygtk/pygtk.h>
 
void pygksu2_register_classes (PyObject *d);
void pygksu2_add_constants(PyObject *module, const gchar *strip_prefix);
extern PyMethodDef pygksu2_functions[];
 
DL_EXPORT (void)
init_gksu2 (void)
{
    init_pygtk();    
    PyObject *m, *d;
    
    m = Py_InitModule ("_gksu2", pygksu2_functions);
    d = PyModule_GetDict (m);
    
    init_pygobject ();
    
    pygksu2_register_classes (d);
	pygksu2_add_constants(m, "GKSU_");
    
    if (PyErr_Occurred ())
        Py_FatalError ("can't initialise module gksu2");
}
