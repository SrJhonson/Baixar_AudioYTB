# Importa a classe YouTube do módulo pytube
from pytube import YouTube
import re

while True:
    # Solicita ao usuário que insira o link do vídeo que deseja baixar
    link = input("Digite o Link do Vídeo que Deseja Baixar (ou 'sair' para terminar):")
    
    # Verifica se o usuário quer sair do loop
    if link.lower() == 'sair':
        break

    # Cria uma instância da classe YouTube, passando o link do vídeo como argumento
    yt = YouTube(link)

    # Trata o título do vídeo para remover caracteres não permitidos em nomes de arquivos
    title = re.sub('[^a-zA-Z0-9 \n\.]', '', yt.title)

    # Imprime o título do vídeo que está sendo baixado
    print("Baixando", title)

    #Baixa somente o Audio do vídeo e salva na pasta Baixados
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
    audio_stream.download(output_path="Baixados", filename=title + ".mp3")

    # Indica que o download foi concluído
    print("Download Concluído!")