from dataclasses import dataclass


@dataclass
class FilterParameter:

    name: str

    value: object

    parameter_type: str

    minimum: object | None = None

    maximum: object | None = None

    step: object | None = None

    options: list | None = None