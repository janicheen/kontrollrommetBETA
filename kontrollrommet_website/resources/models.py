"""
This module defines the core triangular model of Person-Entity-Property.
It icludes the core models, relational models and category models to go with it.
It also contains signal listeners that to automatic operations on core models
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Django dependencies
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
#Django User model
from django.contrib.auth.models import User

### Category models### 

# Person Category (NOT relational status).
@python_2_unicode_compatible  # only if you need to support Python 2
class PersonCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

# Entity Category
@python_2_unicode_compatible  # only if you need to support Python 2
class EntityCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

# Property Category
@python_2_unicode_compatible  # only if you need to support Python 2
class PropertyCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

# Person-to-Entity relation category
@python_2_unicode_compatible  # only if you need to support Python 2
class PersonToEntityRelationCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

# Entity-to-Property relation category
@python_2_unicode_compatible  # only if you need to support Python 2
class EntityToPropertyRelationCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

# Property-to-Person relation category
@python_2_unicode_compatible  # only if you need to support Python 2
class PropertyToPersonRelationCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

### Core Tables ###

# Person Table
@python_2_unicode_compatible  # only if you need to support Python 2
class Person(models.Model):
    # Basic credentials
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    category = models.ForeignKey(EntityCategory, on_delete=models.CASCADE, null=True, blank=True,)
    #Attatched user identification
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    # Decorator that defines full_name as a model property
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s' % (self.full_name)

# Entity Table
@python_2_unicode_compatible  # only if you need to support Python 2
class Entity(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(EntityCategory, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

# Property Table
@python_2_unicode_compatible  # only if you need to support Python 2
class Property(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

### Relation Tables

# Person-to-Entity relation
@python_2_unicode_compatible  # only if you need to support Python 2
class PersonToEntityRelation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    relation_category = models.ForeignKey(PersonToEntityRelationCategory, on_delete=models.CASCADE)
    #created_time =
    def __str__(self):
        return '%s - %s - %s' % (self.person, self.relation_category, self.entity)

# Entity-to-Property relation
class EntityToPropertyRelation(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    _property = models.ForeignKey(Property, on_delete=models.CASCADE)
    relation_category = models.ForeignKey(EntityToPropertyRelationCategory, on_delete=models.CASCADE)
    #created_time = 
    def __str__(self):
        return '%s - %s - %s' % (self.entity, self.relation_category, self._property)

# Property-to-Person relation
class PropertyToPersonRelation(models.Model):
    _property = models.ForeignKey(Property, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    relation_category = models.ForeignKey(PropertyToPersonRelationCategory, on_delete=models.CASCADE)
    #created_time = 
    def __str__(self):
        return '%s - %s - %s' % (self._property, self.relation_category, self.person)


### Signal listeners that perform automatic operations on models

# Singal listener that automatically creates related Person instance, when new user is created 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('my_signal received')
    if created:
        Person.objects.create(
            user=instance, 
            first_name=instance.first_name, 
            last_name=instance.last_name,
            )

# Signal listener, that automatically edits user entry in Person instance, when user is edited.
# PS! Should be looked at. As long as the ID(primary key) is permanent, user data and person data can be edited separately, and be linked together.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    relatedperson = Person.objects.get(user=instance)
    relatedperson.user = instance
    relatedperson.save()
