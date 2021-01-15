def create_file(name, content):
    with open(name, 'w') as file:
        file.write(content)
    return file

def read_file(name):
    with open(name) as file:
        return file.read()

if __name__ == "__main__":
    print('===TRABALHAR COM ARQUIVOS===')

    while True:
        try:
            resposta = input('Deseja: (criar/ler/sair)')
            if resposta == 'c':
                nome = input('Nome do arquivo: ')
                conteudo = input('Conteúdo: ')
                create_file(nome, conteudo)
                break
            elif resposta == 'l':
                nome = input('Nome do arquivo: ')
                print(read_file(nome))
                break
            elif resposta == 's':
                print('Programa encerrado!')
                break
        except:
            print('Inválido')