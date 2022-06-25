from django.shortcuts import render
from yelp.utils import get_db, get_collection
db_handle, mongo_client = get_db("Yelp","mongodb://localhost:27017/")
collection_handle = get_collection(db_handle,)
collection_handle.find({...})
collection_handle.insert({...})
collection_handle.update({...})

# Create your views here.
