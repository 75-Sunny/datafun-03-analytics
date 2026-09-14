"""src/datafun/appmiller.py - Project script.

Author: Denise Case

Date: 2026-08-23

This project reads the Romeo and Juliet text file,
counts occurrences of the words Romeo and Juliet,
verifies the results, and writes the counts
to a processed text file.

HOW TO RUN THIS FILE:

From the VS Code terminal in the project root folder:

uv run python -m datafun.appmiller
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path


# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P03", level="DEBUG")


# === LOCATE THE DATA FOLDERS ===

RAW_DIR: Final[Path] = Path("data") / "raw"
PROCESSED_DIR: Final[Path] = Path("data") / "processed"


# === TEXT FILE SETTINGS ===

TXT_INPUT: Final[Path] = RAW_DIR / "romeo_and_juliet.txt"

TXT_OUTPUT: Final[Path] = (
    PROCESSED_DIR / "txt_romeo_juliet_word_counts.txt"
)

ROMEO_WORD: Final[str] = "Romeo"
JULIET_WORD: Final[str] = "Juliet"


# === MAIN FUNCTION ===

def main() -> None:
    """Read Romeo and Juliet and count Romeo and Juliet occurrences.

    Extract: Read the text file.
    Transform: Count occurrences of Romeo and Juliet.
    Verify: Confirm the counts are non-negative.
    Load: Write the results to a processed text file.

    Arguments: None.
    Returns: None.
    """

    log_header(LOG, "P03")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    log_path(LOG, "raw folder", path=RAW_DIR)
    log_path(LOG, "processed folder", path=PROCESSED_DIR)

    # Ensure the output folder exists.
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # === EXTRACT ===

    LOG.info("===================================")
    LOG.info("TEXT PIPELINE - EXTRACT")
    LOG.info("===================================")

    LOG.info(f"Reading file: {TXT_INPUT}")

    text = TXT_INPUT.read_text(encoding="utf-8")

    LOG.info("Text file successfully read.")


    # === TRANSFORM ===

    LOG.info("===================================")
    LOG.info("TEXT PIPELINE - TRANSFORM")
    LOG.info("===================================")

    romeo_count = text.lower().split().count(ROMEO_WORD.lower())
    juliet_count = text.lower().split().count(JULIET_WORD.lower())

    LOG.info(f"{ROMEO_WORD} count: {romeo_count}")
    LOG.info(f"{JULIET_WORD} count: {juliet_count}")


    # === VERIFY ===

    LOG.info("===================================")
    LOG.info("TEXT PIPELINE - VERIFY")
    LOG.info("===================================")

    if romeo_count >= 0 and juliet_count >= 0:
        LOG.info("Verification successful.")
    else:
        raise ValueError("Word counts cannot be negative.")


    # === LOAD ===

    LOG.info("===================================")
    LOG.info("TEXT PIPELINE - LOAD")
    LOG.info("===================================")

    results = (
        "Romeo and Juliet Word Counts\n"
        "============================\n"
        f"Romeo: {romeo_count}\n"
        f"Juliet: {juliet_count}\n"
    )

    TXT_OUTPUT.write_text(results, encoding="utf-8")

    LOG.info(f"Results written to: {TXT_OUTPUT}")

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
