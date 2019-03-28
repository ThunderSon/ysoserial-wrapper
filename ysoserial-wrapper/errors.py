__all__ = ["JarNotFoundException", "EnvironmentKeyNotFoundException"]


class JarNotFoundException(Exception):
    """Raised when a jar is not accessible"""


class EnvironmentKeyNotFoundException(Exception):
    """Raised when the KEY environment variable is missing"""
