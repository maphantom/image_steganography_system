import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from PIL import Image
import stepic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def say_hello(request):
    return render(request, "index.html")

def main(request):
    return render(request, "main.html")
def hide_text_in_image(image,text):
      data = text.encode('utf-8')
      return stepic.encode(image,data)

def encryption(request):
    message = ''
    if request.method == "POST":
        text = request.POST.get('text')
        image_file = request.FILES.get('image')
        if text and image_file:
            image = Image.open(image_file)
            new_image = hide_text_in_image(image, text)
            # Ensure the 'encrypted_images' directory exists
            os.makedirs('encrypted_images', exist_ok=True)
            # Construct the image path with the original filename and extension
            image_name, image_ext = os.path.splitext(image_file.name)
            image_path = f'encrypted_images/new_{image_name}.png'
            new_image.save(image_path)
            message = 'Text has been hidden in the image'

    return render(request, "encryption.html", {'message': message})

def decryption(request):
    text = ''
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            image = Image.open(image_file)
            text = extract_text_from_image(image)
    return render(request, "decryption.html", {'text': text})

def extract_text_from_image(image):
    data = stepic.decode(image)
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data

def user_login(request):
    if request.method == 'POST':
    
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None and user.is_authenticated:
                login(request, user)
                return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'regester.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')