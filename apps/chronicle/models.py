from django.db import models

# Create your models here.
class Chronicle(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    current_date = models.DateField()

class Character(models.Model):
    name = models.CharField(max_length=25)
    
    pc = models.BooleanField()

    relationships = models.ManyToManyField('Character', through='CharacterRelationship')


class CharacterRelationship(models.Model):
    class Meta:
        unique_together = (('character1', 'character2'),)

    character1 = models.ForeignKey(Character, on_delete=models.CASCADE)
    character2 = models.ForeignKey(Character, on_delete=models.CASCADE)

    FEELING_CHOICES = [
        ('Love', (
            ('lover', 'Lover'),
            ('married', 'Married')
        )),
        ('enemy', 'Enemy'),
        ('friend', 'Friend')
    ]

    feeling = models.CharField(max_length=10, choices=FEELING_CHOICES)


class CharacterComponent(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    class Meta:
        abstract = Trues


class VampireClan(models.Model):
    name = models.CharField(max_length=10)

class VampireCC(CharacterComponent):
    clan = models.ForeignKey(VampireClan)
    sire = models.ForeignKey(Character)

    embrace_date = models.DateTimeField()

class HumanCC(CharacterComponent):
    birth_date = models.DateTimeField()


class Location(models.Model):
    name = models.CharField(max_length=25)
