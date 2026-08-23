# Session 1 - Assignment — Text to JSON

From this folder, with the virtual environment active:

Text file format:
Date: 2026-08-24
Title: Checkout Reliability Review
Owner: Prasanna Venkatesh
Attendees: Prasanna, John, Azhar
Decisions: Add retry logging; create a payment failure dashboard
Actions: John|Add structured logs|2026-08-26; Azhar|Draft dashboard|2026-08-28

Run
```bash
python main.py

Reads `data/meeting_notes.txt` → writes `output/notes.json`.
