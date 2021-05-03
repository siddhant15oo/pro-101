#sl.AmyE2_RkjboKBXIQMqIwCqxD2pDuHPd48_cImfvbyUFbbCmVPAJLv6VC5lUT2Nn7z_Uo7Wc1GHRkLJSXiho9EB9rwrg27qSBOigQJ4tZs7YZs0ChyTTY-qrfyLGNGS1Qna3rzKI

import dropbox

class TransferData():
    def __init__ (self,access_token):
        self.access_token=access_token

    def uplaod_file(self,file_from,file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
    def main():
           access_token = 'sl.AnF6zF-517SEBPsk3GrC45IFebvjHk5qjrjmB_9Nakxr-Da_9SaAkZnBKToZV0MhGBHm9j-JsXBuYWVpZr3uTi77x0SSkv5vT2v7RdoYc0EclsJxW6RxYaWdaC99STKEUY8Yq5c'

           transferData = TransferData(access_token)

            file_from = input (" pleas eneter file path:")
            file_to = input("enter full path to drop to dropbox:")  # The full path to upload the file to, including the file name
            # API v2
            transferData.upload_file(file_from, file_to)
            print("file has been uploaded")


#if __name__ == '__main__':
    main()

