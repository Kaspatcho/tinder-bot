from webscraping import Tinder
from time import sleep

t = Tinder(timeout=20)
phone_number = ''
t.login(phone_number)

while True:
    _, description = t.get_person_data()
    if description != -1:
        t.accept_person()
    else:
        t.reject_person()
    sleep(1)

