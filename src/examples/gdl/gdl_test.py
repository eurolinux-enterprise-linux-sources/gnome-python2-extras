#!/usr/bin/python
import pygtk
pygtk.require("2.0")
import gtk
import gdl

win = gtk.Window(gtk.WINDOW_TOPLEVEL)

dock = gdl.Dock()
layout = gdl.DockLayout(dock)

item1 = gdl.DockItem("item1", "Item #1", gtk.STOCK_EXECUTE,gdl.DOCK_ITEM_BEH_NORMAL)
button = gtk.Button ("test")
item1.add(button)
dock.add_item (item1, gdl.DOCK_RIGHT)

item1.dock_to(None, gdl.DOCK_FLOATING, -1)

item1.show_all()

item2 = gdl.DockItem("item2", "Item #2", gtk.STOCK_EXECUTE, gdl.DOCK_ITEM_BEH_NORMAL | gdl.DOCK_ITEM_BEH_CANT_ICONIFY | gdl.DOCK_ITEM_BEH_CANT_CLOSE)
button = gtk.Button ("test2")
item2.add(button)
dock.add_item (item2, gdl.DOCK_RIGHT)

item2.dock_to(None, gdl.DOCK_FLOATING, -1)

item2.show_all()


win.add(dock)


win.show_all()
gtk.main()
