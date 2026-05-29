class Tarefa:
    tarefas = []
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False
        Tarefa.tarefas.append(self)

    def __str__(self):
        return f'{self.titulo} | {self.descricao}'
    
    @classmethod
    def listarTarefas(cls):
        for tarefa in cls.tarefas:
            print(tarefa)

tarefa1 = Tarefa('Criar metodo', 'como criar metodo')
tarefa2 = Tarefa('Criar classe', 'como criar classe')

Tarefa.listarTarefas()

qtd_tarefas = len(Tarefa.tarefas)

print(f'A quantidade de tarefas é {qtd_tarefas}')