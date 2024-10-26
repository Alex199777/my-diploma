
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product



# Create your views here.
def good_index(request, category_slug=None, ):
    #Создаем переменную по ключу page и текущей странией 1
    page = request.GET.get('page', 1)
    #Создаем переменные для поиска по фильтру
    on_sale = request.GET.get('on_sale', None)#None Если пользователь не выбрал пункт
    order_by = request.GET.get('order_by', None)  # None Если пользователь не выбрал пункт

    #Создаем переменную для формы поиска
    query = request.GET.get('q', None)
    # Если слаг категории все товары получаем запрос на вывод всех объектов
    if category_slug == 'vse-tovary':
        goods = Product.objects.all()

    #Если есть запрос поиска
    elif query:

        def query_search(query):
            '''Для получения запросов из базы данных'''
            #Поиск по id
            if query.isdigit():
                return Product.objects.filter(id=int(query))#переводим полученный запрос в интовое значение

            #Поиск по названию
            elif query.isalpha():
                return Product.objects.filter(name__contains=query)#Если название содержит query получаем товары

            else:
                return None


        goods = query_search(query)



    else:
        goods = Product.objects.filter(category__slug=category_slug)

    #Если выбран пункт акция добавляем к goods фильтрацию по полю discount great than - 0
    if on_sale:
        goods = goods.filter(discount__gt=0)
    #Если выбран пункт фильтрации по цене и не равна значению default добавляем фильтрацию  order_by(price)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    #Создаем переменную для пагинации страниц передаем ей queryset и кол-во отображаемых товаров
    paginator = Paginator(goods, 4)

    #Создаем переменную для вывода текущей страницы
    current_page = paginator.page(page)

    #Передаем в контекст текущую страницу
    context = {'goods': current_page,
               'slug_url': category_slug }
    return render(request, 'good_index.html', context)




def good_detail(request, good_slug):
    good = Product.objects.get(slug=good_slug)
    context = {
        'good':good,
    }
    return render(request, 'good_detail.html', context)