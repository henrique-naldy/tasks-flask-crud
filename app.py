from flask import Flask, request
from models.task import Task
app = Flask(__name__)

# CRUD
#Create, Read, Update and Delete = Criar, ler, Atualizar e Deletar
#Tabela: Tarefa

tasks = []

@app.route('/tasks', methods=['POST',])
def Create_task():
    data = request.get_json()
    print(date)
    return 'Test'
if __name__ == "__main__":
    app.run(debug=True)