import os
import ffmpeg

start_dir = os.getcwd()

def convert_to_mp4(mkv_file):
    no_extension = str(os.path.splitext(mkv_file))
    with_mp4 = no_extension + ".mp4"
    ffmpeg.input(mkv_file).output(with_mp4).run()
    print("Finished converting {}".format(no_extension))


convert_to_mp4('/home/daniel-catto/Vídeos/caninos_brancos-acao_aventura.mkv')