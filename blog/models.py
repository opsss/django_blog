from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='url')
    parent = TreeForeignKey('self', null=True, blank=True, verbose_name='подкатегория', db_index=True)

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название статьи')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='url')
    category = models.ForeignKey(Category, verbose_name='Категория')
    preview = RichTextUploadingField('Анонс статьи')
    text = RichTextUploadingField('Полная статья')
    pub_date = models.DateTimeField(verbose_name='Создан')

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ("-pub_date", )

    def __str__(self):
        return self.title





