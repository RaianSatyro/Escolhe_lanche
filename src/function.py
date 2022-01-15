from src.list import *
from random import randint


def decisao_comida(escolha):
    
    
    if escolha == 1:
        print(f'\nSua escolha de hoje vai ser: {comidas_saudavel[randint(0, 10)]}')

    elif escolha == 2:
        print(f'\nSua escolha de hoje vai ser: {comidas_nao_saudavel[randint(0, 8)]}')
    
    else:
        print('Opção invalida, digite um numero valido')
        decisao_comida()
        
        
def decisao_bebida(escolha):
    if escolha == 1:
        print(f'E sua bebida será: {bebidas_saudavel[randint(0, 2)]}\n')
        
    elif escolha == 2:
        print(f'E sua bebida será: {bebidas_nao_saudavel[randint(0, 3)]}\n')
        
    else:
        print('Opção invalida, digite um numero valido')
        decisao_bebida()
        