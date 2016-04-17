from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

#taggit
from taggit.managers import TaggableManager
'''
#Command in the  shell to create Blog ' Post

import random
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from faker import Factory
fake = Factory.create()
s = ' '

user = User.objects.first()
for item in range(1,40):
    author = fake.name()
    title = s.join(fake.words(random.randint(4,16)))
    slug = slugify(title)
    #slugify the title
    status = 'published'
    body = s.join(fake.paragraphs(random.randint(2,10)))
    book = Post.objects.create(title=title, author=user, status=status, body=body, slug=slug )
    print(author)
    book.save()
    #Creating Tags
    #Retrieve the last saved Post
    p = Post.objects.first() #last saved Post
    available_tags = ['music', 'tango', 'hip hop', 'country', 'jazz']
    for i in range(0, random.randint(0,5)):
        pick_a_tag = random.choice(available_tags)
        if pick_a_tag not in p.tags.all():
            p.tags.add(pick_a_tag)        
    #creating Comments
    for sug in range(1,3):
        name = fake.name()
        email = fake.email()
        body = s.join(fake.paragraphs(random.randint(1,3)))
        comment = Comment.objects.create(post=p, name=name, email=email, body=body)
        comment.save()

####
#Delete Post and comments
comments = Comment.objects.all()
for i in comments:
    i.delete()

posts = Post.objects.all()
for i in posts:
    i.delete()
'''

# Create your models here.

class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
            )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    tags = TaggableManager()

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()


    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, 
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug])



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


