
### Telegram File Transfer Bot

This script uses the Telethon library to automate the transfer of files from one Telegram channel to another. It filters specific file types, downloads them, and uploads them to another channel.

#### Requirements
- Python 3.x
- Telethon package

#### Installation
Install Telethon using pip:
```bash
pip install telethon
```

#### Usage
1. **Setup API Keys:** First, obtain your `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org).
2. **Configure Script:** Open the script and replace `api_id` and `api_hash` with your actual API credentials. Set `channel_url` to the source channel's URL and `channel_b_username` to the target channel's username.
3. **Run Script:** Execute the script. On the first run, you'll need to authenticate with your phone number.

#### Code Explanation

- **Initialization:**
  ```python
  import os
  from telethon import TelegramClient, events

  api_id = 123  # Replace with your API ID
  api_hash = '123'  # Replace with your API Hash
  client = TelegramClient('session_name', api_id, api_hash)
  ```

- **Function to Check if a File is Uploaded:**
  ```python
  def is_file_uploaded(file_name):
      ...
  ```

- **Main Function:**
  - Connect to Telegram.
  - Authenticate if not already authorized.
  - Set up source (`channel_url`) and target (`channel_b_username`) channels.
  - Iterate through messages in the source channel, downloading and re-uploading specified file types.

- **File Download and Upload:**
  - Check file extensions.
  - Download files to `downloads/` folder.
  - Retry mechanism for both downloading and uploading.
  - Delete the file locally after uploading.

- **Running the Client:**
  ```python
  with client.start():
      client.loop.run_until_complete(main())
  ```

#### Note
- This script requires a persistent internet connection.
- Ensure sufficient local storage for temporary file downloads.
- Be aware of Telegram's rate limits to avoid being temporarily banned.

#### License 📜
This project is licensed under the GNU General Public License, version 3 (GPL-3.0). See the [LICENSE](LICENSE) file for details.

#### Author ✍️
This script was developed by SecWithMoh.


