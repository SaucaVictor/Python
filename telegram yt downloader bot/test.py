import os
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#bot token and username
token = '<api_example>'
bot_username = '@ytuploaderdestroyerbot'

#bot start command 
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Message format: <link> mp3/mp4')

#bot response
async def response(text1: str):
    if 'hello' in text1.lower():
        return 'hi there'
    elif 'youtu' in text1.lower():
        global title_path
        title_path = 0
        global title_path2
        title_path2 = 0
        text1 = text1.split(' ')
        [text := i for i in text1 if 'https' in i]
        clean=True
        if clean:
            folder_path = "downloads"
            files = os.listdir(folder_path)
            for file in files:
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)

        if '&list' in text:
            text=text.split('&list')
            text=text[0]
        if 'mp4' in text1:
            from pytube import YouTube
            video_url = text 
            output_directory = "./downloads"
            url=video_url
            output_path=output_directory
            try:
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                if stream:
                    print("Downloading:", yt.title)
                    stream.download(output_path)
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
                        title_path=freshest_file[:len(freshest_file)-4]
                else:
                    print("No MP4 stream available for this video.")
            except Exception as e:
                print("Error:", e)
        elif 'mp3' in text1:
            video_url = text
            output_directory = "./downloads/"
            url = video_url
            output_path = output_directory
            try:
                subprocess.run(["yt-dlp", "--cookies","--cookies-from-browser", "--extract-audio", "--audio-format", "mp3", "--output", output_path + "/%(title)s.%(ext)s", url], check=True)
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
                    title_path2=freshest_file[:len(freshest_file)-4]
            except Exception as e:
                print("Error:", e)
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
        global title_path
        global title_path2
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
