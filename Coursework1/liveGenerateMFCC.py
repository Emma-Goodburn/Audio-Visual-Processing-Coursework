import sounddevice as sd
import featureExtraction
import datetime

# Takes mic input and generates MFCC for that audio clip to be used for live testing of speech rec

sampleRate = 16000
seconds = 2

signal = sd.rec(seconds * sampleRate, samplerate=sampleRate, channels=1)
sd.wait()

sd.play(signal, sampleRate)

folderName = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

mfcc_features = featureExtraction.main(signal, sampleRate, "signal_MFCC", folderName)