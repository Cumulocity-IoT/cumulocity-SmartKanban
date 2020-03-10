import logging

import mapper
import settings


class Event(object):

    def __init__(self,macID):
        self.logger = logging.getLogger('Event')
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger.debug('Logger for Event was initialised')
        self.macID = macID.translate({ord(':'): None})
        self.logger.info('The following macID was pressed: %s', self.macID)
        self.logger.debug('Checking whether MAC is listed')
        if mapper.checkWhetherIDIsListed(self.macID) is False:
            self.logger.info('Mac address is not listed inside C8Y, setting event.valid to false and skipping event')
            self.valid = False
            return
        self.valid = True
        self.macIDName = mapper.checkWhetherIDIsListed(self.macID)
        self.logger.info('macID is listed in C8Y %s', self.macIDName)
        self.c8yTopic = 's/us'
        self.logger.info('c8yTopic was set inside the Event to %s', self.c8yTopic)
        self.c8yPayload = '400,' + 'c8y_MAC_Event' + ',The following Mac Adress was seen ' + str(self.macID)
        self.logger.info('C8yPayload was set inside the Event to %s', self.c8yPayload)
