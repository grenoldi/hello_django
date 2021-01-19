from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}!</h1>'.format(nome))


def soma(request, num1, num2):
    somando = num1 + num2
    return HttpResponse('<h2>Somando {} e {} teremos {}</h2>'.format(num1, num2, somando))


def subtracao(request, num1, num2):
    subtraindo = num1 - num2
    return HttpResponse('<h2>Subtraindo {} e {} teremos {}</h2>'.format(num1, num2, subtraindo))


def multiplicacao(request, num1, num2):
    multiplicando = num1 * num2
    return HttpResponse('<h2>Multiplicando {} e {} teremos {}</h2>'.format(num1, num2, multiplicando))


def divisao(request, num1, num2):
    if num2 != 0:
        somando = num1 / num2
        return HttpResponse('<h2>Dividindo {} e {} teremos {}</h2>'.format(num1, num2, somando))
    else:
        return HttpResponse('<h2>Mandamento 11: Nunca dividiras por zero</h2>')