import configparser

config = configparser.ConfigParser()
config.read('config.ini')

tenant = config['C8YMQTT']['tenant']
tenantID = config['C8YMQTT']['tenantID']
c8yPort = config['C8YMQTT']['port']
c8yUser = config['C8YMQTT']['user']
c8yPassword = config['C8YMQTT']['password']
