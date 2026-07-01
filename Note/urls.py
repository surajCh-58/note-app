from django.urls import path
from . import views
app_name="Note"
urlpatterns = [
    path('addnote',views.AddNote,name="addnote"),
    path('editnote/<int:pk>',views.AddNote,name="editnote"),
    path('deletenote/<int:pk>',views.DeleteNote,name="deletenote"),
    path('',views.AllNote,name="dashboard")
]
