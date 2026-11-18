# Meeting Action Item Extractor

Extracts candidate decisions, action items, owners, and deadlines from meeting transcripts using transparent text rules.

## Usage
```bash
python src/extract_actions.py sample/meeting.txt --output outputs/actions.json
```

The output is reviewable and is intended to support meeting follow-up rather than silently assign work.
