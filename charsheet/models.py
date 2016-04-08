from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.core.urlresolvers import reverse

#from django.contrib.auth.models import User
from djangae.contrib.gauth.datastore.models import GaeDatastoreUser

# Create your models here.

@python_2_unicode_compatible
class Character(models.Model):
    """
    This is the main model for character sheets
    """

    user = models.ForeignKey(GaeDatastoreUser)

    # Char Details
    player_name = models.CharField(max_length=100, blank=True)
    character_name = models.CharField(max_length=100)
    background = models.CharField(max_length=200, blank=True)
    race = models.CharField(max_length=200, blank=True)
    alignment = models.CharField(max_length=200, blank=True)
    experience_points = models.IntegerField(null=True, blank=True)
    max_hit_points = models.IntegerField(null=True, blank=True)
    current_hit_points = models.IntegerField(null=True, blank=True)
    temporary_hit_points = models.IntegerField(null=True, blank=True)
    armor_class = models.IntegerField(null=True, blank=True)
    initiative = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    inspiration = models.IntegerField(null=True, blank=True)
    proficiency_bonus = models.IntegerField(null=True, blank=True)

    # Hit Dice
    hit_dice_total = models.IntegerField(null=True, blank=True)
    hit_dice = models.TextField(blank=True)

    # Death Saves - I may switch this to a many to many field, but for now
    # I don't think it's worth it.
    death_save_success_1 = models.BooleanField(default=0)
    death_save_success_2 = models.BooleanField(default=0)
    death_save_success_3 = models.BooleanField(default=0)
    death_save_failure_1 = models.BooleanField(default=0)
    death_save_failure_2 = models.BooleanField(default=0)
    death_save_failure_3 = models.BooleanField(default=0)

    # Char Description
    age = models.IntegerField(null=True, blank=True)
    height = models.CharField(max_length=200, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    eyes = models.CharField(max_length=200, blank=True)
    skin = models.CharField(max_length=200, blank=True)
    hair = models.CharField(max_length=200, blank=True)
    character_appearance = models.TextField(blank=True)
    character_backstory = models.TextField(blank=True)
    allies_and_organizations = models.TextField(blank=True)
    additional_features_and_traits = models.TextField(blank=True)

    treasure = models.TextField(blank=True) # Not sure if i want this to be a TextField

    # Main Stats
    strength = models.IntegerField(null=True, blank=True)
    dexterity = models.IntegerField(null=True, blank=True)
    constitution = models.IntegerField(null=True, blank=True)
    intelligence = models.IntegerField(null=True, blank=True)
    wisdom = models.IntegerField(null=True, blank=True)
    charisma = models.IntegerField(null=True, blank=True)

    # Skills
    acrobatics = models.BooleanField(default=0)
    animal_handling = models.BooleanField(default=0)
    arcana = models.BooleanField(default=0)
    athletics = models.BooleanField(default=0)
    deception = models.BooleanField(default=0)
    history = models.BooleanField(default=0)
    insight = models.BooleanField(default=0)
    intimidation = models.BooleanField(default=0)
    investigation = models.BooleanField(default=0)
    medicine = models.BooleanField(default=0)
    nature = models.BooleanField(default=0)
    perception = models.BooleanField(default=0)
    performance = models.BooleanField(default=0)
    persuasion = models.BooleanField(default=0)
    religion = models.BooleanField(default=0)
    sleight_of_hand = models.BooleanField(default=0)
    stealth = models.BooleanField(default=0)
    survival = models.BooleanField(default=0)

    personality_traits = models.TextField(blank=True)
    ideals = models.TextField(blank=True)
    bonds = models.TextField(blank=True)
    flaws = models.TextField(blank=True)

    features_and_traits = models.TextField(blank=True)
    other_proficiencies_and_languages = models.TextField(blank=True)

    # Spell Casting Saves
    spell_casting_class = models.CharField(max_length=50, blank=True)
    spellcasting_ability = models.CharField(max_length=50, blank=True)
    spell_save_dc = models.IntegerField(null=True, blank=True)
    spell_attack_bonus = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.character_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class CharacterClass(models.Model):
    """
    Character Class models, Many to One field for character classes
    """
    character = models.ForeignKey(Character)
    char_class = models.CharField(max_length=200)
    level = models.IntegerField(null=True, blank=True)

class Equipment(models.Model):
    character = models.ForeignKey(Character)
    value = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True)

class AttacksAndSpellcasting(models.Model):
    character = models.ForeignKey(Character)
    attack = models.CharField(max_length=50)
    bonus = models.IntegerField(null=True, blank=True)
    damange = models.CharField(max_length=50)
    damage_type = models.CharField(max_length=50)

class Spells(models.Model):
    character = models.ForeignKey(Character)
    level_or_cantrip = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    prepared = models.BooleanField()
