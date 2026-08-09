from __future__ import annotations

import logging
from typing import Any


def configure_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=level.upper(),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def log_context(event: str, **fields: Any) -> dict[str, Any]:
    return {"event": event, **fields}
