# libreria para autenticarse en el drive, se debe tener permisodel desarrollador 
# si no estas en la lista de usuarios aporbados va denegar su acceso
from pydrive.auth import GoogleAuth
#libreria para crear, modificar y eliminar contenio del dirve
from pydrive.drive import GoogleDrive
#fechas
from datetime import date
from datetime import datetime
from datetime import time

def gurdarArchivo():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() 
    drive = GoogleDrive(gauth)

    fecha = str(datetime.now())
    exte='.avi'
    peatones='peatones'
    circulos='circulos'
    suma1= peatones + fecha + exte
    suma2= circulos + fecha + exte


    folderName = 'alma'  # Please set the folder name.

    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file1=drive.CreateFile({'title': suma1,'parents': [{'id': folder['id']}]}) 
            file1.SetContentFile('DetecciónDePeatones.avi')
            file1.Upload()
            file2=drive.CreateFile({'title': suma2,'parents': [{'id': folder['id']}]}) 
            file2.SetContentFile('Dectector_mov.avi')
            file2.Upload()



