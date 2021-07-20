# Dataset

## Propriedades

- `name` Nome do dataset
- `description` Descrição do dataset
- `labels` (opcional) Labels do dataset

## Outputs

- `name` Nome do dataset como recebido nas propriedades

# Table

## Propriedades

- `name` Nome da tabela
- `dataset` Nome do dataset da tabela
- `description` Descrição da tabela
- `schema` (obrigatório para tabelas nativas, opcional para externas) Campos da tabela (lista com os itens contendo name e type)
- `partition` (opcional) Configurações de particionamento da tabela
    - `mode` (opcional, padrão TIME) Modo de particionamento da tabela, entre TIME e RANGE
    - `field` Campo por onde a tabela se particiona
    - `type` Tipo de particionamento por tempo (DAY, HOUR, MONTH, ou YEAR)
    - `expirationMs` (opcional) Tempo para manter a partição (em milisecundos) para particionamento por tempo
    - `range` Para partições do modo range
        - `start` Início do range
        - `end` Final do range
        - `interval` Tamanho do intervalo das partições das partições
- `external` (opcional) Mapeamento para as tabelas externas
    - `bucket` Nome do bucket onde estarão os dados (e diretório, caso aplicável)
    - `format` Formato do arquivo (ex: NEWLINE_DELIMITED_JSON)
    - `hivePartition` (opcional) Se a tabela externa estiver particionada como uma estrutura de partição por subdiretório
        - `mode` (opcional, padrão AUTO) O tipo de avaliação de tipo das partições (entre AUTO, STRING ou CUSTOM)
        - `source` A forma do caminho para a raiz da tabela, para AUTO ou STRING. Com as formatação dos tipos de particao para o CUSTOM
- `labels` (opcional) Labels da tabela

## Schema

O campo `schema` da tabela contém todos os campos e suas definições em uma lista.

- `name` O nome do campo (id_registro, por exemplo)
- `description` (opcional) A descrição do conteúdo do campo
- `type` O tipo do campo (STRING, INTEGER, RECORD etc.)
- `mode` (opcional, padrão NULLABLE) Característica especial do campo (REQUIRED, REPEATED, NULLABLE, etc.)

### Exemplo

```YAML
  ...
  schema:
    - name: campo_teste
      description: Um campo de teste
      type: STRING
  ...
```

## Campos Array

Um campo array contém vários valores do seu tipo em formato de lista. Para definir um campo do tipo array use `mode: REPEATED` na definição do campo.

```YAML
- name: nm_dependentes
  type: STRING
  mode: REPEATED
```

## Campos Record

Um campo desse tipo contém outros campos internamente, sendo usado para representar informações comumente recebidas em json, por exemplo. Esse campo é definido usando como `type: RECORD` e seus campos internos são definidos em `fields`, usando as mesmas regras do `schema`.

Campos do tipo record podem conter outros campos do tipo record. Um campo record pode ser também um campo array.

```YAML
- name: rd_campo_record
  type: RECORD
  fields:
    - name: id_record
      type: INTEGER
```

## Campos de particionamento

O field de uma tabela particionada deve ser escolhido conforme seu mode.

- Uma tabela com `mode` TIME deve escolher um campo TIMESTAMP para fazer seu particionamento
- Uma tabela com `mode` RANGE deve escolher um campo numérico para fazer seu particionamento

## Outputs
name Nome recebido nas propriedades
