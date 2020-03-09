#!/usr/bin/python
# coding=utf-8
import logging
import math
import sys
import os
from scapy.all import *

import mapper
import event
import sendData


logger = logging.getLogger('Listener')
logger.debug('Logger for Listener was initialised')

def udp_filter(pkt):
    if pkt.haslayer(DHCP):
        options = pkt[DHCP].options
        for option in options:
            if isinstance(option, tuple):
                if 'requested_addr' in option:
                    CurrentEvent = event.Event(pkt.src)
                    if CurrentEvent.valid is not False:
                        logger.debug('Creating connector to C8Y´s MQTT')
                        C8YConnector = sendData.MQTTc8yConnector(ID = pkt.src)
                        logger.debug('Connector to C8Y´s MQTT created, Creating SendMQTT to C8Y object and inserting event')
                        C8YSendMQTTData = sendData.SendDataViaMQTT(C8YConnector,CurrentEvent)
                        logger.debug('Connector to C8Y´s MQTT created, Creating SendMQTT to C8Y object and inserting event')
    else:
        logger.debug('No DHCP Layer')

sniff(prn=udp_filter, store=0, filter="udp")
if __name__ == "__main__":
    try:
        logger.info('Starting listener')
    except KeyboardInterrupt:
        logger.warning('KeyboardInterrupt was called, stopping listener and raising SystemExit')
        raise SystemExit
