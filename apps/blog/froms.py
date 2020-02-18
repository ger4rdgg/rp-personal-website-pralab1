from django import forms

class CommentForm(form.Form):

    author =form.CharField(
        max_length=70,
        widget= forms.TextField
    )
