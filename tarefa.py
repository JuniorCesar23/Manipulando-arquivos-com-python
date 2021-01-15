from datetime import datetime, timedelta
 
class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendente(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito == True]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas 
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} - ({len(self.pendente())} tarefa(s) pendentes)'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluido(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(vence em {dias} dias)')
        return f'{self.descricao}' + ''.join(status)

def main():

    casa = Projeto('Tarefas de casa')
    casa.add('Lavar roupa', datetime.now())
    casa.add('Lavar louça', datetime.now() + timedelta(days=3, minutes=12))
    print(casa)
    for tarefa in casa:
        if tarefa.descricao == 'Lavar louça':
            tarefa.concluido()
        print(tarefa)
    print(casa)

    escola = Projeto('Deveres da escola')
    escola.add('Provas')
    escola.add('Seminários')
    print(escola)
    for tarefa in escola:
        if tarefa.descricao == 'Seminários':
            tarefa.concluido()
        print(tarefa)
    print(escola)
   
if __name__ == "__main__":
    main()
