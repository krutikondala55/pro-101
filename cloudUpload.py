import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

        

def main():
    access_token = 'sl.A4CKIriCSfccM8QH4t5DQpxMR6EDSgYlzd8pym_bQcJAzhP4hXzo2uUb43FrXjTBYudJqD4u-2YccZcUmucmNKB2myK4QY77a7fRiDEVOcpl-hTpDf6KO8brVLFpHeUqJMh9KmM'
    transferData = TransferData(access_token)

    file_from = str(input('Enter The Folder Path to Transfer:- '))
    file_to = str(input('Enter The Path to upload to dropbox:- '))  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('File Has Been Uploaded')

main()