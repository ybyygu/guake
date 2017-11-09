#! /usr/bin/env python2
# [[file:~/Install/configs/guake/guake.note::648a338e-cc21-4aed-908f-2fe014b65ece][648a338e-cc21-4aed-908f-2fe014b65ece]]
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
#       CREATED:  <2010-11-02 Tue 14:39>
#       UPDATED:  <2017-11-09 Thu 11:01>
#====================================================================#
# 648a338e-cc21-4aed-908f-2fe014b65ece ends here

# [[file:~/Install/configs/guake/guake.note::4a0758fd-1722-4c72-9262-1d906556c5d5][4a0758fd-1722-4c72-9262-1d906556c5d5]]
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
# 4a0758fd-1722-4c72-9262-1d906556c5d5 ends here

# [[file:~/Install/configs/guake/guake.note::4aa333ff-9989-4938-a1b9-429fd1cf12e1][4aa333ff-9989-4938-a1b9-429fd1cf12e1]]
def add_tabs(remote_object):
    ##
    # gmail checker
    # --------------------------------------------------------------------
    # use gconf-editor to disable apps/guake/use_vte_titles;
    # if not rename cmd will lose effect
    remote_object.rename_current_tab("sys")

    remote_object.add_tab()
    remote_object.rename_current_tab("proxy")
    remote_object.execute_command("sslocal -c ~/Install/configs/proxy/shadowsocks/config.default")
    time.sleep(5)

    remote_object.add_tab()
    remote_object.rename_current_tab("backup")
    # reduce io delay
    remote_object.execute_command("ionice -c 3 ~/Backup/start-lsyncd.sh")

    remote_object.add_tab()
    remote_object.rename_current_tab("dropbox")
    remote_object.execute_command("sleep 30 && dropbox")
# 4aa333ff-9989-4938-a1b9-429fd1cf12e1 ends here

# [[file:~/Install/configs/guake/guake.note::bc16e801-32b3-48c1-9241-6fa586882570][bc16e801-32b3-48c1-9241-6fa586882570]]
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
# bc16e801-32b3-48c1-9241-6fa586882570 ends here

# [[file:~/Install/configs/guake/guake.note::b3f9cba8-d656-43fa-8ec1-eb204d2d2750][b3f9cba8-d656-43fa-8ec1-eb204d2d2750]]
def main():
    remote_object, already_running = start_guake()

    if not already_running:
        add_tabs(remote_object)
        gtk.main()

if __name__ == '__main__':
    main()
# b3f9cba8-d656-43fa-8ec1-eb204d2d2750 ends here
