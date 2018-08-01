from django import forms

class BorrowForm(forms.Form):
  ACTION_CHOICES = (
    ('borrowing', 'Borrow'),
    ('returning', 'Return'),
    ('extension', 'Extend'),
  )
  action = forms.ChoiceField(
    label = 'Action',
    widget = forms.RadioSelect,
    choices = ACTION_CHOICES,
    required = True,
  )
  name = forms.CharField(
    label = 'Name',
    max_length = 20,
    required = True,
    widget = forms.TextInput(),
  )
