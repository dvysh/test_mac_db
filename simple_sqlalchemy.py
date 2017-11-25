#!/usr/bin/env python3

from flask import Flask
from flask_table import Table, Col

#import os
#import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

Base = declarative_base()

class Macaddress(Base):
    __tablename__ = 'macaddress'
    id = Column(Integer, primary_key=True)
    mac = Column(String(20), unique=True)
    account = Column(String(250))
    status = Column(String(8))
    fullname = Column(String(250))
    desc = Column(String(250))
    alive = Column(String(8))

engine = create_engine('postgresql://test123:p0o9i8u7@192.168.248.189/ddtest', echo=False )
DBSession = sessionmaker(bind=engine)
session = DBSession()

class UserTable(Table):
    mac = Col('Mac address')
    account = Col('Account')
    status = Col('Status')
    fullname = Col('Full Name')
    desc = Col('Description')

users = session.query(Macaddress).all()

@app.route('/')
def index():
    return UserTable(items=users,border=True).__html__()

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
