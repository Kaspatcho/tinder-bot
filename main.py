from webscraping import Tinder
from time import sleep

t = Tinder(timeout=20)
number = '' # seu numero
t.login(number)

while True:
    name, description = t.get_person_data()
    if description != -1:
        t.accept_person()
    else:
        t.reject_person()
    sleep(1)

