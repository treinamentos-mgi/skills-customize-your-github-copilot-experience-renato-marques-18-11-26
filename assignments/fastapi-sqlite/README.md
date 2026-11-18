# 📘 Atividade: FastAPI e SQLite

## 🎯 Objetivo

Construa uma API REST que persiste dados em um banco SQLite. Pratique consultas SQL, integração entre FastAPI e Pydantic e operações CRUD que continuam disponíveis após reiniciar o servidor.

## 📝 Tarefas

### 🛠️ Configurar o banco e a criação de registros

#### Descrição

Use SQLite para criar uma tabela de tarefas e adaptação de dados. Implemente a criação de registros por meio de um endpoint FastAPI.

#### Requisitos
O programa concluído deve:

- Criar o arquivo `tasks.db` e uma tabela `tasks` contendo `id`, `title`, `description` e `completed`.
- Definir modelos Pydantic para validar os dados recebidos e devolvidos pela API.
- Implementar `POST /tasks` para inserir uma tarefa e retornar o registro completo com seu identificador.
- Retornar dados persistidos no formato JSON.

### 🛠️ Consultar, atualizar e remover tarefas

#### Descrição

Complete a API executando operações SQL relacionadas aos registros armazenados e aplicando tratamento de resultados inexistentes.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` para listar todas as tarefas armazenadas.
- Implementar `GET /tasks/{task_id}` para buscar uma tarefa pelo identificador.
- Implementar `PUT /tasks/{task_id}` para atualizar os campos enviados e `DELETE /tasks/{task_id}` para remover um registro.
- Retornar HTTP `404` quando o identificador não existir.
- Confirmar que os dados continuam disponíveis após reiniciar a aplicação.

### 🛠️ Validar e testar a persistência

#### Descrição

Use testes automatizados para verificar o comportamento da API e garantir que todas as operações afetam o banco SQLite.

#### Requisitos
O programa concluído deve:

- Rejeitar uma tarefa sem título por meio da validação Pydantic.
- Testar criação, consulta, atualização e remoção de registros.
- Incluir pelo menos um teste que insira uma tarefa, reinicie ou recrie a conexão e confirme que ela continua armazenada.
- Registrar as instruções necessárias para instalar dependências e iniciar o servidor.
