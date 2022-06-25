from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
import pandas as pd
from yelp.utils import get_db, get_collection




# Create your views here.
db_handle, mongo_client = get_db("Yelp","mongodb://localhost:27017/")
collection_handle = get_collection(db_handle,"Users")

def Table(request):
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient['Yelp']
    collection = db['Users']
    users_query = pd.DataFrame(collection.find())
    
    #'tableview/static/csv/20_Startups.csv' is the django 
    # directory where csv file exist.
    # Manipulate DataFrame using to_html() function
    users_query = users_query.to_html()
  
    return HttpResponse(users_query)