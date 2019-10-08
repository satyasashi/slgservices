from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages # for Flash Messages
from django.core.mail import mail_admins # Feedback form sending Emails

# Create your views here.
def home(request):
    if request.method == "POST":
        print("POST called")
        f = ContactForm(request.POST)
        print("Errors: {}".format(f.errors))
        print("cleaned_data {}".format(f.cleaned_data))
        if f.is_valid():
            name = f.cleaned_data['name']
            phone = f.cleaned_data['phone']
            subject = name
            email = f.cleaned_data['email']
            message = "\nMessage: {}".format(f.cleaned_data['message'])
            try:
                mail_admins(subject, message)
                f.save()
                print("Message sent")
                messages.add_message(request, messages.INFO, "Form Submitted")
            except Exception as e:
                messages.add_message(request, messages.ERROR, "Sorry something went wrong. Please try after sometime.")
                print("Exception ", e)
            return redirect('home')
    else:
        print("GET called")
        return render(request, 'index.html')
