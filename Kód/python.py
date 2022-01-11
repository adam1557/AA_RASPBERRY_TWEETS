#-*- coding: utf-8 -*-
import sys
from twython import Twython
import Adafruit_DHT
import tweepy
from subprocess import call
from datetime import datetime

API_KULCS = 'WhBF8H3Q4uIcQSCEnfDbV2gUn'
API_KULCS_TITKOS = 'Qw25YmYlk1SMwB7GTjxProRXrU6bRApeik7C7h37IdBpbh7icU'
HOZZAFERES_KULCS = '2762628255-l5f7d7sxqyyoK0PR4gbMCQzSz6RFvQN0L9rqwnI'
HOZZAFERES_KULCS_TITKOS = 'b5K30HuugSCi1IAQ6jQZZi8u2wQMjbjFJGNRDc0MmlEBy'

api=Twython(API_KULCS,API_KULCS_TITKOS,HOZZAFERES_KULCS,HOZZAFERES_KULCS_TITKOS)
sensor=22
pin=4
h, t = Adafruit_DHT.read_retry(sensor,pin)
BEV=('AZ AA_RASPBERRY_TWEETS ISMÉT JELENTKEZIK:\n\n')
FO= ('A hőmérséklet: {0:0.1f} celsuius-fok, a páratartalom: {1:0.1f}%.'.format(t,h))

i = datetime.now()
datum_most = i.strftime('%Y%m%d-%H%M%S')
fenykep_nev = datum_most + '.jpg'
cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + fenykep_nev
call ([cmd], shell=True)


auth = tweepy.OAuthHandler(API_KULCS, API_KULCS_TITKOS)
auth.set_access_token(HOZZAFERES_KULCS, HOZZAFERES_KULCS_TITKOS)

api = tweepy.API(auth)

foto_eleresiut = '/home/pi/' + fenykep_nev
BEF = '\n\nA TWEET alján található  pillanatkép az AA_RASPBERRY_TWEETS állomáson  lett megörökítve, az alábbi dátummal: ' + i.strftime('%Y/%m/%d %H:%M:%S')
api.update_with_media(foto_eleresiut, status=BEV+FO+BEF)
