from pyrogram.types import Message, InlineKeyboardButton


def get_file_id(msg: Message):
    if not msg.media: return None
    for message_type in ("photo", "animation", "audio", "document", "video", "video_note", "voice", "sticker"):
        obj = getattr(msg, message_type)
        if obj:
            setattr(obj, "message_type", message_type)
            return obj
          
