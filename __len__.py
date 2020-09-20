class NoLenDefined:
    
    def __len__(self):
        
        return 1
    
    pass

obj = NoLenDefined()
len(obj)
