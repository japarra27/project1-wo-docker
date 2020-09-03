from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for v0_back."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class Company(User):
    company_name = models.CharField(max_length=150)

    # class Meta:
    #     proxy = True

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=250)
    project_price = models.DecimalField(max_digits=10, decimal_places=2)
    project_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

class Design(models.Model):
    design_creation_date = models.DateTimeField(auto_now_add=True)
    designer_first_name = models.CharField(max_length=50)
    designer_last_name = models.CharField(max_length=50)
    designer_email = models.EmailField()
    design_file = models.FileField(upload_to='Designs/')
    design_price = models.DecimalField(max_digits=10, decimal_places=2)
    design_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_state = models.CharField(max_length=15, default="En Proceso")

    def __str__(self):
        return self.designer_first_name


