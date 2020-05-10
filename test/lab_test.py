import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from healthoslib.health_os_client import *

host = 'www.healthos.co'
o_auth_access_token = '187803134480f3bfead3b23e4f2f8203a29be237c7718405d245c5b102f9e745'
client = HealthOSClient(host, o_auth_access_token)


lab_tests_client = client.lab_tests


def labFunc(labname):

    try:
        result = lab_tests_client.search_lab_tests(labname)
        result_lab_test_data = result[0]['lab_test_data']
    except:
        result = []

        # print "Test code: " + result_lab_test_data['Test Code']
        # print "Alternate name: " + result[0]['alternate_name']
        # print "Laboratory: " + result_lab_test_data['Laboratory']
        # print "Frequency: " + result_lab_test_data['Frequency']
        # print "Specimen types: " + result_lab_test_data['Specimen types']
        # print "Minimum Adult Volume: " + result_lab_test_data['Minimum Adult Volume']
    if len(result) != 0:
        with open("labData.txt", "w") as fptr:
            fptr.write(str(result))
    else:
        with open("labData.txt", "w") as fptr:
            fptr.write(" ")
