class PropertyUtilityError(Exception):
    """Base exception for Property Utility errors."""


class DatabaseUnavailableError(PropertyUtilityError):
    """Raised when the application cannot reach the configured database."""
