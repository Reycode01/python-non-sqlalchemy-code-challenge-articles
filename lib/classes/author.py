from classes.many_to_many import Article

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []
        self._magazines = set()

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list(self._magazines)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        self._magazines.add(magazine)
        return article
    def topic_areas(self):
        areas = set()
        for article in self._articles:
            areas.add(article.magazine.category)
        return list(areas)


