# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:19:31 2021

@author: Mohammed
"""
from pymongo import MongoClient
import json
import numpy as np


cluster = MongoClient("mongodb+srv://MoElfadil:SIOTproject123@cluster0.4wzez.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["<dbname>"]
collection = db["Lichess"]
collection2 = db["Emotions"]

for i in range(0,30):
results = collection.find({})

#post = {
#	"result" : "loss",
#	"moves" : "A4",
#	"date" : "02:04",
#	"time" : "6:20",
# "colour" : "white"
#}
#
#collection.insert_one(post)
#results = collection2.find({"_id": 0})
#emotions = np.array(emotions)
#lists = emotions.tolist()
#json_str = json.dumps(lists)
#post["emotions"] = emotions