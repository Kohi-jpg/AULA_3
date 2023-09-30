pais = input('Digite o seu país ou o DDD do seu país:\n')
ddd = input('Digite o seu ddd:\n')
numero = input('Digite o seu número:\n')

if pais == 'Brasil':
    print(f'+55 ({ddd}) {numero}')
else:
    print(f'+{pais} ({ddd}) {numero}')

