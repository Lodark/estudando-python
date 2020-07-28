"""
1)ex 1
pessoa=[{'nome':str(input('nome')),'idade':int(input('idade'))}]
print(pessoa)
alterarnome=str(input('nome:'))
for c in range(len(pessoa)):
  if alterarnome in pessoa[c]['nome']:
    pessoa[c]['nome']=str(input('nome:'))

print(pessoa)


2)ex 2
cadastro=[]
nome=str(input('nome:'))
idade=int(input('idade:'))
cadastrando=lambda n,i:cadastro.append([n,i])
cadastrando(nome,idade)
print(cadastro)

3)ex 3
cadastro=[]
nome=str(input('nome:'))
idade=int(input('idade:'))
cadastrando=lambda n,i:{'nome':n,'idade':i}
cadastro.append(cadastrando(nome,idade))
print(cadastro)
[{print(f'{x}={z}')for x,z in c.items()}for c in cadastro]


"""

