import os
from telethon import TelegramClient, events

api_id = 123# your API ID
api_hash = '123'  # your API Hash

client = TelegramClient('session_name', api_id, api_hash)

def is_file_uploaded(file_name):
    with open('uploaded_files.txt', 'a+') as file:
        file.seek(0)
        if file_name in file.read():
            return True
        else:
            file.write(file_name + '\n')
            return False

async def main():
    await client.connect()

    if not await client.is_user_authorized():
        phone_number = input("Enter your phone number: ")
        await client.send_code_request(phone_number)
        await client.sign_in(
            input("Enter the code you received: "),
            phone=phone_number
        )

    channel_url = "https://t.me/123"
    channel = await client.get_entity(channel_url)

    channel_b_username = 'YOUR_CHANNEL_NAME'
    channel_b = await client.get_entity(channel_b_username)

    async for message in client.iter_messages(channel):
        if message.media and hasattr(message.media, 'document'):
            file_extension = message.file.ext
            file_name = f'{message.id}_{message.file.name}'

            if file_extension in ['.mp4', '.mkv', '.avi', '.zip', '.rar']:
                if is_file_uploaded(file_name):
                    continue

                max_attempts = 3
                for attempt in range(max_attempts):
                    try:
                        await message.download_media('downloads/' + file_name)
                        break
                    except Exception as e:
                        if attempt < max_attempts - 1:
                            print(f"Retry {attempt+1} of {max_attempts}: Error downloading {file_name}: {e}")
                        else:
                            print(f"Failed to download {file_name} after {max_attempts} attempts: {e}")
                            break

                caption_text = f"Here's a file from {channel.username}! \nFilename: {file_name}"
                if message.message:
                    caption_text += f"\nDescription: {message.message}"

                for attempt in range(max_attempts):
                    try:
                        await client.send_file(
                            channel_b,
                            'downloads/' + file_name,
                            caption=caption_text
                        )
                        break
                    except Exception as e:
                        if attempt < max_attempts - 1:
                            print(f"Retry {attempt+1} of {max_attempts}: Error uploading {file_name}: {e}")
                        else:
                            print(f"Failed to upload {file_name} after {max_attempts} attempts: {e}")
                            break

                os.remove(f"downloads/{file_name}")

    await client.disconnect()

with client.start():
    client.loop.run_until_complete(main())
