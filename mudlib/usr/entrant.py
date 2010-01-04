# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/entant.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
BaseUser derived class to handle logins and new account creation.
"""

import random

from mudlib.sys import THE_LOG
from mudlib.dat import rejected_name
from mudlib.dat import check_credentials
from mudlib.dat import record_visit
from mudlib.usr import BaseUser
from mudlib.usr.account import create_account
from mudlib.usr.account import load_account

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


class Entrant(BaseUser):

    """
    Process logins and new account registrations.
    """

    def __init__(self, client):

        BaseUser.__init__(self, client)
        self.client = client
        self.login_attempts = 0
        self.username = 'Anonymous'
        self.password = None
        self.uuid = None
        client.send_cc(_GREETING % random.choice(_BCOLORS))

        self.state = None
        self.req_username()

#    def __del__(self):
#        print "Entrant destructor called"

    #---------------------------------------------------------Returning Players

    def req_username(self):
        self.send("Username or ^!new^1 to create an account: ")
        self.change_state('get_username')

    def req_password(self):
        self.send("password: ")
        self.client.password_mode_on()
        self.change_state('get_password')

    def state__get_username(self):
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

    def state__get_password(self):
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

            elif status == 'suspended':
                self.alert('\nAccount is under temporary suspension.\n')
                record_visit(self.username, self.client.address)
                self.delayed_deactivate()

            else:
                ## Load existing account
                self.uuid = uuid
                record_visit(self.username, self.client.address)
                load_account(self.client, self.username, self.uuid)

    #--------------------------------------------------------------New Accounts

    def req_new_username(self):
        self.send('Username for new account: ')
        self.change_state('get_new_username')

    def req_new_password(self):
        self.send('Password for new account: ')
        self.client.password_mode_on()
        self.change_state('get_new_password')

    def req_new_password_again(self):
        self.send('\nType the password again just to be sure: ')
        self.change_state('get_new_password_again')

    def state__get_new_username(self):
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

    def state__get_new_password(self):
        password =  self.client.get_command()
        if password == '':
            self.send('\n')
            self.req_new_password()
        else:
            self.password = password
            self.req_new_password_again()

    def state__get_new_password_again(self):
        password =  self.client.get_command()
        if password != self.password:
            self.alert('\nPasswords do not match.\n')
            self.req_new_password()
        else:
            ## Create a new account
            self.client.password_mode_off()
            create_account(self)
