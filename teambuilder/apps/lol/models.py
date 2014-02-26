from django.db import models


class ChampionManager(models.Manager):
    def getChampionById(self, id):
        return None

class Champion(models.Model):
    name = models.CharField(verbose_name='Name', max_length=30)
    riot_id = models.IntegerField(verbose_name="Riot's id", max_length=10)
    difficulty_rank = models.IntegerField(verbose_name='Difficulty level', max_length=2)
    magic_rank = models.IntegerField(verbose_name='Magic level', max_length=2)
    attack_rank = models.IntegerField(verbose_name='Attack level', max_length=2)
    defense_rank = models.IntegerField(verbose_name='Defense level', max_length=2)
    image = models.ImageField(verbose_name='Image', upload_to='teambuilder/app/lol/static/img/champion/')

    objects = ChampionManager()

    REQUIRED_FIELDS = ['name', 'riot_id']

    class Meta:
        app_label='lol'
        db_table = 'champion'
        verbose_name = 'Champion'
        verbose_name_plural = 'Champions'
        ordering = ['name',]

    def __unicode__(self):
        return self.name

