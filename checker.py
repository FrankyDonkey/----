## PUT YOUR CPF HERE ##
cpf = '24947139098' ## < Your CPF > #
## WITHOUT DOT OR DASH ##

if not(cpf.isdecimal() and len(cpf) == 11):
    raise ValueError('\n\nCPF informado tem formato invalido.\nDigite somente os 11 numeros do CPF que desejas validar.')

def cpf_valido(cpf):
    mult1 = (10,9,8,7,6,5,4,3,2)

    dv1 = 0

    for n in range(9):
        dv1 += mult1[n]*int(cpf[n])

    if dv1 % 11 < 2:
        dv1 = '0'
    else:
        dv1 = str(11 - (dv1 % 11))

    cpf1 = cpf[:-2] + dv1

    mult2 = (11,10,9,8,7,6,5,4,3,2)

    dv2 = 0

    for n in range(10):
        dv2 += mult2[n]*int(cpf1[n])

    if dv2 % 11 < 2:
        dv2 = '0'
    else:
        dv2 = str(11 - (dv2 % 11))

    if cpf == cpf1 + dv2:
        return True
    else:
        return False



if cpf_valido(cpf):
    print('CPF',cpf, 'GOOD')
else:
    print('CPF',cpf, 'BAD')
