def voto(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

ano_nascimento = int(input('Digite seu ano de nascimento: '))
voto(ano_nascimento)