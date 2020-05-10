import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from healthoslib.health_os_client import *

# Configuration parameters and credentials
host = 'www.healthos.co'
o_auth_access_token = '187803134480f3bfead3b23e4f2f8203a29be237c7718405d245c5b102f9e745'
client = HealthOSClient(host, o_auth_access_token)


def priyamFunc(medicine):
    medicines_client = client.medicines
    medicine_query = medicine
    generic = ''

    try:
        result = medicines_client.search_medicines(medicine_query)
    except:
        result = ""

    if len(result) != 0:
        med_id = result[0]['medicine_id']
        medicine_id = med_id
        constituents = result[0]['constituents']
        generic = constituents[0]['name']

# printing general details
        # print "\n"
        form = result[0]['form']
        # print "Form: ", result[0]['form']
        constituent = generic
        # print "Constituents: ", generic, " ", constituents[0]['strength']
        manufacturer = result[0]['manufacturer']
        # print "Manufacturer: ", result[0]['manufacturer']
        price = result[0]['price']
        # print "Price: ", result[0]['price']
        with open("manufac.txt", "w") as fptr:
            fptr.write(str(manufacturer)+"\n")
            fptr.write(str(price)+"\n")
            fptr.write(str(constituent)+"\n")
            fptr.write(str(form)+"\n")
    else:
        with open("manufac.txt", "w") as fptr:
            fptr.write(str(" "))
    # try:
        # printing side-effects
    print "\nSide Effects: \n"
    try:
        result3 = medicines_client.get_common_side_effects(medicine_id)
        obj = result3[0]['side_effects']

    except:
        obj = ""

    if len(obj) != 0:
        with open("sideEffects.txt", "w") as fptr:
            for i in range(0, len(obj)):
                # print obj[i]['term'], " - ", obj[i]['percent'], "%"
                fptr.write(str(obj[i]['term'])+" - " +
                           str(obj[i]['percent'])+" %"+"\n")

    else:
        with open("sideEffects.txt", "w") as fptr:
            fptr.write(str(" "))

    # printing similar medicines
    print "\nSimilar Medicines: \n"
    try:

        result4 = medicines_client.search_medicines(medicine_query)
    except:
        result4 = ""

    if len(result4) != 0:
        with open("similar.txt", "w") as fptr:
            fptr.write(str(result4)+"\n")

    else:
        with open("similar.txt", "w") as fptr:
            fptr.write(str(" "))

    # for i in range(0, len(result4)):
    #     print "Name: ", result4[i]['name']
    #     print "Form: ", result4[i]['form']
    #     print "Price: ", result4[i]['price']
    #     print "Manufacturer: ", result4[i]['manufacturer']
    #     print "\n"

    # printing therauptic usage
    generics_client = client.generics
    generic_query = generic
    print "Usage: \n"
    try:
        result2 = generics_client.search_generics(generic_query)
        obj2 = result2[0]['therauptic_uses']
        # for i in range(0, len(obj2)):
        # print obj2[i]
    except:
        obj2 = ""
    if len(obj2) != 0:
        with open("theraUses.txt", "w") as fptr:
            for i in range(0, len(obj2)):
                fptr.write(str(obj2[i])+"\n")
    else:
        with open("theraUses.txt", "w") as fptr:
            fptr.write(str(" "))
