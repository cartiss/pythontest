import requests

class Yandex_Request:
    def __init__(self, yandex_token):
        self.yandex_token = yandex_token
        self.headers = {'Authorization': f'OAuth {self.yandex_token}', 'Content-Type': 'application/json',
                        'Accept': 'application/json'}

    def create_folder(self, BASE_URL):
        response = requests.put(BASE_URL, headers=self.headers, params={
            'path': 'testfolder'
        })
        return response.status_code

if __name__ == '__main__':
    test = Yandex_Request('AgAAAAAnT4gjAADLWxNiaFqSQk1Zl4YxP-nbi5o')
    print(test.create_folder())