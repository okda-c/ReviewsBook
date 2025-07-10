from django import forms

from reviews.models import Review

"""
class ReviewForm(forms.Form):
    name = forms.CharField(max_length=30, label='имя америконца')
    email = forms.EmailField()
    review = forms.CharField(widget=forms.Textarea,label="отзыв пж")
    rating = forms.IntegerField(max_value=10, min_value=1, label = "поставьте оценку")
"""

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=('name','email','review','rating')
        widgets={"rating":forms.NumberInput(attrs={"min":1,"max":10})}