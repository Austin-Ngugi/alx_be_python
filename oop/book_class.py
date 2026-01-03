class Book: 

    def __init__(self, title:str, author:str, year:int ): 

        self.title = title 
        self.author = author 
        self.year = year 
        
    def __del__ (self, title):
        self.title.close()
        print( f"deleting {self.title}")
        
    def _str_(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def _repr_(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    
        
        
