from flask import Flask
from models.task import Task
app = Flask(__name__)

# CRUD
#Create, Read, Update and Delete = Criar, ler, Atualizar e Deletar
#Tabela: Tarefa

tasks = []



if __name__ == "__main__":
    app.run(debug=True)