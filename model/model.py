from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Relationship
from .base import TimeStampModel, Model

class Person(TimeStampModel):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    phone = Column(String(255), unique=True)
    family_id = Column(Integer, ForeignKey("person.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)

    family = Relationship("Person", remote_side=[id])
    role = Relationship("Role", secondary="people_roles", back_populates="people", passive_deletes=True)
    addresses = Relationship("Address", back_populates="person", passive_deletes=True)
    user = Relationship("User", back_populates="person", passive_deletes=True)

class User(TimeStampModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(255), nullable=False, unique=True)
    passw = Column(String(255))

    preference = Relationship("Preference", back_populates="user", uselist=False, passive_deletes=True)
    person = Relationship("Person", back_populates="user", passive_deletes=True)

class Preference(TimeStampModel):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(80), nullable=False, default="Bahasa Indonesia")
    currency = Column(String(3), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, index=True, unique=True)

    user = Relationship("User", back_populates="preference")

class Address(TimeStampModel):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    road_name = Column(String(255))
    postcode = Column(String(255))
    city = Column(String(255), nullable=False)
    person_id = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"), nullable=False, index=True)

    person = Relationship("Person", back_populates="addresses")

class Role(Model):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)

    people = Relationship("Person", secondary="people_roles", back_populates="role", passive_deletes=True)


class PeopleRoles(TimeStampModel):
    __tablename__ = "people_roles"

    person_id = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    role_id = Column(Integer, ForeignKey("role.id", ondelete="CASCADE"), primary_key=True)