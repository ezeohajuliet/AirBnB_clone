#!/usr/bin/python3

""" Place Module """

from models.base_model import BaseModel

class Place(BaseModel):
	""" This class inherits from the BaseModel
	Attributes:
		city_id (str): This is the <city_id>
		user_id (str): This is the <user_id>
		name (str): This is the name of the place
		description (str): Description of the place
		number_rooms (int): Number of the room
		number_bathrooms (int): This is the number of bathrooms
		max_guest (int): Maximum number of quest expected
		price_by_night (int): Price per night
		latitude (float): Latitude of the place
		longitude (float): Longitude of the place
		amenity_ids (list): List of strings of <amenity_id>
	"""

	city_id = user_id = name = description = ""
	number_rooms = number_bathrooms = max_guest = price_by_night = 0
	latitude = longitude = 0.0
	amenity_ids = []
