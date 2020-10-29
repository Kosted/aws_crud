import os
from ast import literal_eval
from typing import Any, Optional

from dotenv import load_dotenv

load_dotenv()


class empty:
    """
    This class is used to represent no data being provided for a given input
    or output value.

    It is required because `None` may be a valid input or output value.
    """
    pass


def get_safe_env(variable_name: str, is_required: bool = True, default: Any = empty, need_eval: bool = False) -> Any:
    value: Optional[str] = os.getenv(variable_name, None)
    if default is empty and is_required and value is None:
        raise ValueError(f"{variable_name} is required. Check your .env file.")
    if value is None and default is not empty:
        return default
    if need_eval:
        value = literal_eval(value)  # type: ignore
    return value
