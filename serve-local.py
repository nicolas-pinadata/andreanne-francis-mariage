#!/usr/bin/env python3
"""Petit serveur local sans dépendance NPM.

Usage :
  python serve-local.py
Puis ouvrir http://localhost:4173
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

PORT = 4173
ROOT = Path(__file__).resolve().parent

class StaticSpaHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Sert les vrais fichiers quand ils existent, sinon retourne index.html.
        raw_path = path.split('?', 1)[0].split('#', 1)[0]
        translated = Path(super().translate_path(path))
        if translated.exists() and translated.is_file():
            return str(translated)
        if raw_path.startswith('/assets/') or raw_path in ('/manifest.json', '/favicon.ico'):
            return str(translated)
        return str(ROOT / 'index.html')

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(ROOT)
    server = ThreadingHTTPServer(('localhost', PORT), StaticSpaHandler)
    print(f'Site disponible ici : http://localhost:{PORT}')
    print('Ctrl+C pour arrêter le serveur.')
    server.serve_forever()
