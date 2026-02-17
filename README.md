# 👁️ Detector de Fadiga Humana com IA
<p align="center">
  <video src="https://github.com/user-attachments/assets/ef0016d1-0bfb-473f-affc-9e4ac4debc58" controls="controls" style="max-width: 600px;">
  </video>
</p>

## 📝 Sobre o Projeto
Este projeto utiliza **Inteligência Artificial** e **Visão Computacional** para monitorar o rosto do usuário através da webcam e detectar sinais de cansaço ou sonolência. É uma solução ideal para sistemas de segurança em veículos ou monitoramento de produtividade.

## 🚀 Como o Projeto Funciona?
O sistema mapeia **468 pontos do rosto** em tempo real usando a malha facial do Mediapipe. O foco principal está no cálculo do **EAR (Eye Aspect Ratio)**:

* **Monitoramento:** A IA mede a distância entre as pálpebras superior e inferior.
* **Análise:** O código possui um filtro que ignora piscadas rápidas (naturais).
* **Alerta:** Se os olhos permanecerem fechados por mais de **1.5 segundos**, o sistema dispara um alerta visual vermelho na tela e um sinal sonoro (BIP).



## 🛠️ Tecnologias Utilizadas
* **Python 3.12**: Linguagem base.
* **Mediapipe**: Biblioteca do Google para rastreamento facial de alta performance.
* **OpenCV**: Para captura e processamento de vídeo da webcam.
* **Winsound**: Para emitir alertas sonoros diretamente no PC.

## ⚙️ Instalação e Uso
1. Instale as bibliotecas: `pip install opencv-python mediapipe pygame-ce`
2. Rode o script: `python detector_fadiga.py`
3. Saia do programa pressionando a tecla **ESC**.

---
Desenvolvido por **David Kauã** 🚀
