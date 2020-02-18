import json, falcon

class MyObject:
    def on_get(self, req, res):
        content = {
            'name': 'Lynard',
            'age': 38,
            'country': 'New Zealand'
        }
        res.body = json.dumps(content)

api = falcon.API()
api.add_route('/test', MyObject())