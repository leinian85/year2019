from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(min_length=6,error_messages={'min_length':"用户名太短"})
    pwd1 = forms.CharField(max_length=30)
    pwd2 = forms.CharField(max_length=30)
    age  = forms.IntegerField()

    def clean(self):
        pwd1 = self.cleaned_data["pwd1"]
        pwd2 = self.cleaned_data["pwd2"]
        if pwd1 != pwd2:
            raise forms.ValidationError(message="两次密码不一致")
        return self.cleaned_data