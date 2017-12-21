from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Relation(models.Model):
    RELATIONSHIP_CHOICES = (
        ('00', 'Husband'),
        ('01', 'Wife'),
        ('02', 'Son'),
        ('03', 'Daughter'),
        ('04', 'Father'),
        ('05', 'Mother'),
        ('06', 'Brother'),
        ('07', 'Sister'),
    )
    source = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='source')
    target = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='target')
    relationship = models.CharField(max_length=2, choices=RELATIONSHIP_CHOICES)

    def __str__(self):
        return '%s is %s of %s' % (self.source, self.get_relationship_name(), self.target)

    def get_relationship_name(self):
        for choice in Relation.RELATIONSHIP_CHOICES:
            if choice[0] == self.relationship:
                return choice[1]
        else:
            return 'Unknown'
