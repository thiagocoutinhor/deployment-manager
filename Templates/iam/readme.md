> Para o uso correto desses templates é necessário a adição da role `Security Admin` na conta de serviço `[número do projeto]@cloudservices.gserviceaccount.com`

# Add Role

## Propriedades

- `role` Papel a ser atribuído a conta

- `account` Conta a qual o papel vai ser atribuído

> A propriedade `account` precisa de um prefixo referente ao tipo de conta. Para as contas de serviço, use `serviceAccount:[EMAIL]` e `user:[EMAIL]`, para os usuários.

# Service Account

## Propriedades

- `name` Nome da conta de serviço

- `displayName` (opcional) Nome de exibição da conta

- `roles` Lista de papeis da conta

- `labels` (opcional) Labels da conta de serviço

> Consulte a lista completa de papeis disponíveis no seu projeto. Ao clicar em qualquer um dos papeis para mais detalhes basta copiar o ID do papel informado na tela e acrescentá-lo na lista.

## Outputs

- `name` Nome recebido na propriedade

- `email` E-mail gerado da conta de serviço