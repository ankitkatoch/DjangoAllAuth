from django import forms
from allauth.account.forms import SignupForm


# class MyCustomSignupForm(SignupForm):
#     # organization = forms.CharField(max_length=30, label='Organisation')
#
#     def signup(self, request, user):
#         user.organization = self.cleaned_data['organization']
#         user.save(active=False)
#         return user

