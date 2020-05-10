import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from healthoslib.health_os_client import *

host = 'www.healthos.co'
o_auth_access_token = '529a69cc5a0f475444821e43e7bcc7e84a5dc7eada857db26433dc49adc246b4'
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
