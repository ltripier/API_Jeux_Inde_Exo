#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from cgi import escape

def index(environ, start_response):
    """ Page d'accueil accessible à '/'
       Affiche simplement une phrase. """
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Ceci est la page d'accueil."]

def hello(environ, start_response):
    """ Page accessible à la route '/hello/'
       Affiche la phrase que l'utilisateur a passée en paramètre. """
    # recupère la phrase depuis l'url si elle a été spécifiée
    # Sinon, affiche Hello World.
    args = environ['https://tastedive.com/davidmaneacheong/bookmarks']
    if args:
       phrase = escape(args[0])
    else:
       phrase = 'Hello World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [phrase]

def not_found(environ, start_response):
    """ Appelée si l'adresse est inconnue. """
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

# associe les adresses aux fonctions
urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)$', hello)
]

def application(environ, start_response):
    """ Dispatche les requêtes aux fonctions précédentes. """
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
       match = re.search(regex, path)
       if match is not None:
           environ['https://tastedive.com/davidmaneacheong/bookmarks'] = match.groups()
           return callback(environ, start_response)
    return not_found(environ, start_response)