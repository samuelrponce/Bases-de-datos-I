#-*- coding: utf-8 -*-
class ConnectionConfig:    
    def __init__(self, server, port, user, password, database):
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.database = database