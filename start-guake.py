#! /usr/bin/env python
# -*- coding: utf-8 -*-
#====================================================================#
#   DESCRIPTION:  open some desktop tools in guake tags
#
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#         NOTES:  guake should not be started before this script
#        AUTHOR:  Wenping Guo (ybyygu)
#         EMAIL:  winpng@gmail.com
#       LICENCE:  GPL version 2 or upper
#       CREATED:  2010-11-02 14:39
#       UPDATED:
#====================================================================#

__VERSION__ = '0.1'
__UPDATED__ = '2015-04-15 18:04:59 ybyygu'

import os
import dbus
import gtk
import sys

# make sure the guake command is linked into python-lib path as guake.py
from guake_bin import Guake
from guake.dbusiface import DbusManager, DBUS_NAME, DBUS_PATH

def main():
    try:
        bus = dbus.SessionBus()
        remote_object = bus.get_object(DBUS_NAME, DBUS_PATH)
        print("already running")
        already_running = True
    except dbus.DBusException:
        instance = Guake()
        remote_object = DbusManager(instance)
        print("no running instance found")
        already_running = False

    
    ##
    # gmail checker
    # --------------------------------------------------------------------
    # use gconf-editor to disable apps/guake/use_vte_titles or rename cmd will lose effect
    #remote_object.execute_command("nice -n 10 gmail-checker.py")
    remote_object.rename_current_tab("mail")
    remote_object.add_tab()
    remote_object.execute_command("ionice -c 3 start-lsyncd.sh")
    remote_object.rename_current_tab("backup")
    #remote_object.execute_command("nice -n 15 isync-dwim")
    # google tasks
    #remote_object.execute_command('alltray -H -- chromium --app="https://mail.google.com/tasks/ig"')
    
    ##
    # ssh-d proxy
    # --------------------------------------------------------------------
    remote_object.add_tab()
    remote_object.rename_current_tab("proxy")
    remote_object.execute_command("nice -n 10 start-proxy.sh")
    # reduce RSI
    # disabled at 2012-04-30: does not work as expected!
    #remote_object.add_tab()
    #remote_object.rename_current_tab("RSI")
    #remote_object.execute_command("xwrits breaktime=0:20 typetime=20:00 canceltime=2:00 +mouse +lock")
    # for emergency events
    remote_object.add_tab()
    remote_object.rename_current_tab("emergency")

if __name__ == '__main__':
    main()
    gtk.main()

# Emacs:
# Local Variables:
# time-stamp-pattern: "100/^__UPDATED__ = '%%'$"
# End:
