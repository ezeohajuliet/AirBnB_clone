#!/usr/bin/phthon3
""" User Module: Inherits from BaseModel """

from models.base_model import BaseModel

class User(BaseModel):
	""" Defines User based on the BaseModel class
	email (str): the user's email
	password (str): the user's password
	first_name (str): the user's first name
	last_name (str): the user's last name
	"""

	email = ""
	password = ""
	first_name = ""
	last_name = ""
