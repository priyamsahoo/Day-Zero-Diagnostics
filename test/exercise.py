import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from healthoslib.health_os_client import *

host = 'www.healthos.co'
o_auth_access_token = '187803134480f3bfead3b23e4f2f8203a29be237c7718405d245c5b102f9e745'
client = HealthOSClient(host, o_auth_access_token)

exercises_client = client.exercises


def exerFunc(exerciseName):
    try:
        resultEX = exercises_client.search_exercises(exerciseName)
    except:
        resultEX = []

    if len(resultEX) != 0:
        with open("exerciseData.txt", "w") as fptr:
            fptr.write("Name: " + str(resultEX[0]['name']) + "\n" +
                       "Category: " + str(resultEX[0]['category']) + "\n" +
                       "Calory count: " + str(resultEX[0]['calory_count']) + "\n" +
                       "Primary muscle group: " + "\n" + str(resultEX[0]['primary_muscle_group'])+"\n")
    else:
        with open("exerciseData.txt", "w") as fptr:
            fptr.write(" ")
