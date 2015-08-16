from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from markdown import markdown
from django.template.defaultfilters import slugify
from django.db.models import permalink
from django.db.models.signals import post_save
from django.conf import settings


#Twitter Authentification
from twython import Twython
twitter = Twython('hCkbdXZwdoFoIJsQqANRQ', 'mccOHaIdUEH8hsLoX0VtYe3sjlgfaX2RiChHT02rg','163400534-6PVteKAIQZVGmU2drQZJ0huwU2nBYS0UWbY7qAxW', 'pP7pa4UH0klP8JlOFmYBL5JhlJkLxmZ0qcreSohjulsig')



# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = u'tag'
        verbose_name_plural = u'tags'
        ordering = ['name']
    
    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(u'title', max_length=255)
    text = models.TextField(u'text',blank=True)
    is_public = models.BooleanField(u'public', default=True)
    date_created = models.DateTimeField(u'date created')
    date_updated = models.DateTimeField(u'date updated')
    owner = models.ForeignKey(User, verbose_name=u'owner', related_name='blogposts')
    tags = models.ManyToManyField(Tag,blank=True)
    text_html = models.TextField(editable=False, blank=True,null=True)
    slug = models.SlugField(unique=True, blank=True)
    send_tweet = models.BooleanField(u'tweet senden')
    sent_tweet = models.BooleanField(u'tweet gesendet')

    class Meta:
        verbose_name = u'post'
        verbose_name_plural = u'posts'
        ordering = ['-date_created']


    def __unicode_(self):
        return u'%s (%s)' % (self.title,self.text)
 
 
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        if not self.slug:
            self.slug = slugify(self.title)
        self.text_html = markdown(self.text, ['codehilite'])
        if self.is_public is True:
            if self.send_tweet is True:
                if not self.sent_tweet:
                    self.sent_tweet = True
                    twitter.update_status(status= 'Neuer Blogpost:' + ' ' + self.title + '\n' + 'http://silvanadrian.ch' + self.get_absolute_url())
        super(Post, self).save(*args, **kwargs)




