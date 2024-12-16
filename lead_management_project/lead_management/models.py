from django.db import models
# Create your models here.
# Lead Model
# Example: If your Lead model looks something like this:
# Add a constant to define possible status choices
STATUS_CHOICES = (
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('completeed', 'Completed'),
    ('lost', 'Lost'),
)
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    source = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    
    # Add any other fields you need

    def __str__(self):
        return self.name

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Sales Pipeline Model
class SalesPipeline(models.Model):
    LEAD = 'Lead'
    PROSPECT = 'Prospect'
    CUSTOMER = 'Customer'

    # STATUS_CHOICES = [
    #     (LEAD, 'Incompleted'),
    #     (PROSPECT, 'Completed'),
    #     (CUSTOMER, 'Inprogess'),
    # ]
    
    STATUS_CHOICES = (
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('completeed', 'Completed'),
    
    ('lost', 'Lost'),
    )
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    stage = models.CharField(max_length=50, choices=STATUS_CHOICES, default=LEAD)
    progress = models.IntegerField(default=0)  # Progress in % (0-100)
    
    def __str__(self):
        return f"{self.lead.name} - {self.stage}"
