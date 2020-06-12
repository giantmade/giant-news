from news.cms_apps import NewsApp


class TestNewsApp:
    """
    Test case for the News
    """

    def test_get_urls_method(self):
        """
        Test get_urls method on the News class
        """

        assert NewsApp().get_urls() == ["news.urls"]
