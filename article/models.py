from django.db import models
from django.core.urlresolvers import reverse

from markdown import markdown
# Create your models here.

class Article(models.Model) :
    title = models.CharField(max_length = 100)  
    category = models.CharField(max_length = 50, blank = True)  
    pub_date = models.DateTimeField(auto_now_add = True)  
    content = models.TextField(blank = True, null = True)  

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'year': self.pub_date.strftime("%Y"), 
                                                'month': self.pub_date.strftime('%m'), 
                                                'day': self.pub_date.strftime('%d'), 
                                                'title': self.title})
    
#    def save(self):
#      self.html = markdown(self.content, 'native')
#      super(Entry, self).save()

    def __str__(self) :
        return self.title

    class Meta:  
        ordering = ['-pub_date']
