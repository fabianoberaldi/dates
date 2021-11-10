from datetime import datetime
from typing import List
from dateutil.relativedelta import relativedelta
#from pandas.tseries.offsets import BMonthEnd
from datetime import date
import calendar
import holidays

def get_ultimo_dia_do_mes(ano : int, mes : int) -> int:
    """Obter o último dia do mês

    Args:
        ano (int): informar o ano
        mes (int): informar o mês

    Raises:
        Exception: O ANO e MÊS deveM ser um número inteiro
        Exception: O MÊS deve ser um número entre 1 e 12
        Exception: Falha ao obter último dia do mês

    Returns:
        int: último dia do mês
    """


    if ((isinstance(ano,int) == False) or (isinstance(mes,int) == False)):
            raise Exception("O ANO e MÊS devem ser um nº inteiro")

    if (mes < 1 or mes > 12):
        raise Exception("O MÊS deve estar entre 1 e 12")

    try:        
        ultimo_dia = (datetime(ano, mes, 1)+relativedelta(day=31)).day

        return ultimo_dia

    except Exception as ex:
        erro = f"Falha ao obter último dia do mês. Erro: {str(ex)}"
        raise Exception(erro)

def get_ultimo_dia_util_do_mes(ano : int, mes : int) -> int:
    """Obter o último dia útil do mês

    Args:
        ano (int): informar o ano
        mes (int): informar o mês

    Raises:
        Exception: O ANO e MÊS deveM ser um número inteiro
        Exception: O MÊS deve ser um número entre 1 e 12
        Exception: Falha ao obter último dia útil do mês

    Returns:
        int: último dia útil do mês
    """
      
    if ((isinstance(ano,int) == False) or (isinstance(mes,int) == False)):
            raise Exception("O ANO e MÊS devem ser um nº inteiro")  

    if (mes < 1 or mes > 12):
        raise Exception("O MÊS deve estar entre 1 e 12")

    try:        
        ultimo_dia_util = max(calendar.monthcalendar(ano, mes)[-1:][0][:5])

        return ultimo_dia_util

    except Exception as ex:
        erro = f"Falha ao obter último dia do mês. Erro: {str(ex)}"
        raise Exception(erro)

def get_feriados_brasil(ano: int) -> list:
    """Obter uma lista de feriados (data) do Brasil

    Args:
        ano (int): informar o ano

    Raises:
        Exception: O ANO deve ser um nº inteiro
        Exception: Falha ao obter lista de feriados

    Returns:
        list: lista de feriados (datas) do Brasil
    """

    if ((isinstance(ano,int) == False)):
        raise Exception("O ANO deve ser um nº inteiro")   

    try:    
        lst_feriados =[]   
        feriados= holidays.Brazil()

        for feriado in feriados[f'{str(ano)}-01-01': f'{str(ano)}-12-31'] :
            lst_feriados.append(feriado)

        return lst_feriados

    except Exception as ex:
        erro = f"Falha ao obter lista de feriados. Erro: {str(ex)}"
        raise Exception(erro)

def get_dias_feriado_mes(ano: int, mes: int) -> list:
    """Obter dias que são feriados no mês

    Args:
        ano (int): informar o ano
        mes (int): informar o mês

    Raises:
        Exception: O ANO e MÊS deveM ser um número inteiro
        Exception: O MÊS deve ser um número entre 1 e 12
        Exception: Falha ao obter lista de feriados

    Returns:
        list: lista de dias 
    """

    if ((isinstance(ano,int) == False) or (isinstance(mes,int) == False)):
        raise Exception("O ANO e MÊS devem ser um nº inteiro")
    
    if (mes < 1 or mes > 12):
        raise Exception("O MÊS deve estar entre 1 e 12")
    
    try:    
            lst_dias =[]   
            feriados= holidays.Brazil()

            for feriado in feriados[f"{str(ano)}"+"-"+f"{str(mes)}-01" : f"{str(ano)}"+"-"+f"{str(mes)}"+"-"+str(get_ultimo_dia_do_mes(ano,mes))] :
                lst_dias.append(feriado.day)

            if len(lst_dias) == 0:
                return 0

            return lst_dias

    except Exception as ex:
        erro = f"Falha ao obter lista de feriados. Erro: {str(ex)}"
        raise Exception(erro)

def get_nome_dia_semana(ano: int, mes: int, dia: int) -> str:
    """Obter nome do dia da semana a partir de uma data informada

    Args:
        ano (int): informar ano
        mes (int): informar mês
        dia (int): informar dia

    Raises:
        Exception: O ANO, MÊS e DIA devem ser um nº inteiro
        Exception: O DIA deve estar entre 1 e 31
        Exception: O MÊS deve estar entre 1 e 12
        Exception: Falha ao obter nome do dia da semana

    Returns:
        str: nome do dia da semana
    """

    if ((isinstance(ano,int) == False) or (isinstance(mes,int) == False) or \
        (isinstance(dia,int) == False)):
        raise Exception("O ANO, MÊS e DIA devem ser um nº inteiro")

    if (dia < 1 or dia > 31):
        raise Exception("O DIA deve estar entre 1 e 31")

    if (mes < 1 or mes > 12):
        raise Exception("O MÊS deve estar entre 1 e 12")

    try:    
        data = datetime(ano, mes, dia)  

        semanaDias = {0:"Seg",1:"Ter",2:"Qua",3:"Qui",4:"Sex",5:"Sab",6:"Dom"}

        return semanaDias[data.weekday()]
        
    except Exception as ex:
        erro = f"Falha ao obter nome do dia da semana. Erro: {str(ex)}"
        raise Exception(erro)

def data_is_feriado(ano: int, mes: int, dia: int) -> bool:
    """Verificar se a data é um feriado

    Args:
        ano (int): informar ano
        mes (int): informar mês
        dia (int): informar dia

    Raises:
        Exception: O ANO, MÊS e DIA devem ser um nº inteiro
        Exception: O DIA deve estar entre 1 e 31
        Exception: O MÊS deve estar entre 1 e 12
        Exception: Falha ao verificar se dia é um feriado

    Returns:
        bool: retora True se feriado ou caso contrário, retorna False
    """

    if ((isinstance(ano,int) == False) or (isinstance(mes,int) == False) or \
        (isinstance(dia,int) == False)):
        raise Exception("O ANO, MÊS e DIA devem ser um nº inteiro")

    if (dia < 1 or dia > 31):
        raise Exception("O DIA deve estar entre 1 e 31")

    if (mes < 1 or mes > 12):
        raise Exception("O MÊS deve estar entre 1 e 12")

    try:    
        resultado = False

        lst_dias = get_dias_feriado_mes(ano, mes) 

        if lst_dias == 0:
             resultado = False
        else:
            if dia in lst_dias:
                resultado = True
            else:
                resultado = False
            
        return resultado

    except Exception as ex:
        erro = f"Falha ao verificar se dia é um feriado. Erro: {str(ex)}"
        raise Exception(erro)

"""print("FERIADOS DO BRASIL-------------------------------------")
print(get_feriados_brasil(2021))
print("FERIADO: Dias do mês ***************************")
print(get_dias_feriado_mes(2021,4))
print("FERIADO: Dia é um feriado?")
print(data_is_feriado(2021,4,1))
print("Obter o nome do dia da semana ***********************")
print(get_nome_dia_semana(1974,5,7))"""
