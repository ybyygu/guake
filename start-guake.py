#! /usr/bin/env python2
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
__UPDATED__ = '2016-02-01 09:49:06 ybyygu'

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
    # screen -a -A -D -R core
    #remote_object.execute_command("screen -a -A -D -R gwp -dm sslocal -c shadowsocks/config.jp109")
    #remote_object.execute_command("tmux new -d -n emacs 'emacs /home/ybyygu/Notes/todo.note'")
    #remote_object.execute_command("emacs /home/ybyygu/Notes/todo.note")
    
    # music daemon
    #mpd ~/.mpd/config

    #conky

    # task manager
    #glista &

    # zotero helper
    #glocator &

    # emacs server
    # commented at 2011/05/21; "emacsclient -c" will create daemon at the first place if necessary
    # emacsclient -e "(kill-emacs)"; LC_CTYPE=zh_CN.utf8 emacs --daemon

    # mouse controller
    # quite unstable. disabled at 2012-08-12
    #imwheel -k -b '0 0 0 0 8 9'
    #easystroke &

    # my notification daemon
    #gnotifier.py -d &
    #sleep 1

    # must be started before lsyncd (launched by start-guake.py)
    #boost-firefox.py

    # open screen session backgroundly
    #screen -dm
    # maximus windows area

    #maximus &

    # check my mails
    #$HOME/bin/gmail-checker.py &

    #osmo &

    remote_object.add_tab()
    remote_object.rename_current_tab("proxy")
    remote_object.execute_command("~/etc/proxy/shadowsocks/start-ss.sh")
    
    remote_object.add_tab()
    remote_object.rename_current_tab("backup")
    # reduce io delay
    remote_object.execute_command("ionice -c 3 ~/etc/backup/start-lsyncd.sh")

    remote_object.add_tab()
    remote_object.rename_current_tab("workrave")
    remote_object.execute_command("workrave")
    
    remote_object.add_tab()
    remote_object.rename_current_tab("dropbox")    
    remote_object.execute_command("dropbox")

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
