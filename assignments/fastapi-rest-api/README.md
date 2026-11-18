# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Pratique a criação de rotas HTTP, validação de dados com modelos Pydantic e documentação automática de APIs.

## 📝 Tarefas

### 🛠️ Criar endpoints CRUD para tarefas

#### Descrição

Implemente uma API para criar e gerenciar tarefas. Cada tarefa deve ter um identificador, um título, uma descrição opcional e um indicador de conclusão. Use uma lista em memória como armazenamento; não é necessário configurar um banco de dados.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI executável com Uvicorn.
- Definir um modelo Pydantic para validar os dados de uma tarefa.
- Implementar `GET /tasks` para listar as tarefas e `GET /tasks/{task_id}` para buscar uma tarefa pelo identificador.
- Implementar `POST /tasks` para criar uma tarefa, `PUT /tasks/{task_id}` para atualizar uma tarefa e `DELETE /tasks/{task_id}` para removê-la.
- Retornar um status HTTP `404` quando o identificador solicitado não existir.

### 🛠️ Validar a API e conferir sua documentação

#### Descrição

Verifique os comportamentos da API e use a documentação interativa gerada pelo FastAPI para explorar os endpoints.

#### Requisitos
O programa concluído deve:

- Rejeitar dados inválidos, como uma tarefa sem título, usando a validação do modelo Pydantic.
- Retornar códigos HTTP adequados para operações bem-sucedidas, criação de recursos e erros de validação ou busca.
- Disponibilizar a documentação interativa em `/docs`.
- Incluir testes para listar, criar, consultar, atualizar e remover tarefas, além de uma busca por identificador inexistente.
