# Projeto de Reconhecimento Facial com RetinaFace e Flask

Este projeto é uma API em Flask que utiliza o modelo RetinaFace para detecção facial e a biblioteca DeepFace para reconhecimento facial e análise de expressões.

---

## Requisitos

- Python 3.8+
- As bibliotecas listadas no arquivo `requirements.txt` (veja abaixo)

---

## Como configurar o ambiente

### 1. Criar um ambiente virtual

No terminal, dentro da pasta do projeto, execute:

```bash
python -m venv venv
````

Isso cria uma pasta chamada `venv` com o ambiente virtual isolado.

### 2. Ativar o ambiente virtual

* No Windows:

```bash
venv\Scripts\activate
```

* No Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

Com o ambiente ativado, rode:

```bash
pip install -r requirements.txt
```

---

## Dependências

As bibliotecas utilizadas são:

```
flask==2.3.3
flask-cors==3.0.10
deepface==0.0.79
numpy==1.23.5
opencv-python==4.7.0.72
tensorflow==2.10.1
```

---

## Como rodar o projeto

Com o ambiente ativado, execute:

```bash
python app.py
```

O servidor Flask será iniciado e ficará aguardando requisições. Você pode usar seu frontend ou fazer requisições diretamente para a API.

---

## Funcionamento geral

* O backend em Flask recebe imagens via requisição HTTP.
* Utiliza o RetinaFace para detectar faces na imagem.
* Com a face detectada, o DeepFace realiza reconhecimento facial e análise de emoções.
* Retorna os resultados para o cliente (frontend, app, etc).

---

## Estrutura do projeto

```
/
|-- app.py                  # Código principal da API Flask
|-- requirements.txt        # Dependências do projeto
|-- README.md               # Este arquivo
|-- static/                 # Arquivos estáticos (opcional)
|-- templates/              # Templates HTML (opcional)
|-- venv/                   # Ambiente virtual (não subir no GitHub)
```

---

## Como contribuir

* Abra issues para bugs ou sugestões.
* Envie pull requests com melhorias.
* Mantenha o padrão de código e teste as mudanças localmente.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para detalhes.