from typing import Dict, Type

from .home_page import HomePage
from .python_learning_page import PythonLearningPage
from .finance_module import FinanceModule
from ..page_utils import WebPage

PAGE_MAP: Dict[str, Type[WebPage]] = {
    "Home": HomePage,
    "Python Learning Module": PythonLearningPage
}

Finance_PAGE_MAP = {
    "finance Module": FinanceModule
}

__all__ = ["PAGE_MAP", "Finance_PAGE_MAP"]



