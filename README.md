# ✈️ Airline Passenger Satisfaction: Análise de CX End-to-End

![Status](https://img.shields.io/badge/STATUS-CONCLUÍDO-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Power BI](https://img.shields.io/badge/Power_BI-Desktop-yellow?style=for-the-badge&logo=powerbi)
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blueviolet?style=for-the-badge&logo=kaggle)

## 📘 Sobre o Projeto

Este projeto foi desenvolvido como uma iniciativa de **Extensão Universitária**, com o objetivo de democratizar o conhecimento em Análise de Dados.

Mais do que apenas apresentar gráficos, este repositório serve como um **guia prático (tutorial)** de como transformar uma planilha bruta em inteligência de negócio. Aqui, documentei todo o processo: desde a limpeza de dados com Python até a construção de um Dashboard Executivo no Power BI.

O case analisa dados reais de **129.880 passageiros** para responder a uma pergunta crítica: *O que faz um cliente amar ou odiar uma companhia aérea?*

---

## 🎯 Objetivos de Aprendizado

Ao explorar este projeto, você verá na prática:

1.**Engenharia de Dados (ETL):** Como tratar datasets massivos, traduzir colunas e lidar com valores nulos usando a biblioteca `Pandas`.

2.**Modelagem de Dados:** Como criar medidas DAX eficientes no Power BI (sem arrastar e soltar colunas aleatoriamente).

3.**Data Storytelling:** Como estruturar um layout executivo que guia o olhar do tomador de decisão.

4.**Análise Estatística:** Correlação entre variáveis (Ex: Como o atraso de voo impacta matematicamente a satisfação).

---

## 🗂️ Estrutura do Repositório

```text
📁 Airline-Satisfaction-Project
│
├── 📂 data
│   ├── train.csv                # Dataset original de treino (Kaggle)
│   ├── test.csv                 # Dataset original de teste (Kaggle)
│   └── dados_aviacao_final.csv  # Arquivo tratado gerado pelo script Python
│
├── 📂 scripts
│   └── preparacao_dados.py      # Script Python para limpeza e unificação
│
├── 📂 dashboard
│   └── Airline_Dashboard.pbix   # Arquivo do Power BI completo
│
└── README.md                    # Documentação do projeto

```

---

## 🚀 Guia de Reprodução (Tutorial)

Quer rodar esse projeto na sua máquina para estudar? Siga o passo a passo:

Passo 1: Preparação dos Dados (Python)
Os dados originais vêm separados e em inglês. O script preparacao_dados.py unifica as bases e traduz para PT-BR.

Pré-requisitos:

```text

pip install pandas numpy

```

Como funciona o Script (Resumo):

```text

import pandas as pd

# 1. Carregar e Unificar

df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')
df = pd.concat([df_train, df_test])

# 2. Limpeza (Drop IDs e Nulos)

df = df.drop(['Unnamed: 0', 'id'], axis=1)
df['Arrival Delay in Minutes'] = df['Arrival Delay in Minutes'].fillna(0)

# 3. Exportação

df.to_csv('dados_aviacao_final.csv', index=False)

```

## 📊 Principais Insights Descobertos

Através da visualização de dados, chegamos a conclusões que contradizem o senso comum:

O "Ponto de Ruptura" da Paciência: Existe uma correlação inversa perfeita entre atraso e satisfação. A tolerância do passageiro se esgota aos 30 minutos. A partir desse ponto, a satisfação despenca, independentemente da qualidade do serviço a bordo.

O Abismo entre Classes:

Classe Executiva: 69% de Satisfação.

Classe Econômica: 18% de Satisfação.

Conclusão: A empresa entrega um serviço premium excelente, mas falha no básico (Econômica) para a maioria dos passageiros.

Tecnologia > Comida: Na Classe Econômica, a nota de "Wifi" e "Check-in Online" tem maior correlação com a insatisfação do que "Comida e Bebida". O passageiro moderno prefere estar conectado a estar bem alimentado.

## 🤝 Contribuição e Comunidade

Este é um projeto Open Source feito para a comunidade. Sinta-se à vontade para sugerir ideias, análises e chamar no LinkedIn para trocarmos ideias.
