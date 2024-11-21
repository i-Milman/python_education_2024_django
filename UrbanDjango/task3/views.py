from django.shortcuts import render, redirect

vendor = 'Айболит'
common_context = {
    'style': """
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #007bff;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        h1 {
            margin: 0;
        }
        nav {
            background-color: #f2f2f2;
            padding: 10px;
            text-align: center;
        }
        nav a {
            color: #333;
            text-decoration: none;
            padding: 10px 20px;
            margin: 0 10px;
        }
        nav a:hover {
            background-color: #007bff;
            color: #fff;
        }
        main {
            padding: 20px;
        }
        section {
            margin-bottom: 40px;
        }
        h2 {
            color: #007bff;
        }
        button {
            padding: 10px 20px;
            text-align: center;
        }
        footer {
            background-color: #007bff;
            color: #fff;
            padding: 10px;
            text-align: center;
        }
    """,
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
        'title_in': f'Аптека "{vendor}"',
    }
    return render(request, 'third_task/index.html', context)


def drags(request):
    context = common_context | {
        'title': f'{common_context['drugs']} - {vendor}',
    }
    return render(request, 'third_task/drags.html', context)


def cart(request):
    context = common_context | {
        'title': f'{common_context['cart']} - {vendor}',
    }
    return render(request, 'third_task/cart.html', context)
