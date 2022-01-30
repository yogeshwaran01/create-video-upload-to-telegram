# Create-video-upload-to-telegram

[![Create video and upload to telegram](https://github.com/yogeshwaran01/create-video-upload-to-telegram/actions/workflows/create-video-and-upload-to-telegram.yml/badge.svg)](https://github.com/yogeshwaran01/create-video-upload-to-telegram/actions/workflows/create-video-and-upload-to-telegram.yml)

Automatically download some images and audio from internet and make it as video and upload to [Telegram Channel](https://t.me/py2js)

## Stack

### 1. Python
  - [Request](https://docs.python-requests.org/en/latest/) and [Beautifulsoup4](https://docs.python-requests.org/en/latest/) to download images
  - [Pytube](https://pytube.io/en/latest/) to download audio from youtube
  - [FFMPEG](https://www.ffmpeg.org/) and [Moviepy](https://zulko.github.io/moviepy/) to edit video

### 2. Node.js
  [Telegraf.js](https://telegraf.js.org/) to handle Telegram bot API

### 3. Bash
  Bash scripting for automate the workflow between python to create video and node.js to upload a video to Telegram

### 4. Github Actions
  [Github Actions](https://docs.github.com/en/actions) to automate the bot to upload 3 three videos for run every 12 hours.
  
