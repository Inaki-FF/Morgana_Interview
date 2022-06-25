from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
import pandas as pd
from django.shortcuts import render
from yelp.utils import get_db, get_collection
db_handle, mongo_client = get_db("Yelp","mongodb://localhost:27017/")
collection_handle = get_collection(db_handle,)

# Create your views here.
def Table(request):
    users_query = pd.DataFrame(collection_handle.find())
    
    #'tableview/static/csv/20_Startups.csv' is the django 
    # directory where csv file exist.
    # Manipulate DataFrame using to_html() function
    users_query = users_query.to_html()
  
    return HttpResponse(users_query)