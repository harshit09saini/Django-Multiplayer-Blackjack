from django import forms


class Room(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'uk-input uk-width-1-1'

    CHOICES = (("Join Room", "Join Room"), ("Create Room", "Create Room"),)
    room_choice = forms.ChoiceField(label='Room Choice', choices=CHOICES)

    room_code = forms.CharField(label="Room Code",
                                widget=forms.TextInput(attrs={'placeholder': 'Enter a Room Code'}),
                                initial=None)
