from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=200)
    project_github_link = models.URLField(max_length=300)

    def __str__(self):
        return self.title
