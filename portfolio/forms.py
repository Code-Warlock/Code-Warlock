from django import forms
from .models import BlogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 dark:bg-warlock-bg border border-gray-300 dark:border-gray-700 rounded-lg p-3 focus:outline-none focus:border-blue-500 dark:focus:border-warlock-green text-gray-900 dark:text-white',
                'placeholder': 'Your Name'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-gray-100 dark:bg-warlock-bg border border-gray-300 dark:border-gray-700 rounded-lg p-3 focus:outline-none focus:border-blue-500 dark:focus:border-warlock-green text-gray-900 dark:text-white',
                'placeholder': 'Share your thoughts...',
                'rows': 4
            })
        }