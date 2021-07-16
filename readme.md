O deployment manager do Google Cloud permite que criemos toda a infraestrutura de um projeto de forma automatizada e confiável. Com ele, usamos um script YAML para definir quais recursos nosso projeto usará e todas as configurações necessárias para criá-lo. Com ele, além de automatizarmos a criação do ambiente do projeto, teremos uma listagem centralizada e detalhada de todos os recursos necessários para a operacionalização do projeto.

# Como montar o YAML

O YAML de criação de recursos é formado por uma raiz resources que contém a lista de recursos. Cara um dos recursos deve ter um name, um type e um properties com as propriedades necessárias para a configuração do recurso em si.

O name do recurso deve ser único em todo o documento.

O type deve conter a referência do recurso sendo criado. Veja quais são os recursos nativamente suportados [aqui](https://cloud.google.com/deployment-manager/docs/configuration/supported-resource-types) e os campos derivado por gcp-type [aqui](https://cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

As properties são as características do recurso sendo criado. Essas propriedades são os mesmos campos enviados ao se chamar a API rest do recurso. Leia a documentação do tipo (acima) para a descobrir que propriedades são necessárias para recurso escolhido.

## Referências e Dependências

É comum os serviços sendo criados terem dependências entre si (como uma tabela dependendo do dataset no BigQuery). Nesse caso é necessário que eles declarem sua dependência par que o deployment manager espere a criação dos recursos superiores antes de tentar criar os dependentes.

Para declarar a dependência de um recurso no outro use a declaração da dependência dentro da metadata do recurso.

```YAML
- name: nome_recurso
  type: tipo_recurso
  ...
  metadata:
    dependsOn
      - recurso_superior1
      - recurso_superior2
  ...
```

Para se referenciar alguma propriedade de outro recurso, a referência deve seguir o padrão: `$(ref.[NOME DO RECURSO].[PROPRIEDADE])`.

## Exemplo

A seguir um breve exemplo de um script de criação de um projeto com uma conta de serviço com o papel de Storage Admin, um bucket e um pubsub.

```YAML
resources:
  - name: svc-conta-servico
    type: iam.v1.serviceAccount
    properties:
      accountId: nome-conta-servico

  - name: svc-role-storage-admin
    type: gcp-types/cloudresourcemanager-v1:virtual.projects.iamMemberBinding
    metadata:
      dependsOn:
        - svc-conta-servico
    properties:
      resource: projeto-001
      role: roles/storage.admin
      member: serviceAccount:$(ref.svc-conta-servico.email)

  - name: bkt-bucket-1
    type: storage.v1.bucket
    properties:
      project: projeto-001
      location: us-central1

  - name: psb-pubsub-1
    type: pubsub.v1.topic
    properties:
      topic: topico-001
```

# Conta de serviço que executa o script

Ao executar um script no deployment manager ele vai executar a criação dos recursos usando a conta de serviço do cloud services `[NUMERO DO PROJETO]@cloudservices.gserviceaccount.com`. Assim, essa conta deve ter as permissões necessárias para a criação e alteração de todos os recursos envolvidos, caso já não possua.

# Execução do script

Para a execução do script é necessário o uso da linha de comando do gcloud passando o nome do deploy, que deve ser único no projeto, e o script YAML, que deve estar local na máquina.

## Criando um deploy
Ao criar um deploy o deployment manager tentará criar todos os recursos listados no resources caso eles não existam. E tentará alterar os recursos que já existam com as configurações passadas no script.

### Exemplo

Criação de um deploy chamado “meu-deploy” com o script no arquivo “config.yaml”:

```shell
gcloud deployment-manager deployments create meu-deploy --config config.yaml
```

## Consultando um deploy

A [interface do deployment manager](https://console.cloud.google.com/dm/deployments) lista todos os deploys executados no projeto e seu status atual. Através dela é possível acessar os deploys individualmente e acompanhar sua execução, consultar os recursos criados por eles e abrir as configurações usadas para isso.

## Alterando um deploy

Ao alterar um deploy o deployment manager verificará quais recursos foram alterados no script e fará as alterações necessárias para igualar as configurações.

### Exemplo

Atualização de um deploy chamado “meu-deploy” com o script no arquivo “config.yaml”:

```shell
gcloud deployment-manager deployments update meu-deploy --config config.yaml
```

## Removendo um deploy

Ao remover um deploy o deployment manager tentará remover todos os recursos do deploy automaticamente, a menos que seja informado que os recursos devem ser abandonados como estão ao se remover o deploy.

Para a remoção do deploy, há também a possibilidade de se utilizar a [interface do deployment manager](https://console.cloud.google.com/dm/deployments), que vai perguntar se os recursos devem ser removidos ou abandonados.

## Exemplos

Remoção de um deploy chamado “meu-deploy” através da linha de comando:

```shell
gcloud deployment-manager deployments delete meu-deploy
```

Remoção de um deploy chamado “deploy-abandonado” com a opção de abandonar os recursos:

```shell
gcloud deployment-manager deployments delete deploy-abandonado --delete-policy=abandon
```

# Referências

- [Saiba mais sobre YAML](https://en.wikipedia.org/wiki/YAML#:~:text=YAML%20a%20recursive%20acronym%20for,is%20being%20stored%20or%20transmitted.)

- [Página oficial do Deployment Manager](https://cloud.google.com/deployment-manager)

- [Página de tutoriais do Deployment Manager](https://cloud.google.com/deployment-manager/docs/quickstart)

- [Tipos de recursos suportados](https://cloud.google.com/deployment-manager/docs/configuration/supported-resource-types)

- [Tipos de recursos por gcp-types](https://cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types)

- [Interface web do deployment manager no projeto](https://console.cloud.google.com/dm/deployments)
