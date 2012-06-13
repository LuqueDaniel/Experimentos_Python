#ecoding: utf-8

from dropbox import client, session, rest

app_key = '' #APP KEY
app_secret = '' #APP_SECRET
app_type = 'app_folder'

sesion = session.DropboxSession(app_key, app_secret, app_type)
request_token = sesion.obtain_request_token()

url = sesion.build_authorize_url(request_token)
print "url:", url
print "Visite la URL de arriba y permita la aplicación, a continuación presione intro"
raw_input()

access_token = sesion.obtain_access_token(request_token)

cliente = client.DropboxClient(sesion)

archivo = 'muestra.txt'
subiendo = cliente.put_file('/muestra1.txt', archivo)
print subiendo