from django.urls import path
from . import views

urlpatterns = [
    path('createContacts', views.createContact, name="createContact"), # get the Contacts a user
    path('updateContact', views.updateContact, name="updateContact"), # call it when we are editing
    path('trashContact', views.trashContact, name="trashContacts"), # handles the soft deletion of the contact
    path('emptyContactTrash', views.emptyContactTrash, name="destroyContact"), # completely delete it from your system
    path('archiveContact', views.archiveContact, name="archiveContact"),
    path('getUserContact', views.getUserContact, name="getUserContact"), 

]