from django import forms

class ContactForm(forms.Form):
	subjecct=forms.CharField(max_length=100)
	message=forms.CharField(widget=forms.Textrea)
	sender=forms.EmailField()
	cc_myself=forms.BooleanField(required=False)
	