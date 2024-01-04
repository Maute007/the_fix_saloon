from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.cache import cache_control
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def logout_and_show_login(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticação do usuário
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Credenciais válidas, faz o login do usuário
            login(request, user)

            # Verifica o grupo de usuário e redireciona para a página apropriada
            if user.groups.filter(name='Admin').exists():
                return redirect('admin:index')
            elif user.groups.filter(name='gestor').exists():
                return redirect('add_registro')
            else:
                return redirect('add_registro')

        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')



# Frontend
@login_required(login_url='login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def index(request):
    products = Product.objects.all().order_by('-data_de_criacao')
    total_products = products.count()
    total_pendentes = products.filter(status='Pendente').count()
    total_concluidos = products.filter(status='Concluído').count()
    total_entregues = products.filter(status='Entregue').count()
    context = {
        'products': products,
        'total_products': total_products,
        'total_pendentes': total_pendentes,
        'total_concluidos': total_concluidos,
        'total_entregues': total_entregues,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_registro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        tipo_de_trabalho = request.POST.get('tipo_de_trabalho')
        quantidade = request.POST.get('quantidade')
        valor_trabalho = request.POST.get('valor_trabalho')
        #valor_pago = request.POST.get('valor_pago')
        assunto = request.POST.get('assunto')
        metodo_de_pagamento = request.POST.get('metodo_de_pagamento')
        data_de_criacao = request.POST.get('data_de_criacao')

        product = Product.objects.create(
            nome=nome,
            telefone=telefone,
            tipo_de_trabalho=tipo_de_trabalho,
            quantidade=quantidade,
            valor_trabalho=valor_trabalho,
            assunto=assunto,
          #  valor_pago=valor_pago,
            metodo_de_pagamento=metodo_de_pagamento,
            data_de_criacao=data_de_criacao,
            status='Concluído' 
        )

        return redirect('add_registro')

    return render(request, 'add_registro.html')


@login_required(login_url='login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def view_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'home.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponseRedirect('/o')


@login_required(login_url='login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def edit_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect(reverse('index'))

    if request.method == 'POST':
        try:
            product.nome = request.POST.get('nome')
            product.telefone = request.POST.get('telefone')
            product.Tipo_De_trabalho = request.POST.get('Tipo_De_trabalho')
            product.quantidade = request.POST.get('quantidade')
            product.valor_trabalho = request.POST.get('valor_trabalho')
            product.valor_pago = request.POST.get('valor_pago')
            product.assunto = request.POST.get('assunto')
            product.metodo_de_pagamento = request.POST.get('metodo_de_pagamento')
            product.data_de_criacao = request.POST.get('data_de_criacao')

            if request.POST.get('status') == 'Concluído' and product.status == 'Pendente':
                product.status = 'Concluído'

            product.save()
        except Exception as e:
            return redirect(reverse('index'))

        return redirect(reverse('index'))
    else:
        return render(request, 'home.html', {'product': product})




# delete_product
@login_required(login_url='login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('/o')

# lista dos produtos
@login_required(login_url='login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def get_products(request):
    products = Product.objects.all().values()  # Obtém todos os produtos como um dicionário de valores
    return JsonResponse(list(products), safe=False)


