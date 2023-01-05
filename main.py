import os

def Fibo(n):
# Sprawdzenie czy podano prawidłową liczbę
# Jeżeli n jest mniejsze od 0 wtedy zwracamy błąd, gdyż wymagana jest nieujemna liczba całkowita

	if n < 0:
		print("Wprowadzono nieprawidłową wartość (n<0)")

# Sprawdzamy czy n jest równe 0
# Jeżeli tak, to zwracamy 0

	elif n == 0:
		return 0

# Sprawdzamy czy n jest równe 1 lub 2
# Jeżeli tak, to zwracamy wartosć 1
	elif n == 1 or n == 2:
		return 1
# W pozostałych przypadkach obliczamy ciąg Fibonacciego
	else:
		return Fibo(n-1) + Fibo(n-2)

# Uruchomienie programu
#print(Fibo(2))

def showAuthor():
    print("Informacje o programie i autorze:")
    print("===========================")
    print("| Nazwa Programu:")
    print("| | FibCalc |")
    print("| Wersja Programu:")
    print("| | v0.1 |")
    print("---------- AUTOR ----------")
    print("| Imie i Nazwisko autora:")
    print("| | Patryk Grzywacz |")
    print("| Numer Grupy:")
    print("| | 2.2 |\n")
while True:
    print("Witaj w programie FibCalc, wybierz jedną z poniższych opcji: \n")
    print("1. Kalkulator ciągu Fibonacciego")
    print("2. Wyświetl informacje o programie i autorze")
    print("3. WYJSCIE")
    options = input(": ")
    match options:
        case "1":
            os.system('clear')
            n = int(input("Który element ciągu chcesz obliczyc? "))
            print("Wynik dla",n,"elementu ciągu jest równy:",Fibo(n),"\n")
        case "2":
            os.system('clear')
            showAuthor()
        case "3":
            break
        case _:
            print("WYBIERZ KTÓRĄŚ Z OPCJI!")