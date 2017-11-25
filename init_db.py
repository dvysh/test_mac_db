#!/usr/bin/env python3

import os
import sys
import sqlalchemy
import psycopg2
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def unpack_macdb(line):
    entry = line.split(";")
    mac = entry[0]
    acct = entry[1]
    status = entry[2]
    fullname = entry[3]
    desc = entry[4]
    return mac, acct, status, fullname, desc


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
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

f = open("mac.db", "r")
lines = f.readlines()

for line in lines:
    fmac, facct, fstatus, ffullname, fdesc = unpack_macdb(line)
    row = Macaddress(mac=fmac, account=facct, status=fstatus, fullname=ffullname, desc=fdesc)
    session.add(row)
    try:
        session.commit()
#    except sqlalchemy.exc.IntegrityError as err:
    except psycopg2.IntegrityError or sqlalchemy.exc.IntegrityError as err:
#    except IntegrityError as err:
#    except:
        print("Error ISSSS", err)
#        print("Key (mac)=", fmac, "already exists.")
