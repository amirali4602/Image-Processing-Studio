from app.filters.filter_manager import FilterManager

from app.filters.high_pass.laplacian_filter import LaplacianFilter
from app.filters.histogram.histogram_matching import HistogramMatching
from app.filters.intensity.log_transform import LogTransform
from app.filters.intensity.piecewise_linear import PiecewiseLinearTransform
from app.filters.low_pass.box_filter import BoxFilter
from app.filters.low_pass.gaussian_filter import GaussianFilter
from app.filters.high_pass.sobel_filter import SobelFilter
from app.filters.high_pass.log_filter import LoGFilter
from app.filters.intensity.gamma_transform import GammaTransform
from app.filters.histogram.histogram_equalization import HistogramEqualization
def register_filters(
    manager: FilterManager
):

    manager.register(
        BoxFilter()
    )

    manager.register(
        GaussianFilter()
    )

    manager.register(
        SobelFilter()
    )

    manager.register(
        LaplacianFilter()
    )

    manager.register(
        LoGFilter()
    )

    manager.register(
        LogTransform()
    )

    manager.register(
        GammaTransform()
    )

    manager.register(
        PiecewiseLinearTransform()
    )

    manager.register(
        HistogramEqualization()
    )

    manager.register(
        HistogramMatching()
    )