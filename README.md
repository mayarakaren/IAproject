# 🌊 Projeto de Reconhecimento de Emoções com DeepFace + Flask

Este é um projeto educacional e interativo de **inteligência artificial** que usa visão computacional para **reconhecer emoções faciais** e retornar uma imagem temática de fundo do mar baseada na emoção detectada.

A aplicação conta com:
- Um backend em **Flask**,
- Detecção de emoções com **DeepFace**,
- Um frontend simples em **HTML/CSS/JS** para interação visual.

---

## 💡 Como funciona?

1. O usuário envia uma foto pelo frontend (ou via API).
2. O backend processa a imagem usando o **DeepFace** e identifica a **emoção dominante**.
3. De acordo com a emoção (`happy`, `sad`, `neutral`), o sistema retorna **uma imagem aleatória de fundo do mar** correspondente.
4. Essa imagem é exibida dinamicamente no frontend.

---

## 📌 Tecnologias utilizadas

- [Python 3.10.11](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [DeepFace](https://github.com/serengil/deepface)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- HTML, CSS e JavaScript (frontend)

---

## 📦 Requisitos do sistema

- Python 3.10.11 instalado
- Git (opcional para clonar)
- Ambiente virtual (recomendado)

---

## 🛠️ Como configurar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
````

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

* **Windows**:

```bash
venv\Scripts\activate
```

* **Linux/Mac**:

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r backend/requirements.txt
```

---

## 🚀 Como executar a aplicação

Com o ambiente virtual ativado:

```bash
python backend/app.py
```

O servidor será iniciado em `http://127.0.0.1:5000`.

Abra o arquivo `frontend/index.html` no navegador ou acesse o frontend automaticamente se o `index.html` estiver sendo servido pelo Flask.

---

## 🎯 Endpoints disponíveis

### `/analisa-rosto`

`POST` com uma imagem (campo `imagem` via FormData)

**Retorno:**

```json
{
  "emocao": "happy",
  "imagem_fundo": "/static/mar_feliz/2.png"
}
```

**Erros possíveis:**

```json
{
  "erro": "Nenhuma imagem enviada"
}
```

---

## 🧠 Emoções reconhecidas

O projeto suporta as seguintes emoções através do `DeepFace`:

* `happy`
* `sad`
* `neutral`

Se a emoção não for reconhecida, será usada uma imagem neutra por padrão.

---

## 📁 Estrutura de pastas

```
/
├── backend/
│   ├── app.py                 # API principal
│   ├── requirements.txt       # Bibliotecas necessárias
│   └── static/
│       ├── mar_feliz/         # Imagens para emoção "happy"
│       ├── mar_triste/        # Imagens para emoção "sad"
│       └── mar_neutro/        # Imagens para emoção "neutral"
│
├── frontend/
│   ├── index.html             # Página principal
│   ├── resultado.html         # Página de exibição da emoção
│   ├── script.js              # Lógica JS do frontend
│   └── style.css              # Estilo visual
│
├── .gitignore                 # Arquivos a serem ignorados pelo Git
└── README.md                  # Este documento
```

---

## ✅ `requirements.txt`

```
flask==2.3.3
flask-cors==3.0.10
deepface==0.0.79
numpy==1.23.5
opencv-python==4.7.0.72
tensorflow==2.10.1
```

---

## 🙋‍♀️ Como contribuir

1. Faça um fork deste repositório
2. Crie uma branch com sua feature: `git checkout -b minha-feature`
3. Faça commit das suas mudanças: `git commit -m 'Minha feature'`
4. Faça push para a sua branch: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✨ Créditos

Este projeto foi desenvolvido com fins educacionais e criativos, conectando inteligência artificial, tecnologia e arte interativa.

---