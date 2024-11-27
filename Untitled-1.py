# numero_1 = input("number 1:")
# numero_2 = input("number 2:")

# def divisione(numero_1, numero_2) -> float:
#     try:
#         divisione = float(numero_1)/ float(numero_2)
#         print(f"Divisione: \n {float(numero_1)}/ {float(numero_2)}) =" f"{divisione}")
#     except ZeroDivisionError:
#         print("Non è possibile dividere per zero")  
#     except ValueError:
#         print("Non int valori trovati, divisione non è possibile.")

lista_di_persone = []
counter_di_input = 0
while counter_di_input < 5:
    lista_di_persone.append(input("Insert a name:\n"))
    counter_di_input += 1

def nome_più_lungo(lista: list) -> str:
    counter = 0
    nome_lungo = lista[0]
    while counter < len(lista)-1:
        counter += 1
        if len(nome_lungo) < len(lista[counter]):
             nome_lungo = lista[counter]
    return nome_lungo  
  
def rimovere_persone(lista: list):
    nome_da_togliere = ""
    while True:
        nome_da_togliere = input("Insert name to remove\n")
        try:
            lista.remove(nome_da_togliere)
            break
        except ValueError:
            print("this person is not on the list")



print(sorted(lista_di_persone))
print(nome_più_lungo(lista_di_persone))
print(rimovere_persone(lista_di_persone))
print(lista_di_persone)

# palla_magica_risposte = ["yes", "no", "maybe"]
# input_utente = ""
# while True:
#     input_utente = input("Ask question or type exit")
#     if input_utente.lower() == "exit":
#         break
# print(palla_magica_risposte[random.randit(0, len(palla_magica_risposte)-1)])
