import uuid
from django.db import models


"""
    Modèle 'Person' de l'application uploads, comprenant en attributs de classe: un prénom, un nom de famille et un uuid, c'est-à-dire une méthode
    permettant une identification unique cryptée.
"""


class Person(models.Model):
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return  f"{self.first_name}, {self.last_name}"


"""
    Modèle 'File' de l'application uploads, comprenant en attributs de classe: un titre, un contenu correspondant au fichier uploadé, et un rattachement 
    au modèle Person par l'utilisation d'une méthode ForeignKey.
"""


class File(models.Model):

    title = models.CharField(max_length=50, null=True)
    content = models.FileField(upload_to="document/")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.content}"


"""
class PersonModel(Person):
      user = uuid.uuid4()
"""
