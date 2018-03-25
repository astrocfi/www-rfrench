from django.db import models

class PaperCategory(models.Model):
    name = models.CharField(max_length=120)
    display_order = models.IntegerField(unique=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return str(self.display_order) + ':  ' + self.name

class PaperSubCategory(models.Model):
    category = models.ForeignKey('PaperCategory', on_delete=models.PROTECT)
    name = models.CharField(max_length=120)
    display_order = models.IntegerField()

    class Meta:
        ordering = ['category', 'display_order']

    def __str__(self):
        return (self.category.name + ' - ' + str(self.display_order) +
                ': ' + self.name)

class Paper(models.Model):
    sub_category = models.ForeignKey('PaperSubCategory', on_delete=models.PROTECT)
    display_order = models.IntegerField()
    doc_type = models.CharField(max_length=255)
    year = models.IntegerField()
    title = models.CharField(max_length=255)
    citation = models.CharField(max_length=120, blank=True)
    authors = models.CharField(max_length=255, blank=True)
    full_text_link = models.CharField(max_length=255, blank=True)
    journal_link = models.CharField(max_length=255, blank=True)
    abstract_link = models.CharField(max_length=255, blank=True)
    arXiv_link = models.CharField(max_length=255, blank=True)
    ADS_link = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['sub_category', 'display_order']

    def __str__(self):
        return (str(self.display_order) + ' - ' + str(self.year) + ': ' +
                str(self.title) + ' @ ' + self.citation +
                ' [' + self.sub_category.name + ']')
