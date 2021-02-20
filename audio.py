import pyaudio  
import wave  

def peticionVoz():
    chunk = 1024  

#ABRIMOS UBICACIÓN DEL AUDIO.  
    f = wave.open("a1.wav","rb")

#INICIAMOS PyAudio.
    p = pyaudio.PyAudio()  

#ABRIMOS STREAM
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)

#LEEMOS INFORMACIÓN  
    data = f.readframes(chunk)  

#REPRODUCIMOS "stream"  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  

#PARAMOS "stream".  
    stream.stop_stream()  
    stream.close()  

#FINALIZAMOS PyAudio  
    p.terminate()  