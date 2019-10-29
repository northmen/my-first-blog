import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as nfft
import scipy as sp
from scipy.signal import stft

import wave
import struct

import random
from guitar import *

def readSound(FileName) :
        """getSound(FileName) --> L
        Read a .wav file  and return data as a list L.
        L is a list of integers, which are the values of sampled sound signal."""
        
        L = []
        f = wave.open(FileName, 'rb')

        nb_channels = f.getnchannels()
        nb_samples = f.getnframes()
        size_sample = f.getsampwidth()
        fS = f.getframerate()

        print("Number of channels :", nb_channels)
        print("Sampling frequency :", fS)
        print("size of each sample :", size_sample, "bytess")
        print("Number of samples :", nb_samples)

        print("Open the file...")
        
        if size_sample == 2 :
            for i in range(nb_samples) :
                b = f.readframes(1)
                val = struct.unpack('h', b)
                L.append(val[0])
        elif size_sample == 1 :
            for i in range(nb_samples) :
                b = f.readframes(1)
                val = struct.unpack('b', b)
                L.append(val[0])
        else :
            print("File format non recognized")
            
        f.close()
        return L
        
def pcolormesh(stop=True, song = "./results/file.wav", directory_to_save = './results/'):
    

    #song = "./results/file.wav"
    #song = "string_kuznechik_full_7"
    print("read {}".format(song))
    f3 = readSound(song)
    #f3 = readSound("music_writer/{}.wav".format(song))
    f3 = np.array(f3)

    f = f3
    N = len(f)
    stepen = 6 # change this to 7 or 8 to increase the accuracy
    f,b,SF=sp.signal.stft(f,fs=N,nperseg=N/pow(2,stepen))


    for i in range(SF.shape[0]):
        a = SF[i,:]
        k = 0.2
        #a[a<a.max()*k] = 0
        SF[i,:] = a


    #------------------------------------
    def grid():
        x_max = 12.28
        a = 0.2
        #plt.hlines(f19, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f18, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f17, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f16, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f15, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f14, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f13, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f12, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f11, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f10, 0, x_max, 'r', '-.')

        plt.hlines(f24, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f23, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f22, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f21, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f20, 0, x_max, 'orange', '--')

        plt.hlines(f33, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f32, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f31, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f30, 0, x_max, 'y', '--')

        plt.hlines(f44, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f43, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f42, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f41, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f40, 0, x_max, 'g', '--')


        plt.hlines(f54, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f53, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f52, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f51, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f50, 0, x_max, 'b', '--')


        plt.hlines(f64, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f63, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f62, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f61, 0, x_max, 'w', '--', alpha = a)
        plt.hlines(f60, 0, x_max, 'violet', '--')

    #------------------------------------
    def find_max(a):
        for i in range(len(a)):
            if a[i] <= 0.5 * a.max():
                a[i] = 0
            else:
                a[i] = 1
        return a
    #------------------------------------

    #directory_to_save = './results/'

    file0 = directory_to_save + 'test0.jpg'
    file1 = directory_to_save + 'test1.jpg'
    file2 = directory_to_save + 'test2.jpg'
    file3 = directory_to_save + 'test3.jpg'

    #plt.pcolormesh(b*N,f[:50],np.abs(SF[:50,:]))
    hight = int(100/pow(2, stepen-6))
    plt.pcolormesh(b*N/500000.*12,f[:hight]/5100.*440,np.abs(SF[:hight,:]))
    fig = plt.gcf()
    fig.set_size_inches(6.4, 4.8)
    #plt.savefig(file0, dpi=100)
    #------------------------------------
    plt.ylabel("frequencies")
    plt.xlabel("time")
    plt.title("temporel frequential representation")
    #plt.subplots_adjust(left=0.1, right=1.9, top=0.5, bottom=0.1)

    if stop:
        plt.show(block=True)


    def plot_fourier(file, size, g=False):
        plt.pcolormesh(b*N/500000.*12,f[:100]/5100.*440,np.abs(SF[:100,:]))
        fig = plt.gcf()
        fig.set_size_inches(size)
        #plt.show(block=False)
        if g==True:
            grid()
        fig.savefig(file, dpi=100)
        print("file {} is ready".format(file))
    


    plot_fourier(file0, (18.5, 10.5))
    plot_fourier(file2, (5, 3))

    plot_fourier(file1, (18.5, 10.5), g=True)
    plot_fourier(file3, (5, 3), g=True)
    

#pcolormesh(stop=True)

