from django.contrib.syndication.views import Feed
from blog.models import Post


class BlogFeed(Feed):
    title = "Silvan Adrian"
    link = "http://silvanadrian.ch"
    description = "Blogposts vom Blog"
    
    def items(self):
        return Post.objects.order_by('-date_created')[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.text_html
    
    # item_link is only needed if NewsItem has no get_absolute_url method.
    #def item_link(self, Post):
#   return reverse('post-item', args=[item.pk])

