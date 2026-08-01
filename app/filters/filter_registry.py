from app.filters.filter_manager import FilterManager

from app.filters.low_pass.box_filter import BoxFilter
from app.filters.low_pass.gaussian_filter import GaussianFilter



def register_filters(
    manager: FilterManager
):

    manager.register(
        BoxFilter()
    )

    manager.register(
        GaussianFilter()
    )