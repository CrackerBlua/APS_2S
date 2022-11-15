# Bibliotecas importantes para o requisito de menu
import os
from re import template

# Função para limpar o terminal
def clearTerminal():
    os.system('cls||clear')

# Classe que será o objeto completo de um menu, que terá suas funções utilitárias
class Menu:
    # Construtor que limpará o console
    def __init__(self):
        clearTerminal()
        os.system('echo off')
    
    # Função que gera o menu toda vez que for chamado   
    def createMenu(self):
        # opções que são aceitas nas entradas do usuário
        Menu.options = {1, 2, 3, 4, 5, 6, 0}
        clearTerminal()
        print('=================================================================================================================')
        print('| 1 - Gerar chave de cripto/decripto                                                                            |')
        print('| 2 - Colocar manualmente chave de cripto/decripto                                                              |')        
        print('| 3 - Conferir chave                                                                                            |')
        print('| 4 - Entrar com mensagem para criptografar                                                                     |')
        print('| 5 - Descriptografar mensagem                                                                                  |')
        print('| 6 - Mostrar mensagem                                                                                          |')
        print('| 0 - Sair do menu                                                                                              |')
        print('=================================================================================================================')
    
    # Função para mostrar a chave gerada/inserida pelo usuário
    def showSecretKey(self, key):
        self.createMenu()
        
        if(len(key) != 0):
            print(f' Essa é a sua Chave: < {key} >                              ')
        else:
            print('| Você não tem uma chave registrada ainda!                                                                      |')
        print('=================================================================================================================')
    
    # Quando gerada a chave, será mostrada ao usuário por essa função
    def messageGeneratedKey(self, key):
        self.createMenu()
        print(f' Chave < {key} > gerada com sucesso                             ')
        print('=================================================================================================================')
        
    def showMessage(self, msg):
        self.createMenu()
        print(f' Mensagem: {msg} ')
        print('=================================================================================================================')
