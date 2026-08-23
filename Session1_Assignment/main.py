import json
from logging import exception
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[0]
INPUT_PATH = PROJECT_ROOT / "data" / "meeting_notes.txt"
OUTPUT_PATH = PROJECT_ROOT / "output" / "notes.json"

def read_notes(text: str) -> str:
    text = INPUT_PATH.read_text(encoding="utf-8")
    return text

def parse_notes(text:str) -> dict:
    notes = {
        "date": "",
        "attendees": [],
        "title":"",
        "owner": "",
        "decisions": [],
        "actions": []
    }
    #print(f"Inside the parse_notes function: {text}")
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            print(f"Skipping line: {line}")
            continue
            
        key, value = line.split(":", maxsplit=1)

        key = key.strip().lower()
        value = value.strip()
        

        #print("Key: ", key, "Value: ", value)

        if key == "attendees":
            notes["attendees"] = [tag.strip() for tag in value.split(",") if tag.strip()]
        if key == "decisions":
            notes["decisions"] = [tag.strip() for tag in value.split(",") if tag.strip()]
        if key == "actions":
            for item in value.split(";"):
                parts = [part.strip() for part in item.split("|")]
                if len(parts) == 3:
                    action = {
                        "owner": parts[0],
                        "task": parts[1],
                        "due_date": parts[2]
                    }
                    notes["actions"].append(action)

        elif key in {"date", "title", "owner"}:
            notes[key] = value

    missing = [field for field in ("date", "title", "owner") if not notes[field]]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")

    return notes   
    #print("Notes dictionary: ", notes)

def save_notes(notes: dict) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(notes, indent=2), encoding="utf-8")       

def main() -> int:
    try:
        #print(f"Inside the main function")
        #print(f"Project root: {PROJECT_ROOT}")
        #print(f"Input path: {INPUT_PATH}")
        #print(f"Output path: {OUTPUT_PATH}")

        readNotes = read_notes(INPUT_PATH)
        #meetingNotes = print(f"{readNotes}")
        meetingNotes = readNotes

        parseNotes = parse_notes(meetingNotes)
        print(f"Parsed notes: {parseNotes}")

        saveNotes = save_notes(parseNotes)



    except FileNotFoundError as error:
        print(f"File not found error: {error}")
        return 1
    except ValueError as error:                          
        print(f"Validation error: {error}")
        return 1
    except Exception as error:
        print(f"Error in the main function: {error}")
        return 1
    
    print(f"Completed the main function successfully")
    return 0    

if __name__ == "__main__":
    raise SystemExit(main())