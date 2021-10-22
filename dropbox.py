import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A61hweln8tDxBr9TRWoWSjr7mwiGWGDaMQOnEHvPpfOYWmD4RA0jcn0tVqAhMnb2mkP1942Akh_6GLEHpcHUeE3U9XL-p3PCm4mTM3xou7ii3w9acQl8rS5W1_95omjKt7OSWSM'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to be transfered:- ")
    file_to = input("enter the full path for dropbox")

  

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

main()
