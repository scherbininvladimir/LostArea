from django.db import models

from users.models import UserProfile


class Scene(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сцена'
        verbose_name_plural = 'Сцены'



class Request(models.Model):
    FORMATS = (
        ('S', 'Сольное выступление'),
        ('G', 'Группа'),
    )
    name = models.CharField(max_length=50)
    text = models.TextField()
    format = models.CharField(
        max_length=1,
        choices=FORMATS
    )
    desired_scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Voice(models.Model):
    VOICES = (
        ('YES', 'За'),
        ('NO', 'Против'),
        ('ABS', 'Воздержался'),
    )
    censor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    voice = models.CharField(
        max_length=2,
        choices=VOICES)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'


class TimeSlot(models.Model):
    SLOTS = (
        ('D', 'День'),
        ('E', 'Вечер'),
        ('LE', 'Поздний вечер')
    )
    day = models.PositiveSmallIntegerField()
    time = models.CharField(
        max_length=2,
        choices=SLOTS
    )


class SceneSlot(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()

