import warnings
from typing import Annotated, TYPE_CHECKING

from .component import DEFAULT_COMPONENT, Component
from .key import FromComponent

if TYPE_CHECKING:
    from typing import Union as FromDishka
else:
    class FromDishka:
        def __init__(self, component: Component = None):
            if component is None:
                self.component = DEFAULT_COMPONENT
                warnings.warn(
                    "Annotated[Cls, FromDishka()] is deprecated "
                    "use `FromDishka[Cls]` or "
                    "`Annotated[Cls, FromComponent()]` instead",
                    DeprecationWarning,
                    stacklevel=2,
                )

            else:
                self.component = component
                warnings.warn(
                    "Annotated[Cls, FromDishka(component)] is deprecated "
                    "use `Annotated[Cls, FromComponent(component)]` instead",
                    DeprecationWarning,
                    stacklevel=2,
                )

        def __class_getitem__(cls, item):
            return Annotated[item, FromComponent()]
