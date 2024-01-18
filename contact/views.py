from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm() # Instanciando una clase form vacio
    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST) # Instanciando una clase form no vacio
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            # Estructura del mensaje
            send_mail = EmailMessage(
                f"Hairnic: {subject}",
                f"De {name} <{email}> \n\n Contenido: \n\n {message}",
                f"{email}",
                ["hairnic@gmail.com"],
                reply_to = [email],
            )
            # Enviar el correo
            send_mail.send()

            return redirect(reverse('contact')+"?ok")
    return render(request, "contact/contact.html", {'form':contact_form})