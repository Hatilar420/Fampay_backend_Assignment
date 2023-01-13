
class CommonDomain:
    def __init__(self, model) : 
        self.model = model
    
    def create(self, data):
        self.model(**data)
        self.model.save()
    
    def bulk_create(self, data):
        res = []
        for i in data:
            res.append(self.model(**data))
            self.model.bulk_create(res)
