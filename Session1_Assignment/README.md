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

```
Reflections

What failed first, and how did I diagnose it?

1. The first failure was only the date field appearing in the JSON output — all other fields were missing.

Diagnosis: I added a print statement inside the parse_notes loop and noticed it only printed once (Key: date, Value: 2026-08-24) before exiting. That revealed the return notes statement was indented inside the for loop, causing the function to exit after processing just the first line. Moving return outside the loop fixed it.

2. **Actions not splitting correctly**

The Actions line contains pipe-delimited fields separated by semicolons (John|Add structured logs|2026-08-26; Azhar|Draft dashboard|2026-08-28). I needed to split on ";" first to get each action, then split each on "|" to extract owner, task, and due_date. Neither split was in place initially.

Reads `data/meeting_notes.txt` → writes `output/notes.json`.
