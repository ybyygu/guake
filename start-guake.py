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
#====================================================================#

__VERSION__ = '0.1.1'
__UPDATED__ = '2015-04-15 19:03:58 ybyygu'

import os
import dbus
import gtk
import sys
import time

import guake.main
from guake.dbusiface import DBUS_NAME
from guake.dbusiface import DBUS_PATH
from guake.dbusiface import DbusManager
from guake.guake_app import Guake

def start_guake():
    ##
    # find dbus object from the running instance
    # --------------------------------------------------------------------
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

    return remote_object, already_running
        
def add_tabs(remote_object):
    ##
    # gmail checker
    # --------------------------------------------------------------------
    # use gconf-editor to disable apps/guake/use_vte_titles;
    # if not rename cmd will lose effect
    remote_object.rename_current_tab("sys")
    # open screen session
    remote_object.execute_command("screen -dm sslocal -c shadowsocks/config.jp109")
    
    remote_object.add_tab()
    remote_object.rename_current_tab("backup")
    # remote_object.execute_command("nice -n 10 gmail-checker.py")
    # remote_object.execute_command("ionice -c 3 start-lsyncd.sh")
    # remote_object.execute_command("nice -n 15 isync-dwim")
    
        
def main():
    remote_object, already_running = start_guake()
    
    if not already_running:
        add_tabs(remote_object)
        gtk.main()

if __name__ == '__main__':
    main()

# Emacs:
# Local Variables:
# time-stamp-pattern: "100/^__UPDATED__ = '%%'$"
# End:
