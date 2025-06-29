from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=30, label='имя америконца')
    email = forms.EmailField()
    review = forms.CharField(widget=forms.Textarea,label="отзыв пж")