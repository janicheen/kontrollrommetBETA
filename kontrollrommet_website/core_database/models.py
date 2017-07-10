# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


### Category lists### 
# Personfunction categories
class PersonfunctionCategory(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.name)

# Entity categories
class EntityCategory(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.name)

# EntityToProperty function categories
class EntityToPropertyRelationCategory(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.name)

### Indexes ###
# Person index

class Person(models.Model):
	#id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

# Singal listener, automatic adds User to Person on creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

# Signal listener, automatic edits user in person.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    relatedperson = Person.objects.get(user=instance)
    relatedperson.user = instance
    relatedperson.save()

# Entity index
class Entity(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	category = models.ForeignKey(EntityCategory, on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.name)

# Property index
class Property(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.name)

### Relation Tables
# Person to Entity relation
class PersonToEntityRelation(models.Model):
	#id = models.AutoField(primary_key=True)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
	function = models.ForeignKey(PersonfunctionCategory, on_delete=models.CASCADE)

# Entity to Property relation
class EntityToPropertyRelation(models.Model):
	#id = models.AutoField(primary_key=True)
	entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
	propertyitem = models.ForeignKey(Property, on_delete=models.CASCADE)
	relation = models.ForeignKey(EntityToPropertyRelationCategory, on_delete=models.CASCADE)



