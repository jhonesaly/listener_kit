import os
from pocketsphinx import LiveSpeech

# Configuração do reconhecimento
speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
)

print("Say the word! ")

# Início do loop de reconhecimento
for phrase in speech:
    audio = phrase.segments(detailed=True)
    
    recognized_text = phrase.hypothesis()
    
    if recognized_text:
        print("you said:", recognized_text)

        # Verifica o comando e executa a ação correspondente
        if recognized_text.lower() == "execute chrome":
            os.system("start Chrome.exe")  # Substitua pelo comando correto se necessário
            print("Executing...")

        break

# Caso nenhum comando seja reconhecido
else:
    print("Didn't understand.")
