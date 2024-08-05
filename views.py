from django.shortcuts import render
from .models import StudentsModels, StudentDetailsModels

# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        # create an object for student
        new_student = StudentsModels( first_name=first_name, last_name=last_name, age=age, email=email)
        new_student.save()

        # get data from database
    pupilone =StudentsModels.objects.all()

    return render(request, 'index.html', {'pupilone':pupilone})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date')
        gender = request.POST.get('gender')

        student = StudentDetailsModels( name=name, email=email, phone_number=phone_number, address=address, date_of_birth=date_of_birth, gender=gender)
        student.save()

    return render(request, 'contact.html')


