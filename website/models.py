from django.db import models
from decimal import Decimal
import datetime
from datetime import timedelta
from datetime import datetime as dt
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 10

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))

# Create your models here.

class Portfolio(models.Model):
	port_format = (
		('Image', 'Image'),
		('Youtube', 'Youtube'),
		('Slide', 'Slide'),
		('Video', 'Video'),
	)
	port_type = (
		('Website', 'Website'),
		('Mobile App', 'Mobile App'),
		('Graphic', 'Graphic'),
		('Digital Marketing', 'Digital Marketing'),
	)
	pro = (
		('On-going', 'On-going'),
		('Completed', 'Completed'),
		('Submitted', 'Submitted'),
	)
	p_format = models.CharField(max_length=100, default='Slide', choices=port_format)
	display_image = models.ImageField(upload_to='portfolio', default='', null=True)
	image = models.ManyToManyField('SlideImage', blank=True)
	p_type = models.CharField(max_length=100, default='Website', choices=port_type)
	project_name = models.CharField(max_length=100, default='')
	slug = models.SlugField(max_length=100, default='', null=True)
	client = models.CharField(max_length=100, default='')
	link = models.URLField(default='null', blank=True)
	duration = models.CharField(max_length=100, default='')
	progress = models.CharField(max_length=100, default='', choices=pro)
	tech = models.CharField(max_length=200, default='')
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

	def __str__(self):
		return self.project_name

class SlideImage(models.Model):
	porfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default=None)
	image = models.ImageField(upload_to='portfolio', default='', null=True)

	def __str__(self):
		return self.portfolio.project_name


class Category(models.Model):
	name = models.CharField(max_length=100, default='')
	desc = models.TextField(default='', blank=True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name


class Blog(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=100, default='')
	image = models.ImageField(upload_to='blogs', default='', null=True)
	slug = models.SlugField(default='')
	tags = models.TextField(default='', blank=True)
	content = models.TextField(default='')
	date = models.DateField(auto_now_add=True)
	comment_count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title

class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=None)
	name = models.CharField(max_length=100, default='')
	email = models.EmailField(default='')
	content = models.TextField(default='')
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name
@receiver(pre_save, sender=Comment)
def update_comment_count(sender, instance, *args, **kwargs):
	print(instance.blog.id)
	get_old_count = Blog.objects.get(id=instance.blog.id)
	add_new_count = int(get_old_count.comment_count) + 1
	Blog.objects.filter(id=instance.blog.id).update(comment_count=add_new_count)


class Reply(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None)
	name = models.CharField(max_length=100, default='')
	email = models.EmailField(default='')
	content = models.TextField(default='')
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Replies"

	def __str__(self):
		return self.name


class PaymentCode(models.Model):
	code = models.CharField(max_length=100, default='', blank=True)
	firstname = models.CharField(max_length=100, default='')
	lastname = models.CharField(max_length=100, default='', blank=True)
	email = models.EmailField(default='', null=True)
	mobile = models.CharField(max_length=100, default='', null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
	description = models.TextField(default='', blank=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.firstname + ' ' + self.lastname

# @receiver(pre_save, sender=PaymentCode)
# def update_ref_slug(sender, instance, **kwargs):
#     random_string = generate_random_string()
#     instance.code = random_string
