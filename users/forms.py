from django import forms

class Login(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'uk-input uk-width-1-1'

    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class Register(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'uk-input uk-width-1-1'

    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

# class Register(FlaskForm):
#     username = StringField(label="Username", validators=[DataRequired()])
#     email = StringField(label="Email")
#     password = PasswordField(label="Password", validators=[DataRequired()])
#     submit = SubmitField(label="Submit")

