from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from markdown import markdown
from django.template.defaultfilters import slugify
from django.db.models import permalink

# Create your models here.
class Update(models.Model):
    project = models.ForeignKey('Project')
    status = models.TextField(u'status',blank=False)
    is_update = models.BooleanField(u'update', default = False)
    date_created = models.DateTimeField(u'date created')
    date_updated = models.DateTimeField(u'date updated')

    class Meta:
        verbose_name = u'update'
        verbose_name_plural = u'updates'
        ordering = ['-date_created']

    def __unicode_(self):
        return u'%s (%s)' % (self.status)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Update, self).save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(u'title',max_length=255)
    description = models.TextField(u'text',blank=True)
    excerpt = models.TextField(u'excerpt',blank = True)
    url = models.URLField()
    square_image = models.ImageField(upload_to = 'media/img/projects/', default = 'media/img/about.png')
    wide_image = models.ImageField(upload_to = 'media/img/projects/', default = 'media/img/about.png',blank=True)
    is_public = models.BooleanField(u'public', default=False)
    date_created = models.DateTimeField(u'date created')
    date_updated = models.DateTimeField(u'date updated')
    date_started = models.DateTimeField(u'date started',blank=True, null = True)
    date_finished = models.DateTimeField(u'date finished',blank = True, null = True)
    customer = models.ForeignKey(User, verbose_name=u'customer', related_name='customers')
    customername = models.CharField(u'customername',max_length=255)
    description_html = models.TextField(editable=False, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = u'project'
        verbose_name_plural = u'projects'
        ordering = ['-date_created']

    def __unicode_(self):
        return u'%s (%s)' % (self.title,self.description)
    
    @permalink
    def get_absolute_url(self):
        return ('view_project', None, { 'slug': self.slug })

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        if not self.slug:
            self.slug = slugify(self.title)
        self.date_updated = now()
        self.description_html = markdown(self.description, ['codehilite'])
        super(Project, self).save(*args, **kwargs)
