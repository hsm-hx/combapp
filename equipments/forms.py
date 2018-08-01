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

class NewForm(forms.Form):
  TYPE_CHOICES = (
    (1, '書籍'),
    (2, 'デバイス'),
    (3, 'コンピュータ'),
  )
  name = forms.CharField(
    label = '名称',
    max_length = 50,
    required = True,
    widget = forms.TextInput(),
  )
  eq_type = forms.ChoiceField(
    label = '種別',
    widget = forms.RadioSelect,
    choices = TYPE_CHOICES,
    required = True,
  )
  remark = forms.CharField(
    label = '備考',
    widget = forms.Textarea(),
    required = False,
  )
