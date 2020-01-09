#!/usr/bin/python
# -*- coding: latin-1 -*-

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

import gtk
import gdl

def create_text_item():
    vbox1 = gtk.VBox (False, 0)

    scrolledwindow1 = gtk.ScrolledWindow ()
    
    vbox1.pack_start (scrolledwindow1, True, True, 0)
    scrolledwindow1.set_policy (gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    scrolledwindow1.set_shadow_type (gtk.SHADOW_ETCHED_IN)
    text = gtk.TextView ()
    text.props.wrap_mode = gtk.WRAP_WORD
    scrolledwindow1.add (text)

    return vbox1

def create_item(title):
    vbox1 = gtk.VBox (False, 0)

    button1 = gtk.Button (title)
    vbox1.pack_start (button1, True, True, 0)

    return vbox1

def save_layout_cb (widget, layout):
    dialog = gtk.Dialog ("New Layout",
			 None,
			 gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
			 (gtk.STOCK_OK, gtk.RESPONSE_OK))

    hbox = gtk.HBox (False, 8)
    hbox.set_border_width (8)
    
    vbox = dialog.get_child ()
    vbox.pack_start (hbox, False, False, 0)

    label = gtk.Label ("Name:")
    hbox.pack_start (label, False, False, 0)
	
    entry = gtk.Entry ()
    hbox.pack_start (entry, True, True, 0)

    hbox.show_all ()
    response = dialog.run ()

    if response == gtk.RESPONSE_OK:
	name = entry.get_text ()
	layout.save_layout (name)
    else:
	dialog.destroy ()

def run_layout_manager_cb (widget, layout):
    layout.run_manager ()

def button_dump_cb (widget, layout):
    layout.save_to_file ("layout.xml")

win = gtk.Window (gtk.WINDOW_TOPLEVEL)
win.connect ("delete_event", gtk.main_quit)
win.set_title ("Docking widget test")
win.set_default_size (400, 400)

''' table '''
table = gtk.VBox (False, 5)
win.add (table)
table.set_border_width (10)

''' create the dock '''
dock = gdl.Dock ()

''' ... and the layout manager '''
layout = gdl.DockLayout (dock)

''' create the dockbar '''
dockbar = gdl.DockBar (dock)
dockbar.set_style(gdl.DOCK_BAR_TEXT)

box = gtk.HBox (False, 5)
table.pack_start (box, True, True, 0)

box.pack_start (dockbar, False, False, 0)
box.pack_end (dock, True, True, 0)

''' create the dock items '''
item1 = gdl.DockItem ("item1", "Item #1", gdl.DOCK_ITEM_BEH_LOCKED);
item1.add (create_text_item ())
dock.add_item (item1, gdl.DOCK_TOP)

item2 = gdl.DockItem ("item2",
                      "Item #2 has some large title",
                      gtk.STOCK_EXECUTE,
                      gdl.DOCK_ITEM_BEH_NORMAL)
item2.props.resize =  False
item2.add (create_item ("Button 2"))
item2.show_all ()

dock.add_item (item2, gdl.DOCK_RIGHT)

item3 = gdl.DockItem ("item3", "Item #3 has accented characters (áéíóúñ)",
                      gtk.STOCK_CONVERT,
                      gdl.DOCK_ITEM_BEH_NORMAL |
                      gdl.DOCK_ITEM_BEH_CANT_CLOSE)
item3.add (create_item ("Button 3"))
dock.add_item (item3, gdl.DOCK_BOTTOM)

item = gdl.DockItem ("Item #4", "Item #4", 
                     gtk.STOCK_JUSTIFY_FILL,
                     gdl.DOCK_ITEM_BEH_NORMAL |
                     gdl.DOCK_ITEM_BEH_CANT_ICONIFY)

item.add (create_text_item ())
dock.add_item (item, gdl.DOCK_BOTTOM)

for i in range(1, 3):
    name =  "Item #%s" % (i + 4)
    a_item = gdl.DockItem (name, 
                           name, 
                           gtk.STOCK_NEW,
                           gdl.DOCK_ITEM_BEH_NORMAL)

    a_item.add (create_text_item ())

    item.dock (a_item, gdl.DOCK_CENTER)

''' tests: manually dock and move around some of the items '''

item3.dock_to (item1, gdl.DOCK_TOP)

item2.dock_to (item3, gdl.DOCK_RIGHT)

item2.dock_to (item3, gdl.DOCK_LEFT)

item2.dock_to (None, gdl.DOCK_FLOATING)
        
box = gtk.HBox (True, 5)
table.pack_end (box, False, False, 0)

button = gtk.Button (None, gtk.STOCK_SAVE)
button.connect ("clicked", save_layout_cb, layout)
box.pack_end (button, False, True, 0)

button = gtk.Button ("Layout Manager")
button.connect ("clicked", run_layout_manager_cb, layout)
box.pack_end (button, False, True, 0)
	
button = gtk.Button ("Dump XML")
button.connect ("clicked", button_dump_cb, layout)
box.pack_end (button, False, True, 0)

a = gdl.DockPlaceholder ("ph1", dock, gdl.DOCK_TOP, False)
b = gdl.DockPlaceholder ("ph2", dock, gdl.DOCK_BOTTOM, False)
c = gdl.DockPlaceholder ("ph3", dock, gdl.DOCK_LEFT, False)
d = gdl.DockPlaceholder ("ph4", dock, gdl.DOCK_RIGHT, False)

win.show_all()
gtk.main()
