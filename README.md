# We Clean .CSV 🧹

Projeto em **Python + Pandas** para diagnóstico, limpeza assistida e exportação de arquivos CSV pelo terminal.

![We Clean .CSV — identidade visual](assets/we-clean-doodle-layout.png)

## Sobre o projeto

O **We Clean .CSV** nasceu como um projeto de estudo e portfólio para aplicar conceitos de análise e tratamento de dados com Python de forma simples, interativa e rastreável.

A proposta é permitir que o usuário carregue um CSV, visualize os principais problemas de qualidade e escolha como deseja tratar cada situação.

## Funcionalidades

- Importação segura de arquivos CSV
- Diagnóstico de linhas e colunas
- Identificação de tipos de dados
- Contagem de valores nulos
- Detecção de linhas duplicadas
- Detecção de colunas totalmente vazias
- Remoção opcional de colunas vazias
- Tratamento de nulos por:
  - remoção de linhas
  - valor numérico informado
  - média
  - mediana
  - moda
- Padronização de texto:
  - remoção de espaços nas extremidades
  - conversão para minúsculas
  - conversão para maiúsculas
- Nova verificação de duplicatas após tratamentos
- Relatório comparativo antes/depois
- Histórico das ações realizadas
- Exportação do CSV tratado

## Tecnologias

- Python 3
- Pandas

## Como executar

Clone o repositório e instale a dependência:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
python we_clean.py
```

O programa solicitará o caminho do arquivo CSV que será analisado.

## Fluxo do We Clean

```text
Importação
   ↓
Diagnóstico
   ↓
Colunas vazias
   ↓
Duplicatas
   ↓
Valores nulos
   ↓
Padronização de texto
   ↓
Nova verificação de duplicatas
   ↓
Relatório
   ↓
Exportação
```

## Identidade visual

O projeto também possui um conceito de interface neo-brutalista com:

- fundo amarelo;
- doodles relacionados a dados;
- cards brancos;
- bordas pretas;
- destaques em rosa/coral.

As artes estão na pasta `assets/`.

## Apoie o projeto

[☕ Buy Me a Coffee](https://www.buymeacoffee.com/lucasfrmg25)

## Autor

**Lucas Freire**
