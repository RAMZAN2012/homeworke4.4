from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип"
    )
    banner = models.ImageField(
        upload_to='banner',
        verbose_name="Баннер"
    )
    facebook = models.URLField(
        verbose_name="facebook"
    )
    twitter = models.URLField(
        verbose_name="twitter"
    )
    google = models.URLField(
        verbose_name="google"
    )
    linkedin = models.URLField(
        verbose_name="linkedin"
    )    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        
        
class Gallary(models.Model):
    image = models.ImageField(
        upload_to="image/",
        verbose_name="Изображение"
    )
    
    def __str__(self):
        return str(self.image)
    
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
        
        
class Form(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="email"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Форма связи"
        verbose_name_plural = "Форма связи"
        
        
class TelegramUser(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользователя telegram"
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        blank=True, null=True
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name="Чат ID"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграма"