import cv2
import mediapipe as mp
import winsound

# Inicializando a IA do Mediapipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
cap = cv2.VideoCapture(0)

# Contador para evitar que o alarme toque em piscadas normais
contador = 0

print("Sistema iniciado! Pressione 'ESC' para sair.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1) # Efeito espelho
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Pegando pontos da pálpebra superior e inferior do olho direito
            # Usamos os pontos 159 e 145 do mapa facial do Mediapipe
            ponto_cima = face_landmarks.landmark[159]
            ponto_baixo = face_landmarks.landmark[145]
            
            # Calculando a distância vertical entre os pontos (EAR simplificado)
            abertura = abs(ponto_cima.y - ponto_baixo.y)

            # Mostra o valor da abertura na tela para te ajudar a calibrar
            cv2.putText(frame, f"Abertura: {abertura:.3f}", (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

            # --- LÓGICA DO ALARME ---
            # Se a abertura for menor que 0.015, o olho é considerado 'fechado'
            if abertura < 0.015:
                contador += 1
                
                # O alarme só toca se o olho ficar fechado por mais de 25 frames
                # Isso ignora piscadas normais e foca em sono real (aprox. 1.5 a 2 segundos)
                if contador > 25: 
                    cv2.putText(frame, "!!! FADIGA DETECTADA !!!", (100, 200),
                                cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 0, 255), 3)
                    winsound.Beep(1000, 500) # Som de alerta
            else:
                # Se abrir o olho, o contador zera na hora
                contador = 0

    cv2.imshow('Detector de Fadiga - David', frame)

    # Aperte ESC para fechar a janela
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
