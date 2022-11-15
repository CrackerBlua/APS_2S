from CryptoBO import AESCipher
import Menu as menuTemplate
import time

# Gero minha classe BO de criptografia
CYPHER = AESCipher()
# Defino minha opção como None
OPTION = None

# Inicializo meu menu
MENU = menuTemplate.Menu()
# Crio meu meno
MENU.createMenu()

# Enquanto o usuário não entrar com zero, tudo se repetirá
while (OPTION != 0):
    # Usuário entra com a opção
    OPTION = int(input('Entre com uma opção do Menu: '))
    
    # Caso não esteja em uma das opções validas definida na minha classe de Menu, voltará para a tela inicial do menu
    if(OPTION not in MENU.options):
        MENU.createMenu()
        continue
    
    # Opção de gerar a random key 
    if(OPTION == 1):
        CYPHER.set_random_key()
        MENU.messageGeneratedKey(CYPHER.key)
        time.sleep(3.5) # Faço o sistema congelar por 3.5s e depois gera o menu novamente
        MENU.createMenu()

    # Opção de inserir uma chave customizada 
    if(OPTION == 2):
        customKey = str(input('Entre com a sua chave customizada: '))
        setBreak = False
        
        if(customKey == "0"): 
            MENU.createMenu()
            continue
        
        # Valido se contem 16 caracteres para uma chave de 16bytes
        while(len(customKey) != 16):
            print('O valor entrado tem de haver 16 caracteres para maior segurança!')
            time.sleep(3.5)
            MENU.createMenu()
            customKey = str(input('Entre com a sua chave customizada: '))
            if(customKey == "0"): break

        if(setBreak): 
            MENU.createMenu()
            continue
        
        # CYPHER.setCustomPassword(customKey)
        MENU.messageGeneratedKey(customKey)
        time.sleep(3.5)
        MENU.createMenu()

    # Opção para mostrar a chave secreta
    if(OPTION == 3):
        MENU.showSecretKey(CYPHER.key)
        time.sleep(3.5)
        MENU.createMenu()
    
    # Opção de inserir um texto a ser criptografado 
    if(OPTION == 4):
        MENU.createMenu()
        msgStr  = str(input('Entre com a mensagem a ser criptografada: '))
        ans = input('Confirmar? \n 1 - Sim \n 2 - Não \n R: ')
        
        if(ans == '1'):
            saveMsg = True
        elif(ans == '2'): 
            saveMsg = False
        else:
            print('Valor entrado não corresponde as alternativas!')
            time.sleep(3.5)
            saveMsg = False
        
        # Enquanto não obedecer os critérios e/ou colocar pra sair, será pedido uma mensagem
        while(not saveMsg): 
            MENU.createMenu()
            
            if(ans == '2'):
                msgStr  = str(input('Entre com a mensagem a ser criptografada: '))            

            ans = input('Confirmar? \n 1 - Sim \n 2 - Não \n R: ')
            
            if(ans == '1'):
                saveMsg = True
            elif(ans == '2'): 
                saveMsg = False
            else:
                print('Valor entrado não corresponde as alternativas!')
                time.sleep(3.5)
                saveMsg = False
                continue

        print('Mensagem encriptografada com sucesso!')
        CYPHER.encrypt(msgStr)
        time.sleep(3.5)
        MENU.createMenu()
    
    # Processo de desciptografar a mensagem 
    if(OPTION == 5):
        CYPHER.decrypt()
        print('Mensagem descriptografada com sucesso!')
        time.sleep(3.5)
        MENU.createMenu()

    # Mostrar a mensage
    if(OPTION == 6):
        MENU.showMessage(CYPHER.message)
        time.sleep(3.5)
        MENU.createMenu()