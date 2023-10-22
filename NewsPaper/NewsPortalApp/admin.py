from django.contrib import admin
from .models import Post, Category, Author

# напишем уже знакомую нам функцию обнуления товара на складе
# def nullfy_quantity(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
#     queryset.update(quantity=0)
#     nullfy_quantity.short_description = 'Обнулить товары' # описание для более понятного представления в админ панеле задаётся, как будто это объект

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('header', 'rating')  # генерируем список имён всех полей для более красивого отображения
    list_filter = ('rating', 'header')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('header', 'category__titles')  # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
