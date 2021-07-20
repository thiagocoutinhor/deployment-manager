# Bucket

## Propriedades

- `name` Nome do bucket a ser criado
- `region` (opcional) Região do bucket (padrão us-central1)
- `labels` (opcional) Labels do bucket
- `policies` (opcional) Lista de acessos específicos ao bucket
    - `role`: Papel a ser adicionado
    - `member`: Membro a receber o acesso

> O memrbo a receber o acesso em `policies` deve ter o prefixo `serviceAccount:` ou `user:` antes de seu e-mail dependendo do tipo.

## Outputs

- `name` Nome recebido nas propriedades