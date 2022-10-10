# app-for-notion-api
App que consome a API do notion e puxa alguns dados de um database do notion.

Dada uma lista de IDs de banco de dados que contém as atividades planejadas por mim para serem realizadas ao longo da semana, o app se conecta a todos esses bancos de dados pelos IDs e lista no terminal apenas as atividades que estão marcadas com a data de hoje.

## Como funciona?
No .env você especifica uma variável chamada "DATABASES" e utiliza *multiline values* para especificar todos os IDs dos banco de dados. O que o app é procurar nesses databases pela coluna "Nome" e pela coluna "Data", e salva em uma lista todos os valores da coluna "Nome" que estão com o valor da coluna "Data" igual a data de hoje. Após isso o app chama uma função que lista na linha de comando esses valores da coluna "Nome" que o app puxou.
