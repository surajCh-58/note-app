from django.shortcuts import *
from . models import *
from . forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def AddNote(request,pk=None):
    instance=get_object_or_404(Note,id=pk) if pk else None
    if request.method=="POST":
        form=NoteForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("Note:dashboard")
    else:
        form=NoteForm(instance=instance)
    return render(request,"AddNote.html",{'form':form})
@login_required
def AllNote(request):
    note=Note.objects.all()
    return render(request,"dashboard.html",{'notes':note})
def DeleteNote(request,pk):
    note=get_object_or_404(Note,id=pk)
    note.delete()
    return redirect("Note:dashboard")