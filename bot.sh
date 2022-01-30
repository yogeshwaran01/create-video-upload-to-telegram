#!/usr/bin/env bash

echo 'Auto Video making and upload it to Telegram'

echo 'Creating video ...'

python create.py --video simbu

echo 'Video Created :)'

echo 'Sending to Telegram ...'

node send.js v output.mp4

echo 'Video sended sucessfully :)'

rm output.mp4
