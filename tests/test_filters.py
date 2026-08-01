from app.filters.filter_manager import FilterManager
from app.filters.test_filter import TestFilter


def test_filter_manager():

    manager = FilterManager()

    manager.register(
        TestFilter()
    )


    assert "Test Filter" in (
        manager.available_filters()
    )


    filter = manager.get_filter(
        "Test Filter"
    )


    assert filter.name == "Test Filter"