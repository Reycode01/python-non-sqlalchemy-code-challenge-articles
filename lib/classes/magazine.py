@property
def name(self):
    return self._name

@property
def category(self):
    return self._category

@name.setter
def name(self, value):
    if isinstance(value, str) and 2 <= len(value) <= 16:
        self._name = value
    else:
        raise ValueError("Name must be a string between 2 and 16 characters")

@category.setter
def category(self, value):
    if isinstance(value, str) and len(value) > 0:
        self._category = value
    else:
        raise ValueError("Category must be a non-empty string")

def add_article(self, article):
    self._articles.append(article)
    
def article_titles(self):
    """Returns list of titles strings of all articles written for that magazine"""
    if self._articles:
        return [article.title for article in self._articles]
    else:
        return []


    
    





    

