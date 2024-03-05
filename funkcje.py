# Funkcja wielomianowa
import numpy as np


def wielomian(x, arr):
    for i in range(len(arr)):
        if i == 0:
            wynik = arr[i]
        else:
            wynik += arr[i] * x**i

    return wynik

def pochodna_wielomianu(x, arr):
    wynik = 0
    for i in range(len(arr)):
        if i == 0:
            continue
        else:
            wynik += arr[i] * i * x**(i-1)

    return wynik


# Funkcja wykładnicza
def wykladnicza(x, a, b=0):
    return a**x + b

def pochodna_wykladniczej(x, a, b=0):
    return a**x * np.log(a)


# Funkcja trygonometryczna
def trygonometryczna(x, funkcja, a, b=0):
    return a * funkcja(x) + b




# # Metoda bisekcji
# def bisekcja_epsilon(id_funkcji, przedzial: tuple, epsilon: float, x0 = None, iteracje = None):
#     funkcja = funkcje[id_funkcji]
#     a, b = przedzial
#     counter = 0

#     while np.abs(a-b) > epsilon:
#         counter += 1
#         srodek = (a+b)/2

#         if funkcja(srodek) == 0:
#             print(f'Miejscem zerowym tej funkcji jest {srodek}, znaleziony po {counter} iteracjach')
#             return srodek

#         a, b = (a, srodek) if funkcja(a)*funkcja(srodek) < 0 else (srodek, b)

#     print(f'Przyblizone miejsce zerowe to {srodek}, znalezione po {counter} iteracjach')
#     return srodek


# def bisekcja_iteracyjnie(id_funkcji, przedzial: tuple, iteracje: int, epsilon = None, x0 = None):
#     funkcja = funkcje[id_funkcji]
#     a, b = przedzial

#     for i in range(iteracje):
#         srodek = (a+b)/2

#         if funkcja(srodek) == 0:
#             print(f'Miejscem zerowym tej funkcji jest {srodek}, znaleziony po {i} iteracjach')
#             return srodek

#         a, b = (a, srodek) if funkcja(a)*funkcja(srodek) < 0 else (srodek, b)

#     print(f'po {iteracje} iteracjach miejsce zerowe przyblizone zostało do {srodek}')
#     return srodek


# def metoda_Newtona_epsilon(id_funkcji: int, epsilon: float, x0: float, przedzial = None, iteracje = None):
#     counter = 0

#     while np.abs(funkcje[id_funkcji](x0)) > epsilon:
#         x0 -= funkcje[id_funkcji](x0)/pochodne[id_funkcji](x0)
#         counter += 1

#     print(f'miejsce zerowe przyblizone do {x0}, po {counter} iteracjach')
#     return x0



# def metoda_Newtona_iteracje(id_funkcji: int, iteracje: int, x0: float, przedzial = None, epsilon = None):
#     for i in range(iteracje):
#         if funkcje[id_funkcji](x0) == 0:
#             print(f'Znaleziono miejsce zerowe w {x0} po {i} iteracjach')
#             return x0
#         x0 -= funkcje[id_funkcji](x0)/pochodne[id_funkcji](x0)

#     print(f'po {iteracje} iteracjach miejsce zerowe przyblizono do {x0}')
#     return x0


# def bisection_method(f, a, b, epsilon):
#     if f(a) * f(b) >= 0:
#         print("Funkcja nie spełnia założenia o przeciwnych znakach na krańcach przedziału.")
#         return None
#     iteration = 0

#     if(epsilon != 0):
#         while (b - a) / 2 > epsilon:
#             midpoint = (a + b) / 2
#             if f(midpoint) == 0:
#                 return midpoint
#             elif f(midpoint) * f(a) < 0:
#                 b = midpoint
#             else:
#                 a = midpoint
#             iteration += 1
#             return (a + b) / 2

#     elif(max_iterations != 0):
#         while iteration < max_iterations:
#             midpoint = (a + b) / 2
#             if f(midpoint) == 0:
#                 return midpoint
#             elif f(midpoint) * f(a) < 0:
#                 b = midpoint
#             else:
#                 a = midpoint
#             iteration += 1
#             return (a + b) / 2


# # Metoda stycznych (Newtona)
# def newton_method(f, x0, epsilon=0, max_iterations=0):
#     iteration = 0

#     if(epsilon != 0):
#         while abs(f(x0)) > epsilon:
#             x0 = x0 - f(x0) / df(x0)
#             iteration += 1
#             return x0

#     elif(max_iterations != 0):
#         while iteration < max_iterations:
#             x0 = x0 - f(x0) / df(x0)
#             iteration += 1
#             return x0

# def plot_function(f, a, b, roots=None):
#     x = np.linspace(a, b, 400)
#     y = f(x)
#     plt.plot(x, y, label='f(x)')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.grid(True)
#     if roots:
#         plt.scatter(roots, [0] * len(roots), color='red', label='Roots')
#     plt.legend()
#     plt.show()