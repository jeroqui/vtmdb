from django.db import models

# Create your models here.
class Chronicle(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    current_date = models.DateField()


class ChronicleData(models.Model):
    chronicle = models.ForeignKey(Chronicle, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Character(ChronicleData):
    name = models.CharField(max_length=25)
    
    pc = models.BooleanField()

    relationships = models.ManyToManyField('Character', through='CharacterRelationship')


class CharacterRelationship(models.Model):
    class Meta:
        unique_together = (('character1', 'character2'),)

    character1 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='relationship_character1')
    character2 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='relationship_character2')

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
        abstract = True


class VampireClan(models.Model):
    name = models.CharField(max_length=10)

class VampireCC(CharacterComponent):
    clan = models.ForeignKey(VampireClan, on_delete=models.CASCADE)
    sire = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, related_name='vampire_sire')

    embrace_date = models.DateTimeField()

class HumanCC(CharacterComponent):
    birth_date = models.DateTimeField()


class Location(ChronicleData):
    name = models.CharField(max_length=25)
