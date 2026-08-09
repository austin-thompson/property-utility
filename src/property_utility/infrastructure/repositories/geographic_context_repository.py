from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


class InMemoryGeographicContextRepository:
    def __init__(self) -> None:
        self._records: list[dict[str, object]] = []

    def save(self, record: dict[str, object]) -> None:
        self._records.append(record)

    def list(self) -> list[dict[str, object]]:
        return list(self._records)

    def get_by_address(self, address: str) -> dict[str, object] | None:
        for record in self._records:
            if record.get("address") == address:
                return record
        return None

    def clear(self) -> None:
        self._records.clear()


class SqliteGeographicContextRepository:
    def __init__(self, db_path: Path | str) -> None:
        self._db_path = Path(db_path)
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._connection = sqlite3.connect(str(self._db_path), check_same_thread=False)
        self._initialize_database()

    def _initialize_database(self) -> None:
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS geographic_context_records (
                address TEXT PRIMARY KEY,
                normalized_address TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                country TEXT NOT NULL,
                confidence REAL NOT NULL,
                source TEXT NOT NULL
            )
            """
        )
        self._connection.commit()

    def save(self, record: dict[str, Any]) -> None:
        self._connection.execute(
            """
            INSERT OR REPLACE INTO geographic_context_records (
                address,
                normalized_address,
                city,
                state,
                country,
                confidence,
                source
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record["address"],
                record["normalized_address"],
                record["city"],
                record["state"],
                record["country"],
                record["confidence"],
                record["source"],
            ),
        )
        self._connection.commit()

    def list(self) -> list[dict[str, Any]]:
        cursor = self._connection.execute(
            "SELECT address, normalized_address, city, state, country, "
            "confidence, source FROM geographic_context_records"
        )
        return [
            {
                "address": row[0],
                "normalized_address": row[1],
                "city": row[2],
                "state": row[3],
                "country": row[4],
                "confidence": row[5],
                "source": row[6],
            }
            for row in cursor.fetchall()
        ]

    def get_by_address(self, address: str) -> dict[str, Any] | None:
        cursor = self._connection.execute(
            "SELECT address, normalized_address, city, state, country, "
            "confidence, source FROM geographic_context_records WHERE address = ?",
            (address,),
        )
        row = cursor.fetchone()
        if row is None:
            return None
        return {
            "address": row[0],
            "normalized_address": row[1],
            "city": row[2],
            "state": row[3],
            "country": row[4],
            "confidence": row[5],
            "source": row[6],
        }

    def clear(self) -> None:
        self._connection.execute("DELETE FROM geographic_context_records")
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()
