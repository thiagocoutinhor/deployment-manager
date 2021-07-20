# Scheduler

## Propriedades

> Pelo menos um dentre `pubsub` ou `http` devem estar preenchidos

- `name` Nome do schedule
- `description` (opcional) Descrição do schedule
- `cron` Agendamento no formato cron
- `pubsub` Caso o alvo do schedule seja um pubsub
- `topic` Tópico alvo no pubsub
- `attributes` (opcional) Dicionário dos valores dos atributos
- `http` Caso o alvo seja uma API (cloud functions são ativadas usando essa opção)
- `method` Método HTTP a ser usado (POST, PUT, DELETE, etc.)
- `url` Url a ser chamado
- `serviceAccountEmail` (opcional) Email da conta de serviço a ser usado como autenticação
- `payload` (opcional) Payload a ser enviado ao alvo. Deve estar encodado em base64
- `region` (opcional) A região onde o schedule vai ser executado (padrão us-central1)
- `labels` (opcional) Labels do schedule

> Para ativar uma cloudfunction através de um shcedule, use a opção `http`

## Payload e Base64

Payloads para http só são permitidos se o `method` for POST, PUT ou PATCH. Qualquer outro method com um payload causará um erro.

Para enviar um payload é necessário que ele seja [codificado em base64](https://www.base64encode.org/).

## Código Python

Para contornar a necessidade de encoding do payload (tanto em HTTP quando para Pub/Subs), o template em python faz esse trabalho e permite que o YAML enviado ao deployment manager tenha o texto do payload cru.

## Outputs

- `name` Nome recebido nas propriedades