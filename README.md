# We Clean .CSV 🧹

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/status-v1.0-success)
![License](https://img.shields.io/badge/license-Portfolio-lightgrey)

Projeto em **Python + Pandas** para diagnóstico, limpeza assistida e exportação de arquivos CSV diretamente pelo terminal.

> **v1.0 — primeira versão funcional do projeto.**

![We Clean .CSV — identidade visual](assets/we-clean-doodle-layout.png)

## ✨ Sobre o projeto

O **We Clean .CSV** nasceu como um projeto de estudo e portfólio para aplicar conceitos de análise e tratamento de dados com Python de forma simples, interativa e rastreável.

A proposta é permitir que qualquer pessoa carregue um arquivo CSV, visualize rapidamente os principais problemas de qualidade e escolha como deseja tratar cada situação antes da exportação.

## 🚀 Funcionalidades

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

## 🧰 Tecnologias

- Python 3
- Pandas

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/lucasfrmg25-del/we_clean_CSV.git
cd we_clean_CSV
```

Instale a dependência:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python we_clean.py
```

O programa solicitará o caminho do arquivo CSV que será analisado.

## 🧪 Teste rápido

O repositório inclui um arquivo de demonstração:

```text
exemplos/teste_inconsistencias.csv
```

Ao iniciar o programa, informe:

```text
exemplos/teste_inconsistencias.csv
```

Esse arquivo contém propositalmente valores nulos, uma linha duplicada, uma coluna totalmente vazia e variações de capitalização/espaçamento para demonstrar o fluxo de limpeza.

## 🔎 Exemplo: antes → depois

### Antes

```text
id | nome     | cidade        | idade | renda
1  | Ana      | " Vitória "   | 29    | 3200
3  | Carlos   | "vila velha " | 41    | NaN
5  | Erica    | "serra"       | 27    | 2900
5  | Erica    | "serra"       | 27    | 2900
6  | Fernando | "Vitória"     | NaN   | 3800
```

Problemas identificados:

- valores nulos;
- linha duplicada;
- espaços extras;
- inconsistências de capitalização;
- coluna totalmente vazia.

### Depois

Um fluxo possível de tratamento pode resultar em:

```text
✓ coluna totalmente vazia removida
✓ duplicata removida
✓ valores nulos tratados
✓ textos padronizados
✓ nova checagem de duplicatas executada
✓ CSV tratado exportado
```

O tratamento final depende das opções escolhidas pelo usuário durante a execução.

## 🧭 Fluxo do We Clean

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

## 🖥️ Exemplo de execução

```text
===== IMPORTAÇÃO DO ARQUIVO =====
Digite o caminho do arquivo CSV que deseja analisar:
exemplos/teste_inconsistencias.csv

✓ Arquivo carregado com sucesso!

===== DIAGNÓSTICO INICIAL =====
Quantidade de linhas: 10
Quantidade de colunas: 6
Total de valores nulos: ...
Total de linhas duplicadas: 1

===== TRATAMENTO DE DUPLICATAS =====
Deseja remover as linhas duplicadas? [S/N]:

===== TRATAMENTO DE VALORES NULOS =====
1 - Remover linhas com valores nulos
2 - Substituir nulos por um número informado
3 - Substituir nulos pela média
4 - Substituir nulos pela mediana
5 - Substituir nulos pela moda
6 - Manter os dados originais

===== AÇÕES REALIZADAS =====
1. ...
2. ...
```

## 🎨 Identidade visual

O conceito visual planejado para uma futura interface utiliza uma estética neo-brutalista com:

- fundo amarelo;
- doodles relacionados a dados;
- cards brancos;
- bordas pretas;
- destaques em rosa/coral.

As artes do projeto ficam na pasta `assets/`.

## 📁 Estrutura

```text
we_clean_CSV/
│
├── we_clean.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── VERSION
│
├── exemplos/
│   └── teste_inconsistencias.csv
│
└── assets/
    ├── we-clean-ui-concept.png
    └── we-clean-doodle-layout.png
```

## 🗺️ Roadmap

- [x] Diagnóstico de CSV
- [x] Tratamento de nulos
- [x] Remoção de duplicatas
- [x] Tratamento de colunas vazias
- [x] Padronização textual
- [x] Relatório de ações
- [x] Exportação de CSV
- [ ] Interface gráfica/web
- [ ] Relatório visual para download
- [ ] Novas regras de qualidade de dados

## 🌐 Links

- [Portfólio](https://lucasfrmg25-del.github.io/)
- [GitHub](https://github.com/lucasfrmg25-del)
- [☕ Buy Me a Coffee](https://www.buymeacoffee.com/lucasfrmg25)

## 👨‍💻 Autor

**Lucas Freire**

Projeto desenvolvido como parte do meu portfólio prático em **Python, análise de dados e automação de processos de qualidade de dados**.
