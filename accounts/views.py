from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from main_app.forms import ImageForm
from .models import ImageCollector
from django.conf import settings    

import numpy as np
from keras.preprocessing import image

def register(request):
    # print("in register")
    if request.method == 'POST':
        # print('POST')
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:    
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
                
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                print('User created')
                return redirect('/accounts/login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:    
            form_data = form.save()
            form_data.username = request.user.username
            form_data.save()
            data = ImageCollector.objects.filter(username = request.user.username).order_by('-created_at')[:1]

            #Some Machine Learning Shit
            model = settings.MODEL
            image_path = settings.MEDIA_ROOT +'/'+ data.values('patient_img')[0]['patient_img']
            pred_img = image.load_img(image_path, target_size = (224, 224))
            pred_img = image.img_to_array(pred_img)
            pred_img = np.expand_dims(pred_img, axis = 0)
            with settings.GRAPH.as_default():
                result = model.predict(pred_img, batch_size = 1)

            print('There is a '+str(round(result[0][0],2))+'% chance of malignancy')

            return render(request, 'results.html', {'data' : data, 'result' : str(round((result[0][0]  * 100),2))})       
            
        else: 
            return redirect('/')        
        
    # else:
    #     form = PatientDataForm()
    # return render(request, 'index.html', {
    #     'form' : form
    # })

