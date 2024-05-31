# Sistema de Gerenciamento de Organizações e Equipes de Motoristas

Este é um sistema de gerenciamento de organizações, equipes de motoristas e grupos, com funcionalidades para criar, visualizar e excluir essas entidades através de uma API RESTful.

## Requisitos

- Python 3.x
- Bibliotecas: `requests`, `time`

## Configuração

Antes de executar o programa, certifique-se de configurar as seguintes variáveis de ambiente no arquivo `utils.py`:

- `API_BASE_URL`: A URL base da API que será usada para interagir com o sistema.
- `AUTH`: As credenciais de autenticação para acessar a API.
- `PARENT_ORGANIZATION_ID`: O ID da organização pai.

## Funcionalidades

- **Criar Organização:** Cria uma nova organização no sistema.
- **Criar Equipe de Motoristas:** Cria uma nova equipe de motoristas associada a uma organização.
- **Criar Motorista:** Cria um novo motorista e o associa a uma equipe de motoristas.
- **Criar Grupo:** Cria um novo grupo associado a uma organização.
- **Excluir Organização:** Remove uma organização existente do sistema.
- **Excluir Equipe de Motoristas:** Remove uma equipe de motoristas existente do sistema.
- **Excluir Motorista:** Remove um motorista existente do sistema.
- **Excluir Grupo:** Remove um grupo existente do sistema.
