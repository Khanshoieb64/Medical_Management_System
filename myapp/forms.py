from django import forms
from .models import AddMedicine,Register,LoginModel

class AddMedicineForm(forms.ModelForm):
    class Meta:
        model=AddMedicine
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter Name','class':'name'}),
            'company':forms.TextInput(attrs={'placeholder':'Enter Company','class':'company'}),
            'rate':forms.TextInput(attrs={'placeholder':'Enter Rate','class':'rate'}),
            'mrp':forms.TextInput(attrs={'placeholder':'Enter MRP','class':'mrp'}),
            'quantity':forms.TextInput(attrs={'placeholder':'Enter Quantity','class':'quantity'}),
            'type':forms.TextInput(attrs={'placeholder':'Type','class':'type'}),
            'purchase_date':forms.DateInput(attrs={'placeholder':'mm/dd/yy','class':'purchase'}),
            'expiry_date':forms.DateInput(attrs={'placeholder':'mm/dd/yy','class':'expiry'}),
        
        }
        labels={
            'mrp':'MRP',
            'purchase_date':'Purchase Date',
            'expiry_date':'Expiry Date',
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter Name','class':'name'}),
            'username':forms.TextInput(attrs={'placeholder':'Enter Username','class':'username'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'pass'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Email','class':'email'}),
        }
        labels={
            'name':'',
            'username':'',
            'password':'',
            'email':'',
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model=LoginModel
        fields='__all__'
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter Username','class':'username'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'pass'}),
        }
        labels={
            'username':'',
            'password':'',
        }