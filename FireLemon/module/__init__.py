class Module:
    def __init__(self, metadata = None, function = None):
        
        self.metadata = metadata
        
        # self.function = function()

    def options(self):
        return self.metadata['options']
    
    def set(self, options):
        self.metadata['options'] = options
