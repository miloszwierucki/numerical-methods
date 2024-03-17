import numpy as np

def wielomian(x, arr):
    wynik = 0  # Inicjujemy zmienną wynik wartością 0
    for i in range(len(arr)):
        wynik += arr[i] * x ** (len(arr) - i - 1)  # Liczymy wartość wielomianu, uwzględniając kolejność współczynników
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
def wykladnicza(x, a, b):
    return a**x + b

def pochodna_wykladniczej(x, a):
    return a**x * np.log(a)


# Funkcja trygonometryczna
def trygonometryczna(x, funkcja, a, b):
    return a * funkcja(x) + b

# def zlozona(x, a):
#     return 0


def wartosc_funkcji(rodzaj_funkcji, x, a=None, b=None, wspolczynniki=None, wybrana_trygonometryczna=None):
    if rodzaj_funkcji == 0:  # Wielomianowa
        if wspolczynniki is None:
            raise ValueError("Brak współczynników dla funkcji wielomianowej.")
        return wielomian(x, wspolczynniki)
    elif rodzaj_funkcji == 1:  # Wykładnicza
        if a is None or b is None:
            raise ValueError("Brak współczynników dla funkcji wykładniczej.")
        return wykladnicza(x, a, b)
    elif rodzaj_funkcji == 2:  # Trygonometryczna
        if a is None or b is None:
            raise ValueError("Brak współczynników dla funkcji trygonometrycznej.")
        elif wybrana_trygonometryczna is None:
            raise ValueError("Brak wybrania funkcji trygonometrycznej.")
        return trygonometryczna(x, wybrana_trygonometryczna, a, b)
    else:
        raise ValueError("Nieprawidłowy rodzaj funkcji.")




def bisekcja_iteracyjnie(rodzaj_funkcji, a, b, iteracje, parametr1=None, parametr2=None, wspolczynniki=None, wybrana_trygonometryczna = None):
    srodek = (a + b) / 2
    print("wartosc testowa funkcji poza petla, x u gory kodu: ",
          wartosc_funkcji(rodzaj_funkcji, srodek, parametr1, parametr2, wspolczynniki, wybrana_trygonometryczna))

    for i in range(iteracje):

        srodek = (a + b) / 2
        wartosc_srodka = wartosc_funkcji(rodzaj_funkcji, srodek, parametr1, parametr2, wspolczynniki,
                                         wybrana_trygonometryczna)
        wartosc_a = wartosc_funkcji(rodzaj_funkcji, a, parametr1, parametr2, wspolczynniki, wybrana_trygonometryczna)

        if wartosc_srodka == 0:
            print(f'Miejscem zerowym tej funkcji jest {srodek}, znaleziony po {i} iteracjach')
            return srodek

        if np.real(wartosc_a * wartosc_srodka) < 0:
            b = srodek
        else:
            a = srodek

    print(f'po {iteracje} iteracjach miejsce zerowe przyblizone zostało do {srodek}')
    return srodek


# Metoda bisekcji

def bisekcja_epsilon(rodzaj_funkcji, a, b, epsilon, parametr1=None, parametr2=None, wspolczynniki=None, wybrana_trygonometryczna=None):
    if epsilon <= 0:
        raise ValueError("Epsilon powinien być większy od zera.")

    srodek = (a + b) / 2
    print("Wartość testowa funkcji poza pętlą, x u góry kodu: ",
          wartosc_funkcji(rodzaj_funkcji, srodek, parametr1, parametr2, wspolczynniki, wybrana_trygonometryczna))

    iteracje = 0

    while abs(b - a) > epsilon:
        srodek = (a + b) / 2
        wartosc_srodka = wartosc_funkcji(rodzaj_funkcji, srodek, parametr1, parametr2, wspolczynniki,
                                          wybrana_trygonometryczna)
        wartosc_a = wartosc_funkcji(rodzaj_funkcji, a, parametr1, parametr2, wspolczynniki, wybrana_trygonometryczna)

        if wartosc_srodka == 0:
            print(f'Miejscem zerowym tej funkcji jest {srodek}, znalezione po {iteracje} iteracjach')
            return srodek

        if np.real(wartosc_a * wartosc_srodka) < 0:
            b = srodek
        else:
            a = srodek

        iteracje += 1

    print(f'Po {iteracje} iteracjach miejsce zerowe zostało przybliżone do {srodek}')
    return srodek


#
# def metoda_Newtona_epsilon(id_funkcji: int, epsilon: float, x0: float, przedzial = None, iteracje = None):
#     counter = 0
#
#     while np.abs(funkcje[id_funkcji](x0)) > epsilon:
#         x0 -= funkcje[id_funkcji](x0)/pochodne[id_funkcji](x0)
#         counter += 1
#
#     print(f'miejsce zerowe przyblizone do {x0}, po {counter} iteracjach')
#     return x0
#
#
#
# def metoda_Newtona_iteracje(id_funkcji: int, iteracje: int, x0: float, przedzial = None, epsilon = None):
#     for i in range(iteracje):
#         if funkcje[id_funkcji](x0) == 0:
#             print(f'Znaleziono miejsce zerowe w {x0} po {i} iteracjach')
#             return x0
#         x0 -= funkcje[id_funkcji](x0)/pochodne[id_funkcji](x0)
#
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