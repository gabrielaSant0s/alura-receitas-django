import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def cadastro(request):
    # infos vindo do template cadastro
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        senha = request.POST["password"]
        senha2 = request.POST["password2"]

        if not nome.strip():
            print("O campo nome não pode ficar em branco")
            return redirect("cadastro")
        if not email.strip():
            print("O campo email não pode ficar em branco")
            return redirect("cadastro")
        if senha2 != senha:
            print("Senhas diferentes")
            return redirect("cadastro")
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect("cadastro")
        user = User.objects.create_user(
            username=nome, email=email, password=senha)

        user.save()
        print('usuario cadastrado com sucesso')

        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def logout(request):
    pass


def dashboard(request):
    pass
