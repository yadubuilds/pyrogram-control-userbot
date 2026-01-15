import subprocess
from pyrogram import filters
from core.config import Config

def register_update(app):

    @app.on_message(filters.command("update") & filters.user(Config.OWNER_ID))
    async def update_bot(_, msg):
        status = await msg.reply("🔄 **Updating system...**")

        try:
            pull = subprocess.run(
                ["git", "pull"],
                capture_output=True,
                text=True
            )

            restart = subprocess.run(
                ["pm2", "restart", "all"],
                capture_output=True,
                text=True
            )

            output = (
                "📥 **Git Pull:**\n"
                f"```\n{pull.stdout.strip()}\n```\n\n"
                "♻️ **PM2 Restart:**\n"
                f"```\n{restart.stdout.strip()}\n```"
            )

            await sta
