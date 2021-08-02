# Workflow Template

## Propriedades

- `id` Identificador do template
- `region` (opcional, padrão us-central1) Região do dataproc
- `timeout` (opcional, padrão 1 hora) Tempo, em segundos, para o timeout de execução

- `cluster` Informações do cluster a ser criado
  - `nameNome` do cluster
  - `bucket` Bucket para uso do cluster
  - `image` (opcional, padrão 1.4-debian10) Imagem do SO do cluster
  - `serviceAccountEmail` da conta de serviço que executará o processo
  - `network` (opcional) Configurações de rede (não pode ser informada junto com subnetwork)
  - `subnetwork` (opcional) Configurações de subrede  (não pode ser informada junto com network)
  - `properties` (opcional) Propriedades aplicadas a todo o cluster (todos os jobs são afetados)
  - `webInterfaces` (opcional, padrão true) Se o cluster permite acesso as interfaces dos componentes
  - `master` (opcional) Informações sobre o master
    - `num` (opcional, padrão 1) Número de masters a serem usados
    - `machine` (opcional, padrão n1-standard-2) O tipo de máquina a ser usado
    - `disk` (opcional) Disco dos masters
      - `type` (opcional, padrão pd-standard) Tipo do disco
      - `size` (opcional, padrão 15) Tamanho em gigas do disco
  - `workers` (opcional) Informações sobre os workers
    - `num` (opcional, padrão 2) Número de workers a serem usados
    - `machine` (opcional, padrão n1-standard-2) O tipo de máquina a ser usado
    - `disk` (opcional) Disco dos workers
      - `type` (opcional, padrão pd-standard) Tipo do disco
      - `size` (opcional, padrão 15) Tamanho em gigas do disco
  - `initialization` (opcional) Script de inicialização do cluster
    - `executableFile` Caminho para o arquivo a ser executado
    - `timeout` (opcional, padrão 120 segundos) Tempo de timeout da execução
- `pysparkJobs` Lista com os jobs pyspark a serem executados no cluster
  - `id` A identificação do job
  - `mainPy` O caminho para o python principal a ser executado
  - `pyFiles` (opcional) Lista do caminho para arquivos python a serem usados
  - `prerequisites` (opcional) Lista de job id que são prerequisitos para a execução desse job
  - `args` (opcional) Lista de argumentos que o job espera
  - `properties` (opcional) Lista de propriedades do job
  - `parameters` (opcional) Lista de parâmetros que esse workflow recebe
  - `labels` (opcional) Labels do template

## Parameters e Args

As configurações de `parameters` em um workflow e dos `args` dentro de cada job estão intrinsicamente conectadas. Os parameters são uma forma centralizada de enviar valores para um ou mais jobs sendo executados, como, por exemplo, a data dos dados a serem processados.

> A notação do campo `fields` dos parâmetros indica qual o parâmetro a ser substituido por referência: `jobs[NOME DO JOB].pysparkJobs.args[NUMERO DO ARGUMENTO]`

Segue um exemplo de como configurar corretamente essas duas propriedades do workflow.

### Args

```YAML
pysparkJobs:
  - id: job-exemplo-1
    mainPy: gs://bucket-codigo/exemplo1.py
    args:
      - DATA
  - id: job-exemplo-2
    mainPy: gs://bucket-codigo/exemplo2.py
    args:
      - URL
      - DATA
```

### Parameters

```YAML
parameters:
  - name: DATA
    fields:
      - jobs['job-exemplo-1'].pysparkJobs.args[0]
      - jobs['job-exemplo-2'].pysparkJobs.args[1]
  - name: URL
    fields:
      - jobs['job-exemplo-2'].pysparkJobs.args[0]
```

## Outputs

- `id` Identificador do template