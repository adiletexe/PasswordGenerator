from django.shortcuts import render
from random import choice
# Create your views here.
def home(request):
     return render(request, 'password_gen_app/index.html')

def password(request):
    generatedpassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length of password', 10))
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('01234567890123456789')
    specialcharacters = list('!@#$%&!@#$%&')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('01234567890123456789'))
    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%&!@#$%&'))

    for i in range(length):
        generatedpassword += choice(characters)

    return render(request, 'password_gen_app/password.html', {'password': generatedpassword})