## 📊 Projeto ETL com Geração de Conteúdo via IA  
**Bootcamp Ciência de Dados – Santander | DIO**

Este projeto foi desenvolvido por **Jonatha Briano** como atividade prática do **Bootcamp de Ciência de Dados do Santander**, ofertado pela plataforma **DIO (Digital Innovation One)**.

O objetivo do projeto é demonstrar, de forma prática, a implementação de um **pipeline ETL (Extract, Transform, Load)** utilizando **Python**, **Pandas** e uma **API de Inteligência Artificial (Groq)** como fonte de dados textuais.

---

## 🧠 Visão Geral do Projeto

O pipeline ETL desenvolvido tem como finalidade:
- Ler dados de usuários a partir de um arquivo CSV
- Enriquecer esses dados com mensagens personalizadas geradas por um modelo de linguagem
- Persistir os dados transformados em um novo arquivo estruturado (JSON)

O projeto simula um cenário real de mercado, onde dados estruturados são combinados com dados não estruturados gerados por IA.

---

## 🔄 Pipeline ETL

### 1️⃣ Extract (Extração)

A etapa de extração consiste na leitura de dados estruturados a partir de um arquivo CSV utilizando a biblioteca **Pandas**.

- O arquivo `SDW2025.csv` contém informações básicas dos usuários
- Os dados são carregados em memória e convertidos para uma lista de dicionários
- Para cada usuário, é criada uma nova chave (`news`) que será utilizada nas próximas etapas

📌 **Objetivo da etapa**: disponibilizar os dados brutos em uma estrutura manipulável para transformação.

---

### 2️⃣ Transform (Transformação)

Na etapa de transformação, os dados extraídos são **enriquecidos com conteúdo gerado por Inteligência Artificial**.

#### 🔹 Uso da API Groq
- A API é utilizada como uma **fonte externa de dados**
- As mensagens geradas são personalizadas com o nome de cada usuário
- O conteúdo é limitado a 100 caracteres, conforme regra de negócio

#### 🔹 Boas práticas aplicadas
- Uso de variáveis de ambiente para armazenar a API Key
- Leitura da chave via `os.getenv()`
- Arquivo `.env` protegido e ignorado pelo Git

📌 **Importante**:  
Neste projeto, a resposta do modelo de linguagem é tratada como **dado não estruturado**, passando a integrar o fluxo de ETL.

Cada mensagem gerada é adicionada ao respectivo usuário, enriquecendo o conjunto de dados original.

---

### 3️⃣ Load (Carga)

Na etapa final, os dados transformados são persistidos em um arquivo JSON:

- O arquivo final contém os dados originais do CSV
- Inclui as mensagens personalizadas geradas pela IA
- O formato JSON facilita reutilização, análises futuras ou integração com outros sistemas

📌 **Resultado**:  
Um novo dataset enriquecido, pronto para consumo analítico ou aplicações futuras.

---

## 🎓 Aprendizados

Com este projeto foi possível consolidar conhecimentos sobre:
- Conceitos e implementação de pipelines ETL
- Manipulação de dados com Pandas
- Uso de APIs externas como fonte de dados
- Boas práticas de segurança e versionamento com Git/GitHub
- Aplicação prática de Inteligência Artificial em projetos de dados

---

## 🏁 Considerações Finais

Este projeto demonstra como pipelines ETL podem ir além de bases de dados tradicionais, incorporando Inteligência Artificial como parte do processo de extração e enriquecimento de dados, refletindo cenários reais do mercado de dados.



