#!/usr/bin/python

#   Copyright (C) 2007 - Gian Mario Tagliaretti <g.tagliaretti@parafernalia.org>
#   
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation;
#   
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   
#   You should have received a copy of the GNU Lesser General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import pygtk
pygtk.require("2.0")
import gdl
import gtk

def combo_button_activate_default_cb (combo):
    print "combo_button_activate_default_cb"

window = gtk.Window (gtk.WINDOW_TOPLEVEL)
window.connect ("delete_event", gtk.main_quit)
window.set_title ("Combo button test")
window.set_resizable (False)

hbox = gtk.HBox (False, 0)
window.add (hbox)

combo = gtk.Button (None, gtk.STOCK_OPEN)
combo.set_relief (gtk.RELIEF_NONE)
hbox.pack_start (combo, False, False, 0)

menu = gtk.Menu ()
menuitem = gtk.ImageMenuItem (gtk.STOCK_OPEN, None)
menu.append (menuitem)
menuitem = gtk.ImageMenuItem (gtk.STOCK_SAVE, None)
menu.append (menuitem)
menu.show_all ()

combo = gdl.ComboButton ()
combo.set_label ("Run")
combo.set_menu (menu)

icon = combo.render_icon (gtk.STOCK_EXECUTE, gtk.ICON_SIZE_LARGE_TOOLBAR)
combo.set_icon (icon)
hbox.pack_start (combo, False, False, 0)

combo.connect ("activate_default", combo_button_activate_default_cb)

combo = gtk.Button (None, gtk.STOCK_SAVE)
combo.set_relief (gtk.RELIEF_NONE)
hbox.pack_start (combo, False, False, 0)

menu = gtk.Menu ()
menuitem = gtk.ImageMenuItem (gtk.STOCK_OPEN, None)
menu.append (menuitem)
menuitem = gtk.ImageMenuItem (gtk.STOCK_SAVE, None)
menu.append (menuitem)
menu.show_all ()

combo = gdl.ComboButton ()
combo.set_label ("Open")
combo.set_menu (menu)

icon = combo.render_icon (gtk.STOCK_OPEN, gtk.ICON_SIZE_LARGE_TOOLBAR)
combo.set_icon (icon)
combo.set_sensitive (False)
hbox.pack_start (combo, False, False, 0)

combo.connect ("activate_default", combo_button_activate_default_cb)

menu = gtk.Menu ()
combo = gdl.ComboButton ()
combo.set_label ("Open")
combo.set_menu (menu)

icon = combo.render_icon (gtk.STOCK_OPEN, gtk.ICON_SIZE_LARGE_TOOLBAR)
combo.set_icon (icon)
hbox.pack_start (combo, False, False, 0)

window.show_all ()

gtk.main ()
