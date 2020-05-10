import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from healthoslib.health_os_client import *
host = 'www.healthos.co'
o_auth_access_token = '187803134480f3bfead3b23e4f2f8203a29be237c7718405d245c5b102f9e745'
client = HealthOSClient(host, o_auth_access_token)

food_client = client.food


def foodFunc(foodName):
    try:
        result = food_client.search_food_items(foodName)
    except:
        result = []
    if len(result) != 0:
        with open("foodData.txt", "w") as fptr:
            for i in range(0, len(result)):
                fptr.write(str(result[i]['item_name'])+" : " +
                           str(result[i]['calories']) + " calories" + "\n")
    else:
        with open("foodData.txt", "w") as fptr:
            fptr.write(" ")
