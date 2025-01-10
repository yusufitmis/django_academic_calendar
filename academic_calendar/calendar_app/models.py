from django.db import models

class Calendar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    SEMESTER_CHOICES = [
        ('Güz', 'Güz Yarıyılı'),
        ('Bahar', 'Bahar Yarıyılı'),
    ]

    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(null=True, blank=True)  # Güz Yarıyılı Başlangıç Tarihi
    end_date= models.DateTimeField(null=True, blank=True)  # Güz Yarıyılı Bitiş Tarihi
    start_date_bahar = models.DateTimeField(null=True, blank=True)  # Bahar Yarıyılı Başlangıç Tarihi
    end_date_bahar = models.DateTimeField(null=True, blank=True)  # Bahar Yarıyılı Bitiş Tarihi
    calendar = models.ForeignKey(Calendar, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


