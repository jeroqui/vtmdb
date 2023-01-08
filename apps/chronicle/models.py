from django.db import models

# Create your models here.
class Chronicle(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    current_date = models.DateField()

    def __str__(self):
        return self.name


class ChronicleData(models.Model):
    chronicle = models.ForeignKey(Chronicle, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Character(ChronicleData):
    name = models.CharField(max_length=25)

    story = models.TextField(null=True, blank=True)
    
    pc = models.BooleanField()

    relationships = models.ManyToManyField('Character', through='CharacterRelationship')

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name

class VampireCC(CharacterComponent):
    clan = models.ForeignKey(VampireClan, on_delete=models.CASCADE)
    sire = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='vampire_sire')

    title = models.CharField(max_length=50, null=True, blank=True)

    embrace_date = models.DateTimeField(null=True, blank=True)

class HumanCC(CharacterComponent):
    birth_date = models.DateTimeField()


class Plot(ChronicleData):
    name = models.CharField(max_length=25)
    description = models.TextField()


class PlotStages(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    description = models.TextField()


class Location(ChronicleData):
    name = models.CharField(max_length=25)
