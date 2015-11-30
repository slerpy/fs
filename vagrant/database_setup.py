#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# database_setup.py
# --------------------
# Let's get our db going with SQLAlchemy
#
# @author Shaden, 0x899319D4251502BA
# @date 29 November 2015
# @version 0.0.1
##############################################################################

import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)


class MenuItem(Base):
    __tablename__ = 'table_name'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)



engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create.all(engine)