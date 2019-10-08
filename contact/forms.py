from django import forms
from django.contrib import messages
from .models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

	# def clean_name(self):
	# 	name = self.cleaned_data['name']
	#
	# 	if len(name) == 0:
	# 		raise forms.ValidationError("Name cannot be empty")
	# 	elif "@" in name or "!" in name or "$" in name or "%" in name or "<>":
	# 		raise forms.ValidationError("Only characters allowed. No special symbols allowed.")
