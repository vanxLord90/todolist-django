from django.db import models

# Create your models here.
class Todo(models.Model):
    Priority = (('Low','Low'),
                ('Medium','Medium'),
                ('High', 'High'))
    title =  models.CharField(max_length = 120)
    description = models.TextField()
    due_date = models.DateField(default =None, null = True, blank = True )
    priority = models.CharField(max_length = 6,choices = Priority, default ='Low')
    completed = models.BooleanField(default = False)

    def _str_(self):
        return self.title
    