from django.db import models


class Project(models.Model):
    """
    OUTPUT:
    --------------------
    A project has a title, description, technology and image. Hence, cards can be built
    when the model is initialised.
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
