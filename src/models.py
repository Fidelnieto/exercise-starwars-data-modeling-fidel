import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    subscription_date = Column(String) 

    favorites = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))

    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    vehicle = relationship("Vehicle")
    planet = relationship("Planet")


class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)

    favorites = relationship("Favorite", back_populates="character")


class Vehicle(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    max_atmosphering_speed = Column(String)
    crew = Column(String)
    passengers = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)
    vehicle_class = Column(String)

    favorites = relationship("Favorite", back_populates="vehicle")

class Planet(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rotation_period = Column(String)
    orbital_period = Column(String)
    diameter = Column(String)
    climate = Column(String)
    gravity = Column(String)
    terrain = Column(String)
    population = Column(String)

    favorites = relationship("Favorite", back_populates="planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
