class Translation(object):
    START_TEXT = """ **Hi,** **Welcome** **To** **@Free_Bot_Pro_bot**   
**I** **am** **a** **Simple** **all** **in** **one** **bot**
**My** **Credits** **to** **:** **@RisingIndianOtaku** """
 
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " **Please don't be selfish.** "
    UPGRADE_TEXT = "Contact @RisingIndianOtaku"
    
    FORMAT_SELECTION = " **Got** **the** **file**.** \n now sent me a image if you want to set as custom thumbnail \n and then click the needed format from the below buttons."
    SET_CUSTOM_USERNAME_PASSWORD = """ **If you want to download premium videos, provide in the following format**:
URL | filename | username | password"""
    NOYES_URL = "@GetPublicLinkBot URL detected. Please do not abuse the service!"
    DOWNLOAD_START = " **Trying** **to** **Download..📥** "
    UPLOAD_START = "**Trying** **to** **Upload..📤**"
    RCHD_BOT_API_LIMIT = "**size** **greater** **than** **maximum** **allowed** **size** (50MB). **Neverthless**, **trying** **to** upload.**"
    RCHD_TG_API_LIMIT = " **Downloaded** **in** {} **seconds.** \nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank** **you** **For** **using** **Me** **!!**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. And \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "**Please** **Contact** **to** **@RisingIndianOtaku**"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/RisingIndianOtaku'>@RisingIndianOtaku</a>"
    SAVED_CUSTOM_THUMB_NAIL = "**Custom** **video** **/** **file** **thumbnail** **saved**. **This** **image** **will** **be** **used** **in** **the** **video** **/** **file**."
    DEL_ETED_CUSTOM_THUMB_NAIL = " ✅ **Custom** **thumbnail** **cleared** **succesfully.** "
    DEL_ETED_CUSTOM_THUMB_NAIL = " ✅ **Custom** **thumbnail** **cleared** **succesfully.** "
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = " ✅ **Media** **cleared** **succesfully.** "
    SAVED_RECVD_DOC_FILE = " **✅ **Document **Downloaded** **Successfully.** "
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom Thumbnail found."
    NO_VOID_FORMAT_FOUND = "something is wrong with the URL you gave me 🤦‍♀️. If you think this could be a bug please report this on https://github.com/ShinchanNohara1/UpgradedAnydlbot issues."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
-----------
Telegram ID: <code>{}</code>
Plan name: <a href='https://t.me/SpEcHlDe/599'>{}</a>
Expires on: {}"""

    HELP_USER = """  There are multiple things I can do:

/start - To check bot is working.
/help - To get this message. 
/upfiles - to get direct link of tg files.
/rename - reply to document / video to rename tg it.
/sthumb - reply to your image to use custom thumbnail. 
/dthumb - reset thumbnail to default
/c2v - reply to video in document form convert to video format 
/dm - download media to my storage to use ffmpegm.
/cffmpegm - clear ffmpeg media.
/storageinfo - to get my local storage info. 
/trim - trim Video | Example - /trim 00:00:01 00:01:00.

Free Users Can Only Use Upload, If you want to use otther commands pls contact @risingindianotaku.

How To Upload ?
🔘 ᴅᴏ ʏᴏᴜ ɴᴇᴇᴅ ᴀ ᴄᴜꜱᴛᴏᴍ ꜰɪʟᴇɴᴀᴍᴇ ꜰᴏʟʟᴏᴡ ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ ᴇxᴀᴍᴘʟᴇ👇
http://www.example.com|example.apk
🔘 ʏᴏᴜ ɴᴇᴇᴅ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ ᴊᴜꜱᴛ ꜱᴇɴᴛ ᴍᴇ ᴀɴ ɪᴍᴀɢᴇ.
🔘 ʏᴏᴜʀ ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴘᴇᴇᴅ ᴡɪʟʟ ᴅᴇᴘᴇɴᴅ ᴏɴ ʏᴏᴜʀ ʟɪɴᴋ ꜱᴘᴇᴇᴅ.
🔘 ʏᴏᴜᴛᴜʙᴇ_ᴅʟ ꜱᴜᴘᴘᴏʀᴛᴇᴅ.

Send /me to know current plan details""" 
  
    REPLY_TO_DOC_GET_LINK = "**Reply** **to** **a** **Telegram** **media** **to** **get**  **Direct** **Download** Link**"
    REPLY_TO_DOC_FOR_C2V = "**Reply** **to** **a** **Telegram** **media** **to** **convert**"
    REPLY_TO_DOC_FOR_RENAME_FILE = "**Reply** **to** **a** **Telegram** **media** **to** **/rename** **with** **custom** **thumbnail**"
    AFTER_GET_DL_LINK = "<b>Direct Link generated</b> 👇\n \n{} \n \n<i>Generated link will expire in {} days.</i> ."
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a HTTP link, to extract embedded subtitle"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ShrimadhaVahdamirhS'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """**Select** **file_name** **to** **upload** **from** **the** **below** **options.**
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "**Process** **Cancelled**"
    ZIP_UPLOADED_STR = "**Uploaded** {} **files** **in** {} **seconds**"
    FREE_USER_LIMIT_Q_SZE = """**Cannot** **Process.**
Free users only 1 request per hour.
/upgrade or Try 3600 seconds later."""
    G_DRIVE_GIVE_URL_TO_LOGIN = "Please login using {}. Send `/gsetup <YOUR CODE>`"
    G_DRIVE_SETUP_IN_VALID_FORMAT = "Send `/gsetup <YOUR CODE>`"
    G_DRIVE_SETUP_COMPLETE = "Logged In."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users. "
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.
<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@ReNameBot</code>
Please short your file name and try again!"""
    YTDL_ERROR_MESSAGE = (
        "please report this issue on https://yt-dl.org/bug . "
        "Make sure you are using the latest version; see "
        " https://yt-dl.org/update  on how to update. "
        "Be sure to call youtube-dl with the --verbose flag "
        "and include its complete output."
    )
    ISOAYD_PREMIUM_VIDEOS = "video is only available for registered users"
