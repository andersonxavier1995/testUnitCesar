# Testes Unitários - Cesar School

Este é um projeto de gerenciamento de usuários em Python. Ele permite adicionar, remover, atualizar e exibir informações de usuários. O sistema também possui validações para garantir que as entradas estejam no formato correto.


## Funcionalidades

- **Adicionar Usuário**: Adiciona um novo usuário com um nome e um cargo (job).
- **Remover Usuário**: Remove um usuário existente pelo nome.
- **Atualizar Usuário**: Atualiza o cargo (job) de um usuário existente.
- **Exibir Usuário por Nome**: Exibe as informações de um usuário específico pelo nome.
- **Exibir Todos os Usuários**: Exibe todos os usuários cadastrados no sistema.

## Validações

O sistema possui validações para garantir que as entradas sejam válidas:

- **Nome e Cargo (job)** devem ser strings alfabéticas (sem números ou caracteres especiais) e não podem estar vazios.
- Se os parâmetros fornecidos não atenderem a esses critérios, o sistema exibe uma mensagem de erro e retorna ao menu principal.


