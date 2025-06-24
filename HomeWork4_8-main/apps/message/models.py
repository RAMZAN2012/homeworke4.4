from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(
        max_length= 100,
        verbose_name= "Имя"
    )
    text = models.CharField(
        max_length=500,
        verbose_name= "Сообщение"
    )
    created_at = models.DateTimeField(
        auto_now_add= True
    )

    likes = models.PositiveIntegerField(
        default=0,
        verbose_name= "Лайки"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= "Сообщение"
        verbose_name="Сообщения"