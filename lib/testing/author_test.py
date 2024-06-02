import pytest
from classes.many_to_many import Article, Magazine, Author

class TestAuthor:
    """Tests for the Author class"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """Author name is of type str and cannot change"""
        author = Author("Carry Bradshaw")

        with pytest.raises(AttributeError):
            author.name = "ActuallyTopher"

    def test_name_len(self):
        """Author name is longer than 0 characters"""
        author = Author("Carry Bradshaw")

        assert len(author.name) > 0

    def test_has_many_articles(self):
        """Author has many articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert len(author.articles()) == 2
        assert article_1 in author.articles()
        assert article_2 in author.articles()

    def test_articles_of_type_article(self):
        """Author articles are of type Article"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")

        assert isinstance(author.articles()[0], Article)

    def test_has_many_magazines(self):
        """Author has many magazines"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_2, "2023 Eccentric Design Trends")

        assert len(author.magazines()) == 2
        assert magazine_1 in author.magazines()
        assert magazine_2 in author.magazines()

    def test_magazines_of_type_magazine(self):
        """Author magazines are of type Magazine"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")

        assert isinstance(author.magazines()[0], Magazine)

    def test_magazines_are_unique(self):
        """Author magazines are unique"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_2, "2023 Eccentric Design Trends")
        Article(author, magazine_2, "Carrara Marble is so 2020")

        assert len(set(author.magazines())) == len(author.magazines())

    def test_add_article(self):
        """Creates and returns a new article given a magazine and title"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = author.add_article(magazine_1, "How to wear a tutu with style")
        article_2 = author.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert isinstance(article_1, Article)
        assert len(author.articles()) == 2
        assert len(magazine_1.articles()) == 1
        assert len(magazine_2.articles()) == 1
        assert article_1 in magazine_1.articles()
        assert article_2 in magazine_2.articles()

    def test_topic_areas(self):
        """Returns a list of topic areas for all articles by author"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "Carrara Marble is so 2020")

        assert len(author.topic_areas()) == 2
        assert set(author.topic_areas()) == {"Fashion", "Architecture"}

    def test_topic_areas_are_unique(self):
        """Topic areas are unique"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_1, "Dating life in NYC")
        author.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert len(set(author.topic_areas())) == len(author.topic_areas())
        assert len(author.topic_areas()) == 2
        assert "Fashion" in author.topic_areas()
        assert "Architecture" in author.topic_areas()
        assert set(author.magazines()) == {magazine_1, magazine_2}





