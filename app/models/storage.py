# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import MetaData, Table, Column, Sequence, ForeignKey,\
                        Integer, BigInteger, SmallInteger,\
                        String, Text, Boolean, Binary, PickleType,\
                        Date, DateTime, Time, TIMESTAMP, Enum,\
                        create_engine, UniqueConstraint, Index
from sqlalchemy.databases import mysql
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text, Column, String, Text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import func, desc, distinct
import datetime



engine_read = create_engine(config.MYSQL_READ, echo = config.ECHO_FLAG, pool_recycle=config.POOL_RECYCLE)
engine_write = create_engine(config.MYSQL_WRITE, echo = config.ECHO_FLAG, pool_recycle=config.POOL_RECYCLE)
engine_create = create_engine(config.MYSQL_CREATE, echo = config.ECHO_FLAG, pool_recycle=config.POOL_RECYCLE)

Base = declarative_base()
metadata = MetaData()
metadata.bind = engine_create

session_factory_read = sessionmaker(
    autocommit=False, autoflush=True,
    expire_on_commit=False, bind=engine_read
)

session_factory_write = sessionmaker(
    autocommit=False, autoflush=True,
    expire_on_commit=False, bind=engine_write
)

Session_read = scoped_session(session_factory_read)
Session_write = scoped_session(session_factory_write)

Base.query = Session_read.query_property()


class ORMBase(object):
    def save(self, commit=True, refresh=False):
        session = Session_write()
        session.add(self)
        if commit:
            session.commit()
        if refresh:
            session.refresh(self)
        Session_write.close()
        Session_write.remove()

    def refresh(self):
        Session().refresh(self)

    @classmethod
    def get(cls, id=None, **kw):
        if id is not None:
            orm = cls.query.get(id)
        elif kw:
            orm = cls.query.filter_by(**kw).scalar()
        else:
            orm =  None
        return orm

    @classmethod
    def count(cls, **kw):
        session = Session_read()
        return session.query(func.count(cls.id)).filter_by(**kw).scalar()

    @classmethod
    def getlist(cls, **kw):
        return cls.query.filter_by(**kw).all()

    @classmethod
    def update(cls, filter_key, update_conf):
        session = Session_write()
        instance = cls.get(**filter_key)
        session.query(cls).filter_by(**filter_key).update(update_conf)
        session.commit()
        Session_write.close()
        Session_write.remove()

