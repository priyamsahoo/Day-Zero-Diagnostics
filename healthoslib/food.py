import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from healthoslib.health_os_client import *

host = 'www.healthos.co'
o_auth_access_token = '16c92e077a2e386cc8ad314ae4813ed96c883f69ff0bb8c7d278a5e537166672'
client = HealthOSClient(host, o_auth_access_token)

food_client = client.food

food_item_name = raw_input("Enter the food item: ")

food_item_query = food_item_name

try:
    result = food_client.search_food_items(food_item_name)
    for i in range(0, len(result)):
        print result[i]['item_name'], ": ", result[i]['calories'], " calories"
except:
    print "Sorry no such food item data available with us."
