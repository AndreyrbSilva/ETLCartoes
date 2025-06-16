# ETLCartoes
# 📊 ETL de Estoque de Cartões - Banco Central do Brasil

Este projeto realiza o processo de Extração, Transformação e Carga (ETL) dos dados públicos sobre estoque de cartões de pagamento divulgados pelo Banco Central do Brasil. Ele gera arquivos .csv e um banco de dados SQLite, além de notebooks com análises exploratórias e estatísticas dos dados.

# 📁 Estrutura do Projeto

```bat

.
├── datasets/             # Dados salvos em CSV e SQLite
│   ├── estoque_cartoes.db
│   └── estoque_cartoes_20241.csv # Exemplo de arquivo gerado
├── src/                  # Módulos de extração, transformação e carga
│   ├── extractTransform.py
│   ├── load.py
│   └── __init__.py
├── Relatorio.ipynb       # Notebook com análises exploratórias
├── AnaliseEstatistica.ipynb # Novo notebook com análise estatística
├── main.py               # Script principal do ETL
└── requirements.txt      # Dependências do projeto
```
# 🚀 Como Executar

Instale as dependências:

Bash

pip install -r requirements.txt
Execute o pipeline ETL:

Bash

python main.py
O script buscará os dados do Banco Central para o trimestre definido (default: 20241 no main.py) e salvará os dados transformados em .csv e .db dentro da pasta datasets/.

Exemplo de saída esperada:

Less

[→] Iniciando ETL de estoque de cartões para o trimestre 20241
[✔] CSV salvo em: datasets/estoque_cartoes_20241.csv
[✔] Dados salvos em SQLite: datasets/estoque_cartoes.db → estoque_cartoes
[✓] ETL de estoque de cartões finalizada com sucesso.
# 🧠 Funcionalidades

🔄 Extração de dados via API pública do Banco Central do Brasil.
🧹 Transformações simples nos dados (conversão para minúsculas, garantia de tipo string para trimestre, ordenação).
💾 Persistência em arquivos .csv (com separador ; e decimal ,) e banco de dados .db (SQLite).
📊 Notebooks interativos (Relatorio.ipynb e AnaliseEstatistica.ipynb) para análise exploratória e estatística.
🛠️ Suporte opcional à exportação para MySQL (requer configuração de credenciais no src/load.py).
🔧 Parâmetros

Trimestre: No formato AAAAT (ex: 20241 para o 1º trimestre de 2024). O padrão pode ser alterado diretamente no main.py.
Separador CSV: ; (padrão para CSV gerado).
Separador decimal: , (padrão para CSV gerado).
📊 Fonte de Dados

Os dados são provenientes da API oficial do Banco Central do Brasil, acessando informações sobre:

Estoque de cartões emitidos e ativos, categorizados por bandeira, função e produto. Atualizados trimestralmente, refletem o total acumulado até o fim de cada trimestre.
📋 Dicionário de Dados

Nome	Tipo	Título	Descrição
trimestre	texto	Trimestre	Ano e trimestre da informação no formato AAAAT (ex: 20231 para o 1º trimestre de 2023).
nomebandeira	texto	Bandeira do cartão	Nome da bandeira do cartão (ex: Visa, Mastercard, American Express).
nomefuncao	texto	Função do cartão	Função do cartão: Crédito, Débito ou Pré-pago.
produto	texto	Produto do cartão	Categoria atribuída ao cartão (ex: Empresarial, Intermediário, Básico).
qtdcartoesemitidos	inteiro	Quantidade de cartões emitidos	Total acumulado de cartões emitidos até o final do trimestre, excluindo cartões cancelados.
qtdcartoesativos	inteiro	Quantidade de cartões ativos	Cartões que realizaram pelo menos uma transação nos últimos 12 meses até o fim do trimestre (considerados ativos).

Exportar para as Planilhas
📈 Análise Exploratória de Dados (AED) - Relatorio.ipynb

Este relatório técnico tem como objetivo extrair, transformar, analisar e visualizar os dados públicos disponibilizados pela API do Banco Central do Brasil sobre o estoque de cartões no país. A análise se refere à quantidade de cartões emitidos e ativos, segmentados por bandeira, tipo de produto e função (crédito, débito etc.), ao longo dos trimestres.

Este notebook segue as etapas do processo ETL (Extração, Transformação e Carga), incluindo:

Extração dos dados da API do Banco Central.
Tratamento e padronização dos dados.
Análise exploratória com visualizações.
Conclusões com base nos padrões observados.
Sumário das Análises:
Após a extração e carregamento dos dados em um banco SQLite, o notebook realiza as seguintes etapas de tratamento e análise:

