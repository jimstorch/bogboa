# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/cmd/system_cmds.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------


from mudlib.sys import THE_LOG
from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.lang import parsers
#from mudlib.dat.map import set_ansi


@parsers.set_or_show
def ansi(player, setting):

    """Turn on or off ANSI color.  No parameters means show current setting."""

    if setting == None:
        curr = player.client.use_ansi
        if curr:
            use = 'on'
        else:
            use = 'off'
        player.send('^YANSI^W is currently set to %s.^w' % use)

    elif setting == True:
        player.client.use_ansi = True
        player.send('^WSetting ^YANSI^W to on.^w')
        ## store preference in database
        #set_ansi(client.name, True)

    else:
        player.client.use_ansi = False
        player.send('Setting ANSI to off.')
        ## store preference in database
        #set_ansi(client.name, False)



@parsers.blank
def ansi_test(player):
    """
    Send ANSI test display.
    """
    test = """
        This is unmodified text.
        Caret escape test: ^^red ^^green ^^blue.
        This is ^dDEFAULT TEXT.
        This is ^~RESET.
        This is ^!BOLD ON and ^.BOLD OFF.
        This is ^IINVERSE ON and ^iINVERSE OFF.
        This is ^UUNDERLINE ON and ^uUNDERLINE OFF.

        ^0This is ^kBLACK and ^KBRIGHT BLACK on black.^~
        ^0This is ^rRED and ^RBRIGHT RED on black.^~
        ^0This is ^gGREEN and ^GBRIGHT GREEN on black.^~
        ^0This is ^yYELLOW and ^YBRIGHT YELLOW on black.^~
        ^0This is ^bBLUE and ^BBRIGHT BLUE on black.^~
        ^0This is ^mMAGENTA and ^MBRIGHT MAGENTA on black.^~
        ^0This is ^cCYAN and ^CBRIGHT CYAN on black.^~
        ^0This is ^wWHITE and ^WBRIGHT WHITE on black.^~

        ^1This is ^kBLACK and ^KBRIGHT BLACK on red.^~
        ^1This is ^rRED and ^RBRIGHT RED on red.^~
        ^1This is ^gGREEN and ^GBRIGHT GREEN on red.^~
        ^1This is ^yYELLOW and ^YBRIGHT YELLOW on red.^~
        ^1This is ^bBLUE and ^BBRIGHT BLUE on red.^~
        ^1This is ^mMAGENTA and ^MBRIGHT MAGENTA on red.^~
        ^1This is ^cCYAN and ^CBRIGHT CYAN on red.^~
        ^1This is ^wWHITE and ^WBRIGHT WHITE on red.^~

        ^2This is ^kBLACK and ^KBRIGHT BLACK on green.^~
        ^2This is ^rRED and ^RBRIGHT RED on green.^~
        ^2This is ^gGREEN and ^GBRIGHT GREEN on green.^~
        ^2This is ^yYELLOW and ^YBRIGHT YELLOW on green.^~
        ^2This is ^bBLUE and ^BBRIGHT BLUE on green.^~
        ^2This is ^mMAGENTA and ^MBRIGHT MAGENTA on green.^~
        ^2This is ^cCYAN and ^CBRIGHT CYAN on green.^~
        ^2This is ^wWHITE and ^WBRIGHT WHITE on green.^~

        ^3This is ^kBLACK and ^KBRIGHT BLACK on yellow.^~
        ^3This is ^rRED and ^RBRIGHT RED on yellow.^~
        ^3This is ^gGREEN and ^GBRIGHT GREEN on yellow.^~
        ^3This is ^yYELLOW and ^YBRIGHT YELLOW on yellow.^~
        ^3This is ^bBLUE and ^BBRIGHT BLUE on yellow.^~
        ^3This is ^mMAGENTA and ^MBRIGHT MAGENTA on yellow.^~
        ^3This is ^cCYAN and ^CBRIGHT CYAN on yellow.^~
        ^3This is ^wWHITE and ^WBRIGHT WHITE on yellow.^~

        ^4This is ^kBLACK and ^KBRIGHT BLACK on blue.^~
        ^4This is ^rRED and ^RBRIGHT RED on blue.^~
        ^4This is ^gGREEN and ^GBRIGHT GREEN on blue.^~
        ^4This is ^yYELLOW and ^YBRIGHT YELLOW on blue.^~
        ^4This is ^bBLUE and ^BBRIGHT BLUE on blue.^~
        ^4This is ^mMAGENTA and ^MBRIGHT MAGENTA on blue.^~
        ^4This is ^cCYAN and ^CBRIGHT CYAN on blue.^~
        ^4This is ^wWHITE and ^WBRIGHT WHITE on blue.^~

        ^5This is ^kBLACK and ^KBRIGHT BLACK on magenta.^~
        ^5This is ^rRED and ^RBRIGHT RED on magenta.^~
        ^5This is ^gGREEN and ^GBRIGHT GREEN on magenta.^~
        ^5This is ^yYELLOW and ^YBRIGHT YELLOW on magenta.^~
        ^5This is ^bBLUE and ^BBRIGHT BLUE on magenta.^~
        ^5This is ^mMAGENTA and ^MBRIGHT MAGENTA on magenta.^~
        ^5This is ^cCYAN and ^CBRIGHT CYAN on magenta.^~
        ^5This is ^wWHITE and ^WBRIGHT WHITE on magenta.^~

        ^6This is ^kBLACK and ^KBRIGHT BLACK on cyan.^~
        ^6This is ^rRED and ^RBRIGHT RED on cyan.^~
        ^6This is ^gGREEN and ^GBRIGHT GREEN on cyan.^~
        ^6This is ^yYELLOW and ^YBRIGHT YELLOW on cyan.^~
        ^6This is ^bBLUE and ^BBRIGHT BLUE on cyan.^~
        ^6This is ^mMAGENTA and ^MBRIGHT MAGENTA on cyan.^~
        ^6This is ^cCYAN and ^CBRIGHT CYAN on cyan.^~
        ^6This is ^wWHITE and ^WBRIGHT WHITE on cyan.^~

        ^0^wThis is white on black.
        """
    player.send(test)




@parsers.blank
def quit(player):
    """
    Exit from the game.
    """
    player.send('\n^YLogging you off -- take care.^w\n')
    THE_LOG.add('.. %s quits from %s' % (player.avatar.get_name(),
        player.client.addrport()))
    THE_SCHEDULER.add(.10, player.deactivate)


def bug(player):
    """
    Permit the player to report a bug to the bug log.
    """
    raise BogCmdError('Not implemented')
