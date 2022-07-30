from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can extract text from images using OCR technology.

By @Harmishhk
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/HK_bots")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/HK_bots")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/HK_bots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/HK_bots")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

Just send an image. Rest is on me.

Note : You can send any amount of images at once and it will work with same speed and accuracy.

More features in development. Keep track by joining @HK_bots.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @HK_bots

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Harmishhk
    """
