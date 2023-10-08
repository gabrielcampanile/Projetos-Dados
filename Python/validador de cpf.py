def quantidade():
    if len(cpf) < 11 or len(cpf) > 11:
        # print(f'O CPF é inválido, pois possui {len(cpf)} caracteres.')
        return False
    else:
        return True


def numerar():
    for a in cpf:
        a = int(a)
        cpf_numerado.append(a)


def primeiro_digito():
    if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
        return False
    else:
        controlador = 10
        acumulador = 0
        resultado = 0
        for numeros in cpf_numerado[0:9]:
            resultado = numeros * controlador
            acumulador += resultado
            controlador -= 1
        acumulador = acumulador * 10 % 11
        if acumulador == 10:
            acumulador = 0
        if acumulador == cpf_numerado[9]:
            return True
        else:
            return False


def segunda_digito():
    if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
        return False
    else:
        controlador2 = 11
        acumalador2 = 0
        resultado2 = 0
        for numeros2 in cpf_numerado[0:10]:
            resultado2 = numeros2 * controlador2
            acumalador2 += resultado2
            controlador2 -= 1
        acumalador2 = acumalador2 * 10 % 11
        if acumalador2 == 10:
            acumalador2 = 0
        if acumalador2 == cpf_numerado[10]:
            return True
        else:
            return False


# recebe o CPF
cpf = str(input('CPF: ')).replace('.', '').replace('-', '')
# numera o cpf
cpf_numerado = []

numerar()
# print(cpf_numerado)

quantidade()
# print(quantidade())

primeiro_digito()
# print(primeiro_digito())

segunda_digito()
# print(segunda_digito())

if quantidade() == 1 and primeiro_digito() == 1 and segunda_digito() == 1:
    print('O CPF é válido')
else:
    print('O CPF é inválido')
