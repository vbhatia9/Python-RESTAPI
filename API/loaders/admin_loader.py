import os
from common_utils import logger
import requests
from pymongo import MongoClient

mongo=os.environ['MONGO']
#print(f"Mongo {mongo}")
client = MongoClient(mongo)
# Set the db object to point to the business database
db=client.sample_airbnb

pricerangecount = db.listingsAndReviews.find({'price':80}).count()
print(pricerange)