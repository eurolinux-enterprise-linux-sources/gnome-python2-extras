import os
import sys
import warnings
import traceback

warnings.simplefilter('ignore', DeprecationWarning)
#warnings.simplefilter('ignore', ImportWarning)

modules = [
    "gtkhtml2",
    ("egg.trayicon", "egg/tray"),
    ("egg.recent", "egg/recent"),
    "gtkmozembed",
    "gtkspell",
    "gdl",
    "gda",
    "gksu",
    ("gksu.ui", "gksu"),
    ]

import ltihooks

for item in modules:
    if isinstance(item, tuple):
        module, dirname = item
    else:
        module = item
        dirname = item
    sys.path.insert(0, os.path.join("..", dirname))
    print "Trying to import module %s... " % (module,),
    try:
        __import__(module) # try to import the module to catch undefined symbols
    except ImportError, ex:
        if ex.args[0].startswith("No module named"):
            print "not found"
        else:
            traceback.print_exc()
            print "NOT ok"
    else:
        print "ok."

ltihooks.uninstall()
