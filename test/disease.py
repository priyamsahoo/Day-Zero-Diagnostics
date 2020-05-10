import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from healthoslib.health_os_client import *

host = 'www.healthos.co'
o_auth_access_token = '187803134480f3bfead3b23e4f2f8203a29be237c7718405d245c5b102f9e745'
client = HealthOSClient(host, o_auth_access_token)

diseases_client = client.diseases

# disease_name = raw_input("Enter the disease: ")

# disease_query = disease_name


def diseaseFunc(diseaseName):

    try:
        result = diseases_client.search_diseases(diseaseName)

    except:
        result = []

        # print "Disease name: " + result[0]['disease_name']
        # print "Disease category: " + result[0]['disease_cat']
        # print "Disease information: " + result[0]['disease_info']
    if len(result) != 0:
        with open("diseaseData.txt", "w") as fptr:
            fptr.write(str(result))
    else:
        with open("diseaseData.txt", "w") as fptr:
            fptr.write(" ")
