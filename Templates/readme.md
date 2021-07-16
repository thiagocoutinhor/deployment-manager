Os templates são formas mais robustas de se criar uma configuração através do deployment manager. Com eles podemos criar padrões de projetos reutilizáveis e de mais simples configuração.

O deployment manager permite que os templates sejam feitos tanto em Jinja quanto em python, mas pela simplicidade, iremos disponibilizar apenas os templates em Jinja

# Como usar um template

Se os arquivos de template estiverem em outro diretório que não o do YAML de configuração, informe o diretório relativo para a importação.

Um template é um arquivo de configuração que termina com .jinja e que deve ser importado no YAML de configurações do projeto antes de ser usado.

```YAML
import:
  - path: template-01.yaml.jinja
  - path: template-02.yaml.jinja
```

Depois de importá-lo, use declare que o tipo do recurso é o template.

```YAML
- name: nome-recurso
  type: template-01.yaml.jinja
  properties:
    propriedade1: valor
```

Note que as propriedades que você deve informar para esse template são definidas por ele, não pelo recurso que ele cria. Consulte a documentação do template que você está utilizando para saber quais propriedades você deve informar.

# Outputs

A maioria dos templates tem alguma informação que pode ser referenciada por outros recursos (ver [Dependências e Referências](../reame.md)). Nesse caso elas são declaradas diretamente no template, permitindo que outros recursos as referenciem.

Veja a documentação de cada template para saber quais propriedades são externadas por outputs.

# Referências

- [Documentação do deployment manager sobre templates](https://cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template)

- [Documentação oficial do Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
