from sqlalchemy import Column, BigInteger, String
from sqlalchemy.util import hybridproperty

from model.base import Base


class BlackList(Base):
    __tablename__ = 'black_list'
    __id = Column('id', BigInteger, primary_key=True)
    __domain = Column('domain', String)

    def __init__(self,
                 domain: str):
        self.__domain = domain

    @hybridproperty
    def id(self):
        return self.__id

    @hybridproperty
    def domain(self):
        return self.__domain
