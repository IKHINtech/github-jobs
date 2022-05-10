import requests

from be_test.app.models import Jobs


class BackendService:
    url = 'http://dev3.dansmultipro.co.id/api/recruitment/positions.json'

    def get_all(self):
        response = requests.get(url=self.url)
        if response.status_code == 200:
            data = response.json()

            for i in data:
                try:
                    already_data = Jobs.objects.get(id=i['id'])
                    if already_data:
                        pass
                except Jobs.DoesNotExist:
                    Jobs.objects.create(**i)

            return data
        else:
            raise response.status_code

    def get_by_id(self, id):
        response = requests.get(url=f'http://dev3.dansmultipro.co.id/api/recruitment/positions/{id}')
        if response.status_code == 200:
            data = response.json()
        return data
