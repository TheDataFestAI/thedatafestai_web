from typing import Dict, Type

from .home_page import HomePage
from .python_learning_page import PythonLearningPage
from ..page_utils import WebPage

PAGE_MAP: Dict[str, Type[WebPage]] = {
    "Home": HomePage,
    "Python Module": PythonLearningPage
}

__all__ = ["PAGE_MAP"]



