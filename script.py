#!/usr/bin/env python

import sys
import os
import logging
logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M',
        filename='/tmp/myapp.log',
        filemode='wa')

log = logging.getLogger(__name__)
log.info("input: %s" % sys.argv)
log.info("env: %s" % os.environ)

import xbmc
import urlparse
import time


try:
        params = urlparse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command',None)
except:
        command = None

log.info("Command is now %s" % command)

if command and command[0] == 'activate':
        xbmc.executebuiltin('CECActivateSource')

elif command and command[0] == 'toggle':
        xbmc.executebuiltin('CECToggleState')

elif command and command[0] == 'standby':
        xbmc.executebuiltin('CECStandby')

elif command and command[0] == 'stop_and_standby':
        if xbmc.Player().isPlaying():
                xbmc.executebuiltin("PlayerControl(Stop)")
                time.sleep(3)
        xbmc.executebuiltin('CECStandby')

log.info("Terminating")
