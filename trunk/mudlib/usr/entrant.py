# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/entant.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""User-parented Class to handle logins and new account creation."""

import random
from uuid import uuid4

from mudlib.sys.log import THE_LOG
from mudlib.dat.map import rejected_name
from mudlib.dat.map import check_credentials
from mudlib.dat.map import add_account
from mudlib.dat.map import last_on
from mudlib.dat.map import record_visit
from mudlib.dat.kv import store_kv_dict
from mudlib.dat.kv import fetch_kv_dict
from mudlib.usr.user import User


_GREETING = """^kb%s^s
     ____              ____
    |  _ \  Amazingly |  _ \   Incomplete
    | |_) | ___   __ _| |_) | ___   __ _
    |  _ < / _ \ / _` |  _ < / _ \ / _` |
    | |_) | (_) | (_| | |_) | (_) | (_| |
    |____/ \___/ \__, |____/ \___/ \__,_|
                  __/ |
    & Unstable   |___/        Test Server^w

"""

_BCOLORS = ['^R', '^B', '^C', '^M', '^G', '^Y',
    '^r', '^b', '^c', '^m', '^g', '^y', ]


class Entrant(User):

    """
    Process logins and new account registrations.
    """

    def __init__(self, client):

        User.__init__(self, client)
        self.login_attempts = 0
        self.username = 'Anonymous'
        self.password = None
        self.uuid = None

        client.send_cc(_GREETING % random.choice(_BCOLORS))
        self.req_username()

    def __del__(self):

        print "Entrant destructor called"


    #---------------------------------------------------------Returning Players

    def req_username(self):
        self.send("Username or ^!new^1 to create an account: ")
        self.cmd_driver = self.get_username

    def get_username(self):
        name = self.client.get_command()

        if name.lower() == 'new':
            self.req_new_username()
        elif name.lower() == 'quit':
            self.send('Seeya.\n')
            self.deactivate()

        elif name == '':
            self.req_username()
        else:
            self.username = name
            self.req_password()

    def req_password(self):
        self.send("password: ")
        self.client.password_mode_on()
        self.cmd_driver = self.get_password

    def get_password(self):
        password = self.client.get_command()
        if password == '':
            self.req_password()

        else:
            self.client.password_mode_off()
            uuid, status = check_credentials(self.username, password)
            if status == 'failed':
                self.alert('\nUsername and/or password not found.\n')
                self.req_username()

            elif status == 'banned':
                self.alert('\nAccount has been permanently banned.\n')
                record_visit(self.username, self.client.address)
                self.delayed_deactivate()
                #self.cmd_driver = self._do_nothing

            elif status == 'suspended':
                self.alert('\nAccount is under temporary suspension.\n')
                record_visit(self.username, self.client.address)
                self.delayed_deactivate()
                #self.cmd_driver = self._do_nothing

            else:
                ## Load existing account
                self.uuid = uuid
                self.load_account()

    #--------------------------------------------------------------Load Account

    def load_account(self):

        self.send('\nWelcome back, %s.\n' % self.username)
        self.send('Your last visit was %s.\n' % last_on(self.username))
        record_visit(self.username, self.client.address)

        profile = fetch_kv_dict(self.uuid, 'profile')


    #--------------------------------------------------------------New Accounts

    def req_new_username(self):
        self.send('Username for new account: ')
        self.cmd_driver = self.get_new_username

    def get_new_username(self):
        name = self.client.get_command()
        if len(name) < 3:
            self.alert('Sorry, that name is too short.\n')
            self.req_new_username()
        elif len(name) > 20:
            self.alert('Sorry, that name is too long.\n')
            self.req_new_username()
        elif rejected_name(name):
            self.alert('Sorry, that name is not available.\n')
            self.req_new_username()
        else:
            self.username = name
            self.req_new_password()

    def req_new_password(self):
        self.send('Password for new account: ')
        self.client.password_mode_on()
        self.cmd_driver = self.get_new_password

    def get_new_password(self):
        password =  self.client.get_command()
        if password == '':
            self.send('\n')
            self.req_new_password()
        else:
            self.password = password
            self.req_new_password_again()

    def req_new_password_again(self):
        self.send('\nType the password again just to be sure: ')
        self.cmd_driver = self.get_new_password_again

    def get_new_password_again(self):
        password =  self.client.get_command()
        if password != self.password:
            self.alert('\nPasswords do not match.\n')
            self.req_new_password()
        else:
            ## Create a new account
            self.client.password_mode_off()
            self.create_account()

    #------------------------------------------------------------Create Account

    def create_account(self):

        self.send("\nCreating your account. "
                "Please don't forgot your username or password.\n")
        self.uuid = uuid4().get_hex()
        add_account(self.username, self.password, self.uuid,
            self.client.address)

        profile = {
            'name':self.username,
            'race':'human',
            'gender':'male',
            'guild':'fighter',
            'level':1,
            }

        store_kv_dict(self.uuid, 'profile', profile)