1. Tratamento dos Dados:
Verificação de dados faltantes e duplicados.
Remoção de dados faltantes (se houver).
Conversão da coluna trimestre de string para o tipo datetime para facilitar análises temporais.
2. Estatísticas Descritivas:
Visão geral do DataFrame (df.info()).
Resumo estatístico das colunas numéricas e categóricas (df.describe(include='all')).
3. Totais e Proporções de Cartões:
Cálculo do total de cartões emitidos e ativos.
Determinação da proporção de cartões ativos vs. inativos.
Visualização da comparação entre emitidos e ativos por meio de gráficos de barras.
4. Médias de Cartões por Registro:
Cálculo da média de cartões emitidos e ativos por registro (linha).
Visualização dessas médias em gráficos de barras.
5. Análise por Categorias:
Top 5 Bandeiras com Mais Cartões Emitidos: Identifica e visualiza as bandeiras com maior volume de emissão de cartões (ex: VISA, MasterCard, Elo).
Top Funções de Cartão (por Cartões Emitidos): Analisa a distribuição de cartões emitidos por função (Débito, Crédito, Pré-Pago).
Top 5 Produtos por Cartões Emitidos: Mostra os produtos de cartão com maior quantidade de emissões (ex: Básico Internacional, Básico Nacional).
6. Análise Temporal (Exemplo com Cartões de Crédito):
Filtragem e agregação de dados para cartões de crédito emitidos por trimestre.
Visualização da tendência de emissão de cartões de crédito ao longo do tempo.
7. Cartões Ativos e Taxa de Ativação por Trimestre:
Cálculo do total de cartões ativos por trimestre.
Determinação do percentual de cartões ativos sobre emitidos por trimestre, revelando a taxa de ativação ao longo do tempo.
8. Taxa de Ativação por Função e Produto:
Análise do percentual de cartões ativos sobre emitidos por função (Crédito, Débito, Pré-Pago), indicando qual função tem a maior taxa de ativação.
Identificação e visualização dos Top 5 Produtos com Maior e Menor Taxa de Ativação, fornecendo insights sobre a performance de diferentes produtos.
# 📊 Análise Estatística Detalhada - AnaliseEstatistica.ipynb

Este notebook foca em uma análise estatística descritiva aprofundada dos dados de estoque de cartões, com o objetivo de identificar características centrais e de dispersão nas quantidades de cartões emitidos e ativos, além de padrões de agrupamento temporal.

Foco da Análise:
Medidas de Tendência Central: Médias, medianas e modas.
Medidas de Dispersão: Desvio padrão.
Agrupamentos Temporais: Análises por mês e por trimestre.
Sumário das Análises:
1. Carregamento e Preparação dos Dados:
Os dados são carregados do banco de dados SQLite estoque_cartoes.db.
A coluna trimestre é convertida para o tipo datetime e novas colunas ano_mes (formato 'YYYY-MM') e trimestre_periodo (formato 'YYYYQX') são criadas para facilitar os agrupamentos temporais.
2. Estatísticas Descritivas Gerais:
Um resumo estatístico abrangente (df.describe(include="all")) é apresentado, fornecendo a contagem, valores únicos, valor mais frequente (top), frequência, média, desvio padrão, mínimo, 25º percentil, 50º percentil (mediana), 75º percentil e máximo para todas as colunas.
3. Medidas de Tendência Central:
As medidas de tendência central para as quantidades de cartões emitidos e ativos são:

Médias:
qtdcartoesemitidos: 13.649.544,93
qtdcartoesativos: 4.565.302,72
Medianas:
qtdcartoesemitidos: 2.017.354,00
qtdcartoesativos: 638.978,50
Modas:
qtdcartoesemitidos: 218,00
qtdcartoesativos: 0,00
4. Medidas de Dispersão (Desvio Padrão):
O desvio padrão indica a dispersão dos dados em torno da média:

qtdcartoesemitidos: 32.090.516,97
qtdcartoesativos: 8.931.789,88
5. Agrupamento por Mês (ano_mes):
As médias mensais de cartões emitidos e ativos revelam flutuações ao longo do ano:

ano_mes	qtdcartoesemitidos	qtdcartoesativos
2023-03	7.395.850,54	2.371.899,00
2023-06	14.438.696,40	5.944.957,33
2023-09	14.484.573,15	5.194.776,31
2023-12	37.431.728,83	8.564.547,50
2024-03	9.983.917,47	4.794.751,33
2024-06	10.592.426,08	2.681.535,33
2024-09	4.147.889,28	1.582.701,28
2024-12	35.976.035,50	10.626.691,38

Exportar para as Planilhas
6. Agrupamento por Trimestre (trimestre_periodo):
As médias trimestrais consolidam a visão sobre a emissão e ativação de cartões:

trimestre_periodo	qtdcartoesemitidos	qtdcartoesativos
2023Q1	7.395.850,54	2.371.899,00
2023Q2	14.438.696,40	5.944.957,33
2023Q3	14.484.573,15	5.194.776,31
2023Q4	37.431.728,83	8.564.547,50
2024Q1	9.983.917,47	4.794.751,33
2024Q2	10.592.426,08	2.681.535,33
2024Q3	4.147.889,28	1.582.701,28
2024Q4	35.976.035,50	10.626.691,38

Exportar para as Planilhas
# 📦 Requisitos

Python 3.8+
pandas
requests
sqlite3 (integrado ao Python)
sqlalchemy
pymysql (para MySQL opcional)
matplotlib
seaborn
plotly
# 📄 Licença

Este projeto é livre para uso educacional e pessoal, utilizando dados públicos disponibilizados pelo Banco Central do Brasil.
