<h1 align="center">📊 YouTube Data Extractor & MongoDB Insights</h1>

<h2>📎 Índice</h2>
<p align="center">
    <a href="#about">🤔 Sobre</a> | 
    <a href="#tech">⚙️ Tecnologias utilizadas</a> | 
    <a href="#struct">🗂 Estrutura do projeto</a> | 
    <a href="#run">🚀 Como rodar o projeto</a> | 
    <a href="#insights">📈 Exemplos de insights gerados</a>
</p>

<h3>📹 Demonstração:</h3>

![Demo](/assets/youtools-proj.gif)

<h2 id="about">🤔 Sobre</h2>

<p align="justify">Um projeto prático para coletar, armazenar e analisar dados de vídeos do YouTube usando Python, MongoDB e visualização de dados.</p>

<p align="justify">Desenvolvido como trabalho prático de NoSQL, este projeto permite:</p>
<ul>
  <li>Extrair os vídeos mais populares de um canal.</li>
  <li>Coletar comentários, transcrição, livechat e superchat de cada vídeo.</li>
  <li>Armazenar todas as informações em um banco MongoDB.</li>
  <li>Gerar gráficos de insights sobre os dados coletados.</li>
</ul>

<h2 id="tech">⚙️ Tecnologias utilizadas</h2> 
<ul>
    <li>Python 3.10+</li>
    <li>MongoDB</li>
    <li>YouTool (coleta de dados do YouTube)</li>
    <li>Matplotlib & WordCloud (visualizações)</li>
    <li>Pymongo</li>
    <li>dotenv</li>
</ul>

<h2 id="struct">🗂 Estrutura do projeto</h2>

```
youtube_nosql_project/
├── analysis/
│   ├── __init__.py
│   └── insights.py
├── database/
│   ├── __init__.py
│   └── mongo_handler.py
├── youtube_extractor/
│   ├── __init__.py
│   ├── channel_scraper.py
│   └── video_scraper.py
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
```

<h2 id="run">🚀 Como rodar o projeto</h2>

<p>Para executar o projeto, siga os passos abaixo:</p>

<ol>
    <li>Clone o repositório:</li>
</ol>

```bash
git clone https://github.com/seu-usuario/youtube-nosql.git
cd youtube-nosql
```

<ol start="2">
    <li>Crie e ative o ambiente virtual yt-nosql</li>
</ol>

Linux/macOS:

```bash
python3 -m venv yt-nosql
source yt-nosql/bin/activate
```

Windows (CMD):

```bash
python -m venv yt-nosql
yt-nosql\Scripts\activate
```

<ol start="3">
    <li>Instale as dependências:</li>
</ol>

```bash
pip install -r requirements.txt
```

<ol start="4">
    <li>Configure as variáveis de ambiente: crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
</ol>

```plaintext
MONGO_URI=mongodb://localhost:27017
DB_NAME=youtube_nosql
YT_API_KEYS=ABCKEY
```

<p>Você pode usar o arquivo `.env.example` como modelo.</p>

<ol start="5">
    <li>Inicie o MongoDB:</li>
</ol>
<p>Se você estiver usando o MongoDB localmente, certifique-se de que o serviço está rodando:</p>

```bash
sudo service mongod start
```

<ol start="6">
    <li>Execute o script principal:</li>
</ol>

```bash
python main.py
```

<p align="justify">Você será solicitado a inserir a URL de um canal do YouTube (ex: https://www.youtube.com/c/CanalXYZ)</p>

<h2 id="insights">📈 Exemplos de insights gerados</h2>

<ul>
    <li>Gráfico de barras: número de comentários por vídeo.</li>
    <li>Nuvem de palavras: palavras mais frequentes nos comentários.</li>
</ul>
