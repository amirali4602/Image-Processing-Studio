from app.filters.base_filter import BaseFilter


class FilterManager:

    def __init__(self):

        self.filters: dict[str, BaseFilter] = {}


    def register(
        self,
        filter_instance: BaseFilter
    ):

        self.filters[
            filter_instance.name
        ] = filter_instance



    def get_filter(
        self,
        name: str
    ) -> BaseFilter:

        if name not in self.filters:
            raise ValueError(
                f"Filter '{name}' not found."
            )

        return self.filters[name]



    def available_filters(self):

        return list(
            self.filters.keys()
        )