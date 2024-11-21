from django.shortcuts import render, redirect

vendor = 'Айболит'
common_context = {
    'mainpage': 'Главная страница',
    'drugs': 'Наши препараты',
    'cart': 'Корзина',
    'copyright': f' 2024 Аптека "{vendor}". Все права защищены.',
}


# Create your views here.
def root(request):
    return redirect(index)


def index(request):
    context = common_context | {
        'title': f'{vendor} - лучшая аптека города',
        'header': f'Аптека "{vendor}"',
        'welcome_head': 'Добро пожаловать в нашу аптеку!',
        'welcome': 'Мы предлагаем широкий ассортимент качественных лекарственных средств '
                   'и косметических товаров по доступным ценам.',
        'partners_head': 'Наши партнёры',
        'partners': ['Яндекс.Директ',
                     'Google.Analytics',
                     'VK Play',
                     ],
        'advantages_head': 'Наши преимущества',
        'advantages': ['Квалифицированные консультанты',
                       'Удобное расположение',
                       'Быстрая доставка',
                       'Гарантия качества',
                       ]
    }
    return render(request, 'fourth_task/index.html', context)


def drags(request):
    context = common_context | {
        'title': f'{common_context['drugs']} - {vendor}',
        'header': common_context['drugs'],
        'products_head': f'{common_context['drugs']}:',
        'products': ['Витамины Омега-3',
                     'Крем для лица с гиалуроновой кислотой',
                     'Противовирусный препарат',
                     ],
        'buy': 'Купить',
    }
    return render(request, 'fourth_task/drags.html', context)


def cart(request):
    context = common_context | {
        'title': f'{common_context['cart']} - {vendor}',
        'header': common_context['cart'],
        'cart_head': f'{common_context['cart']}:',
        'empty': 'Ваша корзина пуста',
    }
    return render(request, 'fourth_task/cart.html', context)
