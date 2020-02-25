from django.db import models

# Create your models here.
from customuser.models import MyUser

case_choices = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('postphoned', 'PostPhoned'),
        ('closed', 'Closed')
        )


class Case(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    registered_by=models.ForeignKey(MyUser,related_name='appealer', on_delete=models.CASCADE)

    first_lawyer = models.ForeignKey(MyUser,related_name='first_lawyer', on_delete=models.CASCADE)
    second_lawyer = models.ForeignKey(MyUser,related_name='second_lawyer', on_delete=models.CASCADE)

    witness = models.ManyToManyField(MyUser, related_name='witness' ,null=True, blank=True)

    hearing_date = models.DateTimeField()
    case_status = models.CharField(choices=case_choices, default="p", max_length=100)

    def __str__(self):
        return self.name+str(self.hearing_date)

