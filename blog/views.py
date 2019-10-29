from django.shortcuts import render
from django.utils import timezone
from .models import Post
#from .pcolormesh import *
#from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
#import numpy as np
#import matplotlib.pyplot as plt

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {})

#from flask import Flask, render_template, jsonify
#import test

#app = Flask(__name__)

#@app.route('/', methods=['POST', 'GET'])
#def index():
#    if request.method == "POST":
#        plt.plot([1,2], [1,2])
#        plt.show()#

#    return render_template('index.html')
"""
def post_list(request):
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    response = HttpResponse(content_type = 'image.png')
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(response)
    return response
 """