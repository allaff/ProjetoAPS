from django.core.exceptions import ValidationError

def valida_cpf(value):
    if(len(str(value)) != 11):
        raise ValidationError ('ERRO! CPF INCOMPLETO!')
    else:
        return value
    
def valida_senha(value):
    if(len(str(value)) !=8):
        raise ValidationError ('ERRO! SENHA INCOMPLETA!')
    else:
        return value
    

def valida_telefone(value):
    if(len(str(value)) != 11):
        raise ValidationError ('ERRO! TELEFONE INCOMPLETO!')
    else:
        return value