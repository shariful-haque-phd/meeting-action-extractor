# Architecture — Meeting Action Item Extractor

```mermaid
flowchart LR
    A["meeting.txt"] --> B["extract_actions.py"]
    B --> C["actions.json"]
```

## Inputs

- `sample/meeting.txt`

## Source files

- `src/extract_actions.py`

## Output

- `results/artifacts/actions.json`

This representation is intended for source navigation. It does not imply a production deployment or undisclosed components. The editable diagram is available as [`architecture.mmd`](architecture.mmd).
