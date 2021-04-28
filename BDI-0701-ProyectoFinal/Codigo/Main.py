# -*- coding: utf-8 -*-
from Core.Conexion.ConnectionConfig import ConnectionConfig
from Core.Conexion.MySQLEngine import MySQLEngine
from Core.Ventanas.Interface import Interface
from configparser import ConfigParser
from tkinter import *
import os




config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'Core', 'config.ini'))
config.read('.core/config.ini')

host = config['mysql']['host']
port = config['mysql']['port']
user = config['mysql']['user']
password = config['mysql']['password']
database = config['mysql']['database']


sqlConfig = ConnectionConfig(host, port, user, password, database)
engine = MySQLEngine(sqlConfig)



Interface(engine)
