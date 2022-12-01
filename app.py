import json
import os
import redis
import flask
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def prediction():
  file = open(os.getcwd() + "/data.json")
  json_file = json.load(file)
  data = json_file
  def get3items():
    max_items = 0
    food_item = ""
    for eater_id, data_ in data.items():
      for food_id,diner in data_.items():
        if eater_id == food_id:
          # if 
          raise NameError("Fooditem ID and Eater ID is same")
        else:
          if max_items < len(diner):
            max_items = len(diner)
            food_item = food_id
            e_id = eater_id

    data.pop(e_id)
    return food_item,max_items


  f_1,m_1 = get3items()
  a = f"1st food item {f_1} with {m_1} diners."

  f_2,m_2 = get3items()
  b = f"2nd food item {f_2} with {m_2} diners."

  f_3,m_3 = get3items()
  c = f"3rd food item {f_3} with {m_3} diners."

  return a,b,c


@app.route('/')
def hello():
  a,b,c = prediction()
  return f"{a}\n{b}\n{c}"