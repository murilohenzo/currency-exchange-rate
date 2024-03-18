#criação de monad para ser implementada
class Maybe:
    def __init__(self, value):
        self.value = value
    
    def bind(self, function):
        if self.value is None:
            return Maybe(None)
        else:
            return Maybe(function(self.value))
        
     