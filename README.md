# Andréanne & Francis — projet statique sans NPM

Ce dossier est une version statique du preview Base44, préparée pour fonctionner sans `npm install`, sans Vite et sans serveur Node.

## Structure

```text
index.html
404.html
manifest.json
.htaccess
serve-local.py
lancer-localement.bat
assets/
  index-B_E0lVNA.js
  index-DB42JtjG.css
  images/
```

## Ouvrir localement

Le plus fiable est d’utiliser le petit serveur Python inclus, parce que les scripts JavaScript en `type="module"` peuvent être bloqués quand on ouvre directement le fichier avec `file://`.

Sur Windows, double-clique sur :

```text
lancer-localement.bat
```

Ou en terminal :

```bash
python serve-local.py
```

Puis ouvre :

```text
http://localhost:4173
```

## Déployer

Tu peux déposer tout le contenu du dossier sur un hébergement statique classique : Cloudflare Pages, Netlify, serveur Apache, Nginx, etc.

Pour Apache, le fichier `.htaccess` inclus ajoute un fallback vers `index.html`, utile si une route React est appelée directement.

## Notes

- Aucun package NPM n’est requis.
- Le bundle React généré par Base44 est déjà compilé dans `assets/index-B_E0lVNA.js`.
- Les appels d’initialisation Base44 ont été neutralisés pour éviter une dépendance au backend Base44 en local.
- Les placeholders `HERO_PLACEHOLDER`, `GALLERY_1` à `GALLERY_12` et `QR_PLACEHOLDER` ont été remplacés par les images locales du dossier `assets/images/`.
- Le CSS utilise encore l’import Google Fonts original. Si tu veux une version 100 % hors ligne, il faudra soit télécharger les polices, soit remplacer les familles par des polices système.
