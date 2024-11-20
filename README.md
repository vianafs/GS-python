# Power Wise - Energy Consumption Tracker

<h2>Detalhes do Projeto</h2>
<h3>O objetivo deste projeto é criar uma aplicação que permita:</h3>
<ul>
  <li>Cadastrar fontes de consumo de energia (ex.: geladeira, chuveiro, etc.).</li>
  <li>Listar as fontes cadastradas.</li>
  <li>Calcular o consumo mensal em kWh e o custo estimado para todas as fontes registradas.</li>
  <li>Salvar e carregar dados automaticamente de um arquivo .txt.</li>
</ul>
<h3>Funcionalidades</h3>
<ol>
  <li>Cadastro de novos items consumidores:</li>
  <ul>
    <li>Permite adicionar novos itens de consumo com nome, potência em kW e tempo de uso diário em horas.</li>
  </ul>
  <li>Listagem de consumidores:</li>
  <ul>
    <li>Exibe todos os items consumidores cadastrados.</li>
  </ul>
  <li>Cálculo de custo mensal:</li>
  <ul>
    <li>Calcula e exibe o consumo mensal e o custo total estimado.</li>
  </ul>
  <li>Persistência de dados:</li>
  <ul>
    <li>Os dados são armazenados e carregados automaticamente do arquivo dados_energia.txt.</li>
  </ul>
</ol>

<h2>Instruções de Uso</h2>
<h3>Pré-requisitos</h3>
<ul>
  <li>Python 3.6 ou superior instalado no sistema.</li>
</ul>
<h3>Instalação</h3>
<h4>1. Clone o repositório ou baixe os arquivos do projeto:</h4>

```bash
git clone https://github.com/vianafs/.git
```
<h4>2. Certifique-se de que o Python esteja instalado no ambiente. Para verificar:</h4>

```bash
python --version

```
<h3>Execução</h3>
<h4>1. Abra o terminal na pasta do projeto.</h4>
<h4>2. Execute o programa principal:</h4>

```bash
python PowerWise.py

```
<h4>3. Siga as instruções do menu exibido no terminal.</h4>
<h2>Dependências</h2>
<p>Este projeto utiliza apenas bibliotecas padrão do Python, como:</p>
<ul>
  <li>os: Para manipulação de arquivos e sistema operacional.</li>
</ul>
<h2>Instruções Específicas</h2>
<ol>
  <li><h4>Adicionar uma nova fonte de consumo</h4></li>
  <ul>
    <li>Escolha a opção 1 no menu</li>
    <li>Digite o nome do aparelho ou fonte.</li>
    <li>Insira a potência em kW (ex.: 0.3 para 300W).</li>
    <li>Informe o tempo de uso diário em horas.</li>
  </ul>
  <li><h4>Listar os consumidores registrados</h4></li>
  <ul>
    <li>Escolha a opção 2 no menu.</li>
    <li>O programa exibirá todos os consumidores cadastrados.</li>
  </ul>
  <li><h4>Calcular o consumo total</h4></li>
    <ul>
    <li>Escolha a opção 4 no menu.</li>
    <li>O programa calculará o consumo mensal e o custo estimado com base nos dados registrados e na tarifa fixa (R$ 0,73/kWh).</li>
  </ul>
  <li><h4>Salvar e carregar dados</h4></li>
    <ul>
    <li>Os dados são salvos automaticamente no arquivo dados_energia.txt ao sair do programa.</li>
    <li>Ao reiniciar o programa, os dados são carregados automaticamente.</li>
  </ul>
</ol>
<h2>Contribuição</h2>
<h3>Contribuições são bem-vindas! Para propor melhorias:</h3>
<ol>
  <li>Faça um fork deste repositório.</li>
  <li>Crie uma branch para sua feature:</li>

```bash
git checkout -b nova-feature

```
  <li>Envie um pull request detalhando as alterações propostas.</li>
</ol>
<h2>Licença</h2>
<h4>Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.</h4>
<h2>Contato</h2>
<h4>Desenvolvedor: Rafael Viana</h4>
<h4>Email: rafaelmenezesviana@gmail.com </h4>

