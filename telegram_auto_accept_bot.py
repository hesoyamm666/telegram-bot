import logging
from telegram import Update
from telegram.ext import Application, ContextTypes, ChatMemberHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def handle_chat_member_update(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_member_update = update.chat_member

    if chat_member_update.new_chat_member.status == "pending":
        user_id = chat_member_update.new_chat_member.user.id
        chat_id = chat_member_update.chat.id
        
        try:
            await context.bot.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
            logger.info(f"User {user_id} qabul qilindi")
        except Exception as e:
            logger.error(f"Xato: {e}")

def main():
    TOKEN = "8813088584:AAEPCbwbRz-_Kt8V_ZVrUzFJ1R5UEwjbOyw"
    
    application = Application.builder().token(TOKEN).build()

    application.add_handler(ChatMemberHandler(
        handle_chat_member_update,
        chat_member_types=ChatMemberHandler.CHAT_MEMBER
    ))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
