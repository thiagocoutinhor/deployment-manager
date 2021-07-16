# Function

## Propriedades

> Um dentre `branch`, `tag` e `revision` deve ser informado na propriedade `source`

- `name` Nome da Cloud Function

- `serviceAccountEmail` E-mail da conta de serviço (recomendo ser recuperado por referencia)

- `source` Dados do código fonte

    - `repository` Nome do repositório

    - `branch` Nome do branch a ser usado como base

    - `tag` Nome da tag a ser usada como base

    - `revision` Número do commit a ser como base

    - `path` (opcional) Caminho para o código fonte, caso não se encontre na raiz do repositório

- `entryPoint` Nome da função a ser executada no código

- `trigger` Trigger de evento da função

    - `url` Para triggers por URL, use esse atributo com true

- `variables` (opcional) Variável de ambiente usada na função

- `memory` (opcional) Quantidade de memória disponível para a função (padrão 128)

- `runtime` (opcional) Qual a linguagem que a função usa (padrão python37)

- `timeout` (opcional) O tempo de timeout da função em segundos (padrão 60)

- `region` (opcional) A região onde a função será criada (padrão us-central1)

- `labels` (opcional) Labels da função

> Para facilitar o preenchimento da propriedade `trigger` crie uma Cloud Function com o tipo de ativação que deseja e verifique o link “equivalente REST” dentro da aba “details”. Busque pela trigger no json e use essas propriedades.

## Pub/Sub Trigger

O trigger associado a um Pub/Sub permite que a Cloud Function seja disparada automaticamente quando uma mensagem é enviada.

```YAML
trigger:
  eventType: providers/cloud.pubsub/eventTypes/topic.publish
  resource: [[TOPIC]]
```

## Storage Trigger

O trigger associado ao storage permite que a função seja disparada automaticamente quando um arquivo é incluído, alterado ou deletado em determinado bucket.

O `eventType` pode ter as seguintes opções:

- `google.storage.object.finalize` para inclusões e alterações de arquivos

- `google.storage.object.deletepara` remoções de arquivos

- `google.storage.object.archive` para arquivamento de arquivos

- `google.storage.object.metadataUpdate` para atualização dos metadados

```YAML
trigger:
  eventType: google.storage.object.finalize
  resource: projects/_/buckets/[[BUCKET]]
  service: storage.googleapis.com
```

## Outputs

- `name` Nome recebido nas propriedades

- `url` URL de ativação da função para funções HTTP