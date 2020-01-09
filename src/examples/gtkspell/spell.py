#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# a simple example to test gtkspell functions
# coded by Gian Mario Tagliaretti, May 2005


import pygtk
pygtk.require("2.0")

import gtkspell
import gtk

class Spell:
    def __init__ (self):
        SOMETEXT = "some English text wiht a mistake\n"\
                   "un po' di testo italiano con un erore\n"\
                   "algum texto Portugues comm um ero"

        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect ("destroy", self.destroy)
        self.window.set_default_size (500, 300)

        vbox = gtk.VBox (False, 5)
        top_hbox = gtk.HBox (False, 5)
        hbox = gtk.HBox (False, 5)
        
        self.buttonEN = gtk.RadioButton (None, "English")
        self.buttonEN.connect ("clicked", self.english)
        self.buttonIT = gtk.RadioButton (self.buttonEN, "Italian")
        self.buttonIT.connect ("clicked", self.italian)
        self.buttonPT = gtk.RadioButton (self.buttonEN, "Portuguese")
        self.buttonPT.connect ("clicked", self.portuguese)
        
        top_hbox.pack_start(self.buttonEN, False, False, 0)
        top_hbox.pack_start(self.buttonIT, False, False, 0)
        top_hbox.pack_start(self.buttonPT, False, False, 0)
        
        self.buttonSpell = gtk.CheckButton ("Spelling ON")
        self.buttonSpell.set_active(True)
        self.buttonSpell.connect ("clicked", self.toggle)
        
        buttonOpen = gtk.Button (None, gtk.STOCK_OPEN)
        buttonOpen.connect ("clicked", self.open)
        
        buttonQuit = gtk.Button(None, gtk.STOCK_QUIT)
        buttonQuit.connect ("clicked", self.destroy)
        
        hbox.pack_start (self.buttonSpell, False, False, 0)
        hbox.pack_start (buttonOpen, False, False, 0)
        hbox.pack_start (buttonQuit, False, False, 0)
        
        self.buffer = gtk.TextBuffer ()
        self.text = gtk.TextView (self.buffer)
        self.buffer.set_text (SOMETEXT)
        
        sw = gtk.ScrolledWindow ()
        sw.set_policy (gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw.add (self.text)
        
        vbox.pack_start (top_hbox, False, False, 0)
        vbox.pack_start (sw, True, True, 0)
        vbox.pack_start (hbox, False, False, 0)

        self.window.add (vbox)
        self.spell = gtkspell.Spell (self.text)
        self.spell.set_language ("en_US")

        self.window.show_all ()
    
    def toggle (self, widget):
        if widget.get_active():
            self.spell = gtkspell.Spell (self.text)
            self.buttonSpell.child.set_text ("Spelling ON")
        else:
            self.spell = gtkspell.get_from_text_view (self.text)
            self.spell.detach ()
            self.buttonSpell.child.set_text ("Spelling OFF")

    def open (self, widget):
        dia = gtk.FileChooserDialog ("gtkspell", self.window,
                                     gtk.FILE_CHOOSER_ACTION_OPEN,
                                     (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT,
                                      gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
        response = dia.run ()
        if response == gtk.RESPONSE_ACCEPT:
            filename = dia.get_filename ()
            self.buffer.set_text (open (filename, 'r').read ())
        elif response == gtk.RESPONSE_REJECT:
            dia.destroy ()
        dia.destroy ()
        
    def english (self, widget):
        try:
            self.spell.set_language("en_EN")
        except:
            self.error("English")

    def italian (self, widget):
        try:
            self.spell.set_language("it_IT")
        except:
            self.error("Italian")

    def portuguese (self, widget):
        try:
            self.spell.set_language("pt_PT")
        except:
            self.error("Portuguese")

    def error (self, lang):
        message = gtk.MessageDialog(self.window, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, 
                                    gtk.BUTTONS_CLOSE, "Sorry " + lang + " is not supported by your system")
        message.format_secondary_text("Please install the language pack if you wish to use it")
        resp = message.run()
        if resp == gtk.RESPONSE_CLOSE:
            message.destroy()
        message.destroy()
    
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def main(self):
        gtk.main()
        
if __name__ == '__main__':
    spell = Spell()
    spell.main()
