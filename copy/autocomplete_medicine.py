import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from healthoslib.health_os_client import *
from Tkinter import *

# Configuration parameters and credentials
host = 'www.healthos.co'
o_auth_access_token = '16c92e077a2e386cc8ad314ae4813ed96c883f69ff0bb8c7d278a5e537166672'
client = HealthOSClient(host, o_auth_access_token)

page = 1
size = 10

med = ''


def url_call(med):
    autocomplete_client = client.autocomplete
    medicine_query = med
    try:
        result = autocomplete_client.get_medicines(medicine_query)
        #print result[0]['name']
        return
    except:
        print ""
        return


def key(event):
    # print(event.char)
    global med
    x=str(T.get("1.0",'end-1c')).strip()
    b =url_call(x)
    T.delete("1.0","end")
    T.config(state=NORMAL)
    T.mark_set("insert","0.0")
    print b
    T.insert("1.0","%s"% b)


def bck_spc(event):
    # print('Back space was pressed')
    global med
    med = med[0:len(med)-1]
    url_call(med)
    return

def spc(event):
    # print('Back space was pressed')
    global med
    med = med + event.char
    url_call(med)
    return


master = Tk()
T = Text(master, height=2, width=30)
"""
T.bind('<KeyPress>', key)
T.bind('<BackSpace>', bck_spc)
T.bind('<space>', spc)
"""
T.bind('<Return>', key)
T.pack()
mainloop()
