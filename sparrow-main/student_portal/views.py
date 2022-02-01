from django.shortcuts import render

# Create your views here.



def random_int():
    random_ref = randint(0, 9999999999)
    uid = random_ref
    return uid
