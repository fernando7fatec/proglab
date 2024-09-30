import functools

# Funcao Lambda que busca nome em uma lista
busca_nomes = lambda nomes,nome : True if nome in nomes else False
n = ['Joao','Maria','Jose']
print('Nome ok' if busca_nomes(n,'Joao') else ' nao encontrado ')

# Factorial Python One-Liner
# functools.reduce(lambda x, y: x * y, range(1, n+1))

# busca o valor maximo em uma lista 
lista = [20,1024,100,10]

# funcao lambda reduzida 
max = functools.reduce(lambda a, b : a if a > b else b, lista)
print(max)