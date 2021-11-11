"""Highlight action implementation."""

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer


def highlight_code(code: str) -> str:
    """Highlight code.

    Args:
        code: code to highlight

    Returns:
        highlighted code
    """
    return highlight(code, PythonLexer(), TerminalFormatter())
