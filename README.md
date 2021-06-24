## WTAntispam

### Setup
Get `api_id` and `api_hash` via [My Telegram Apps](https://my.telegram.org/apps)

#### PowerShell
```powershell
python -m venv venv
venv/Scripts/Activate.ps1
pip install -r requirements.txt
```
#### Bash
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run
#### PowerShell
```powershell
venv/Scripts/Activate.ps1
$env:API_ID = 000000
$env:API_HASH = "ffffffffffffffffffffffffffffffff"
python __main__.py
```
#### Bash
```bash
source venv/bin/activate
export API_ID=000000
export API_HASH="ffffffffffffffffffffffffffffffff"
python __main__.py
```

## Extensions
### Printer
Prints pretty all dialogs and their ids and usernames. Also, can print dialogs under Reader extension.
It close an application after print.
#### Usage
Add one of follow environment variables for effect:

Name|Value|Description
---|---|---
SHOW_DIALOGS|1|All dialogs
CURRENT_DIALOGS|1|Dialogs that affected by Reader extension

### Reader
Automatically mark as read dialogs that ids in `reader.txt` file.

### Filter
Automatically remove messages (for all) from dialogs using filters.

`filter.json` structure:
```json
{
  "chat_id": ["filter_name", ...],
  ...
}
```
All filters placed in `filters` folder. Use `filter_name.txt` format for files. Words placed line by line:
```text
something
...
```