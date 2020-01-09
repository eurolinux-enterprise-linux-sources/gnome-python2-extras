/* PyGkSu - Python bindings for GkSu.
   Copyright (C) 2005 - Gian Mario Tagliaretti <g.tagliaretti@parafernalia.org>
   
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
 
void pygksuui_register_classes (PyObject *d); 
extern PyMethodDef pygksuui_functions[];
 
DL_EXPORT (void)
initui (void)
{
    PyObject *m, *d;
    
    m = Py_InitModule ("gksu.ui", pygksuui_functions);
    d = PyModule_GetDict (m);
    
    init_pygobject ();
    init_pygtk ();
    
    pygksuui_register_classes (d);
    
    if (PyErr_Occurred ())
        Py_FatalError ("can't initialise module gksu.ui");
}
