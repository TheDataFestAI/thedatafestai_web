from typing import Dict, Type

from .home_page import HomePage
from ..page_utils import WebPage

PAGE_MAP: Dict[str, Type[WebPage]] = {
    "Home Page": HomePage
}

__all__ = ["PAGE_MAP"]



