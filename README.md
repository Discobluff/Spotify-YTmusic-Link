# Spotify-YTmusic-Link

## Description

A tool to link Spotify playlists to YouTube Music. When a new song is added to a YT Music playlist, it will be added to the linked Spotify playlist as well. This is useful for users who want to maintain their playlists across both platforms without having to manually update them. Only work in one direction (YT Music to Spotify) for now.

## Installation

Clone this repository and install the dependencies:

## Setup

### Activate Spotify API


### Activate YouTube Music API

- Créer un projet sur [Google Cloud Console](https://console.cloud.google.com/)
- Activer l'API YouTube Data v3 pour ce projet
- Créer des identifiants d'API (clé API) pour ce projet et copier la clé API générée dans le .env

**Les playlists doivent être au moins en non répertorié**

## Usage

```bash
python3 main.py
```