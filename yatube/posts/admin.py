from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Group

class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке.
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
        )
    # Это позволит изменять поле "group" в любом посте без
    # лишних движений мышкой, прямо из списка постов.
    list_editable = ('group',)    
    # Добовляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате.
    list_filter = ('pub_date',)
    # На случай пустого поля
    empty_value_display = '-пусто-'



admin.site.register(Post, PostAdmin,)
admin.site.register(Group,) 