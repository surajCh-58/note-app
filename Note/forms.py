from django import forms
from .models import *

INPUT_CLASS = (
    "w-full bg-slate-800 border border-slate-700 text-slate-100 "
    "placeholder-slate-500 rounded-lg px-4 py-2.5 text-sm "
    "focus:outline-none focus:ring-2 focus:ring-amber-400 focus:border-transparent "
    "transition duration-150"
)

TEXTAREA_CLASS = (
    "w-full bg-slate-800 border border-slate-700 text-slate-100 "
    "placeholder-slate-500 rounded-lg px-4 py-3 text-sm resize-none "
    "focus:outline-none focus:ring-2 focus:ring-amber-400 focus:border-transparent "
    "transition duration-150"
)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Note title…',
                'class': INPUT_CLASS,
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your note here…',
                'rows': 8,
                'class': TEXTAREA_CLASS,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': INPUT_CLASS})
        self.fields['content'].widget.attrs.update({'class': TEXTAREA_CLASS})
