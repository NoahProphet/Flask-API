import json
import models

class UserSerilizers:
    def __init__(self, input, many=False):
        self.many = many
        self.input = input
        
    @property 
    def data(self):
        result = [] if self.many else None
        if self.many:
            for d in self.input:
                result.append(d.serilizer)
            return result
        else:
            return self.input.serilizer
        
    def create(self):
        data = json.loads(self.input)
        
        if self.many:
            for d in data:
                models.User.create(username=d['username'], email=d['email'])
        else:
            models.User.create(username=data['username'], email=data['email'])
        return True
        