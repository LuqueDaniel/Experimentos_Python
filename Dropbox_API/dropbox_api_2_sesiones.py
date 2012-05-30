#!/usr/bin/env python
#encoding: utf-8

from dropbox import client, session, rest

app_key = '' # APP KEY
app_secret = '' # APP SECRET
app_type = 'app_folder'

sesion = session.DropboxSession(app_key, app_secret, app_type)
request_token = sesion.obtain_request_token()

url = sesion.build_authorize_url(request_token)
print "url:", url
print "Visite la URL de arriba y permita la aplicación, a continuación presione intro"
raw_input()

access_token = sesion.obtain_access_token(request_token)

cliente = client.DropboxClient(sesion)
informacion = cliente.account_info()

# print informacion

for i in informacion.items():
	if i[0] == 'display_name':
		print "Nombre de usuario:\t%s" % (i[1])
	elif i[0] == 'country':
		print "Pais:\t%s" % (i[1])
	elif i[0] == 'quota_info':
		print "Shared: %i" % (i[1]['shared'])
		print "quota: %i" % (i[1]['quota'])
		print "Normal: %i" % (i[1]['normal'])
	elif i[0] == 'email':
		print "Email:\t%s" % (i[1])