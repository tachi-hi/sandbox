import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

filename = "sampleSounds/doremi_stereo.wav"

fs, data = wav.read(filename)

# convert data to more convenient form
time = np.asarray(range(data.shape[0]), dtype=np.float32)/fs
data_fp = data.astype(np.float32) / np.max(abs(data))

# show data
print("sampling rate is ", fs)
print("data shape is ", data_fp.shape)


# show waveform
def plot_waveform(time, array):
    plt.plot(time, array)
    plt.xlabel("Time [s]")
    plt.savefig("waveform.png")


data_fp[:,0] += 2 # left channel
data_fp[:,1] *= 0.8 # right channel
plot_waveform(time, data_fp)


# stft
import scipy.fftpack as FFT
import cmath
def window(len):
    t = np.asarray(range(len), dtype=np.float32)/len * 2 * np.pi
    return (1. - np.cos(t))/2.

def stft(array_, L=256, S=128):
    # zero pad
    array = np.zeros(S + len(array_) + L)
    array[S:S+len(array_)] = array_

    # params and window
    n_frame = int(np.ceil( len(array_) / S ))
    n_freq = L / 2 + 1
    win = window(L)

    # alloc
    spec = np.ndarray((n_frame, n_freq),dtype=np.float32)

    # compute
    for t in range(n_frame):
        short = array[S*t : min(S*t+L, len(array))]
        c = FFT.fft(short * win)
        a = np.absolute(c[:n_freq])
        spec[t,:] = a

    return spec

def spec_show(spec_):
    spec = spec_**0.3
    plt.clf()
    plt.imshow(spec,interpolation="nearest", aspect='auto', origin='lower')
    plt.set_cmap("hot")
    plt.savefig("spec.png")

spec = stft(data_fp[:,1], L = 1024, S = 256)
spec = spec.transpose()
spec_show(spec)
