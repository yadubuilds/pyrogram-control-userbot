import subprocess
from pyrogram import filters
from core.config import Config

def register_update(app):

    @app.on_message(filters.command("update") & filters.user(Config.OWNER_ID))
    async def update_bot(_, msg):
        status = await msg.reply("🔄 **Updating bot...**")

        try:
            pull = subprocess.check_output(
                ["git", "pull"],
                stderr=subprocess.STDOUT
            ).decode()

            restart = subprocess.check_output(
                ["pm2", "restart", "all"],
                stderr=subprocess.STDOUT
            ).decode()

            await status.edit(
                "✅ **Update Successful**\n\n"
                "📥 Git Output:\n"
                f"```{pull[-3000:]}```\n"
                "♻️ PM2 Restarted"
            )

        except subprocess.CalledProcessError as e:
            await status.edit(
                "❌ **Update Failed**\n\n"
                f"```{e.output.decode()}```"
            )
