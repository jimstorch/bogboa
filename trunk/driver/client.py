# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/client.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

# telnet_conn -> client -> avatar


class Client(object):

    def __init__(self):

        self.conn = None
        self.active = False
        self.avatar = None

    #--------------------------------------------------------------------Inform

    def send(self, msg):
        self.conn.send(msg) 

    #-----------------------------------------------------------Process Command

    def process_command(self):
        cmd = self.conn.get_command()
        print cmd
        self.send(cmd)

    #----------------------------------------------------------------Deactivate

    def deactivate(self):
        self.active = False
        self.conn.active = False
