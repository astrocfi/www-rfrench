from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    link = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title) + ' @ ' + str(self.location)

class Gig(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    low_level = models.CharField(max_length=3)
    high_level = models.CharField(max_length=3, blank=True)
    event = models.ForeignKey('Event', on_delete=models.PROTECT)
    callers = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return (str(self.start_date) + ' ' + self.event.title + ' (' +
                self.low_level + '-' + self.high_level + ') @ ' +
                self.event.location)

    def pretty_level(self):
        if self.high_level == '':
            return self.low_level
        return self.low_level + ' - ' + self.high_level

    def pretty_date(self):
        start = self.start_date.strftime('%m/%d')
        if self.end_date is None:
            return start
        end = self.end_date.strftime('%m/%d')
        return start + ' - ' + end

    def full_date(self):
        return self.start_date.strftime('%y-%m-%d')

    def year(self):
        return self.start_date.year

    def title(self):
        return self.event.title

    def link(self):
        return self.event.link

    def location(self):
        return self.event.location
