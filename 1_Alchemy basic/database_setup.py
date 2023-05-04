import sys
import pymysql

# sqlalchemy: flask 프레임워크에서 사용하는 ORM 라이브러리 이름
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


# declarative_base() : Table 생성을 위한 부모 class인 Base 생성하는 함수
Base = declarative_base() 

# -------------------------------- configuration ----------------------------------------------------
class Restaurant(Base):
    __tablename__ = 'restaurant'

    # mapper
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item' # 테이블 이름 지정 (default는 클래스 이름인 MenuItem)

    # mapper
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

# -------------------------------- configuration ----------------------------------------------------

##### insert at end of file #####

engine = create_engine('mysql+pymysql://root:root@localhost/restaurant') # restaurant은 데이터베이스 이름

Base.metadata.create_all(engine)
