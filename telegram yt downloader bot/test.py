import os
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# bot token and username
token = 'api_token'
bot_username = '@ytuploaderdestroyerbot'

# bot start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Message format: <link> mp3/mp4')

# bot response
async def response(text1: str):
    global title_path, title_path2
    title_path = ""
    title_path2 = ""

    if 'hello' in text1.lower():
        return 'hi there'
    elif 'youtu' in text1.lower():
        text1 = text1.split(' ')
        text = next((i for i in text1 if 'https' in i), None)

        clean = True
        if clean:
            folder_path = "downloads"
            files = os.listdir(folder_path)
            for file in files:
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)

        if text and '&list' in text:
            text = text.split('&list')[0]

        if 'mp4' in text1:
            video_url = text
            output_directory = "./downloads/"
            url = video_url
            output_path = output_directory
            try:
                result = subprocess.run([
                    "yt-dlp",
                    "--format", "mp4",
                    "--output", os.path.join(output_path, "%(title)s.%(ext)s"),
                    url
                ], capture_output=True, text=True)
                
                if result.returncode != 0:
                    print("Error:", result.stderr)
                    return 'error X('
                
                print("Download complete!")
                folder_path = "downloads"

                def get_freshest_file(folder_path):
                    files = os.listdir(folder_path)
                    files = [os.path.join(folder_path, file) for file in files if os.path.isfile(os.path.join(folder_path, file))]
                    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
                    if files:
                        return os.path.basename(files[0]) 
                    else:
                        return None 
                freshest_file = get_freshest_file(folder_path)
                if freshest_file:
                    title_path = freshest_file[:len(freshest_file)-4]
            except Exception as e:
                print("Error:", e)
                return 'error X('
        elif 'mp3' in text1:
            video_url = text
            output_directory = "./downloads/"
            url = video_url
            output_path = output_directory
            try:
                result = subprocess.run([
                    "yt-dlp",
                    "--extract-audio",
                    "--audio-format", "mp3",
                    "--output", os.path.join(output_path, "%(title)s.%(ext)s"),
                    url
                ], capture_output=True, text=True)
                
                if result.returncode != 0:
                    print("Error:", result.stderr)
                    return 'error X('
                
                print("Download complete!")
                folder_path = "downloads"

                def get_freshest_file(folder_path):
                    files = os.listdir(folder_path)
                    files = [os.path.join(folder_path, file) for file in files if os.path.isfile(os.path.join(folder_path, file))]
                    files.sort(key=lambda x: os.stat(x).st_ctime, reverse=True)
                    if files:
                        return os.path.basename(files[0]) 
                    else:
                        return None 
                freshest_file = get_freshest_file(folder_path)
                if freshest_file:
                    title_path2 = freshest_file[:len(freshest_file)-4]
            except Exception as e:
                print("Error:", e)
                return 'error X('
        else:
            return 'send valid message format'
        if title_path or title_path2:
            return 'complete'
        else:
            return 'error X('
    elif 'upload' in text1.lower():
        pass
    else:
        return 'idk'

async def resp_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mess = update.message.chat.type
    text = update.message.text

    print(f'User ({update.message.chat.id}  ->  {mess})  typed : {text}')

    if mess == 'group':
        return
    else:
        response_ = await response(text)
    print('Bot: ', response_)
    await update.message.reply_text(response_)

    if response_ == 'complete':
        chat_id = update.message.chat.id
        document_path = "./downloads/"
        global title_path, title_path2
        if title_path:
            document_filename = f"{title_path}.mp4"
            await context.bot.send_document(chat_id=chat_id, document=open(document_path + document_filename, 'rb'))
        if title_path2:
            document_filename = f"{title_path2}.mp3"
            await context.bot.send_document(chat_id=chat_id, document=open(document_path + document_filename, 'rb'))

if __name__ == '__main__':
    print('starting')
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, resp_back))
    print('polling')
    app.run_polling(poll_interval=3)
