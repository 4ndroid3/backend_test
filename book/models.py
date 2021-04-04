""" Book Models"""

# Django Imports
from django.db import models


class Library(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'


class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey('book.Author', on_delete=models.CASCADE)
    libraries = models.ManyToManyField('book.Library')

    def __str__(self):
        return '{} - {}'.format(self.title, self.author)


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Leads(models.Model):
    """ Modelo de Lead
    Campos:
    - email
    - full_Name
    - phone
    - library (fk)
    """
    email = models.EmailField(
        unique=True,
        error_messages={
            'Unico' : 'Ya existe un usuario con esa dirección de Email.'
        }
    )

    full_name = models.CharField(
        max_length=50,
        verbose_name='Nombre y Apellido',
        help_text='Nombre completo',
    )

    phone = models.CharField(
        max_length=17,
        blank=True,
        verbose_name='Numero de Teléfono',
        help_text='Numero de Teléfono del usuario',
    )

    library = models.ForeignKey(
        'Library',
        on_delete=models.CASCADE,
        verbose_name='Libreria',
        help_text='Libreria del Usuario',
    )

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
     