import os
import math
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Mualliflik huquqlari
# Dasturchi: @DragonOwner

expressions = {}
user_count = 0

def create_keyboard():
    keyboard = [
        [InlineKeyboardButton("  7  ", callback_data='7'), InlineKeyboardButton("  8  ", callback_data='8'), InlineKeyboardButton("  9  ", callback_data='9'), InlineKeyboardButton("  /  ", callback_data='/')],
        [InlineKeyboardButton("  4  ", callback_data='4'), InlineKeyboardButton("  5  ", callback_data='5'), InlineKeyboardButton("  6  ", callback_data='6'), InlineKeyboardButton("  *  ", callback_data='*')],
        [InlineKeyboardButton("  1  ", callback_data='1'), InlineKeyboardButton("  2  ", callback_data='2'), InlineKeyboardButton("  3  ", callback_data='3'), InlineKeyboardButton("  -  ", callback_data='-')],
        [InlineKeyboardButton("  0  ", callback_data='0'), InlineKeyboardButton("  (  ", callback_data='('), InlineKeyboardButton("  )  ", callback_data=')'), InlineKeyboardButton("  +  ", callback_data='+')],
        [InlineKeyboardButton("  ⬅  ", callback_data='backspace'), InlineKeyboardButton("  C  ", callback_data='C'), InlineKeyboardButton("  √  ", callback_data='sqrt'), InlineKeyboardButton("  ^  ", callback_data='^')],
        [InlineKeyboardButton("  =  ", callback_data='=')],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context):
    global user_count
    user_count += 1
    user_id = update.message.from_user.id
    expressions[user_id] = ""

    await update.message.reply_text(
        f"👋 Assalomu alaykum {update.message.from_user.first_name}!\nMen murakkab matematik amallarni yecha oladigan kalkulyator botman.🤖",
        reply_markup=create_keyboard()
    )

async def button(update: Update, context):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if user_id not in expressions:
        expressions[user_id] = ""

    data = query.data

    if data == 'C':
        expressions[user_id] = ""
        await query.edit_message_text("Tozalandi✅", reply_markup=create_keyboard())
    elif data == '=':
        try:
            expression = expressions[user_id]
            if '√' in expression:
                expression = expression.replace('√', 'math.sqrt(') + ')'
            expression = expression.replace("^", "**")
            result = eval(expression)
            result = round(result, 2)
            await query.edit_message_text(f"Natija: {result}", reply_markup=create_keyboard())
            expressions[user_id] = ""
        except Exception as e:
            await query.edit_message_text(f"Xatolik: {e}", reply_markup=create_keyboard())
    elif data == 'sqrt':
        expressions[user_id] += "√"
        await query.edit_message_text(f"Joriy ifoda: {expressions[user_id]}", reply_markup=create_keyboard())
    elif data == 'backspace':
        expressions[user_id] = expressions[user_id][:-1]
        await query.edit_message_text(f"Joriy ifoda: {expressions[user_id]}", reply_markup=create_keyboard())
    elif data == 'statistics':
        await show_statistics(query)
    else:
        expressions[user_id] += data
        await query.edit_message_text(f"Joriy ifoda: {expressions[user_id]}", reply_markup=create_keyboard())

async def about(update: Update, context):
    await update.message.reply_text(
        "📜 Bu kalkulyator bot matematik amallarni yecha oladi.\n"
        "Dasturchi: @DragonOwner", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dasturchi", url="https://t.me/DragonOwner")]])
    )

async def admin_panel(update: Update, context):
    if str(update.message.from_user.id) == "YOUR_ADMIN_ID":  # O'zingizning admin ID ni kiriting
        await update.message.reply_text("Iltimos, admin parolini kiriting:")

async def check_password(update: Update, context):
    if update.message.text == "YOUR_ADMIN_PASSWORD":  # O'zingizning admin parolingizni kiriting
        context.user_data['is_admin'] = True
        await show_admin_panel(update)
    else:
        await update.message.reply_text("Xato parol! Qayta urinib ko'ring.")

async def show_admin_panel(update: Update):
    keyboard = [
        [InlineKeyboardButton("📤 Xabar va Rasm yuborish", callback_data='send_media')],
    ]
    await update.message.reply_text("Admin paneliga xush kelibsiz!", reply_markup=InlineKeyboardMarkup(keyboard))

async def send_media(update: Update, context):
    await update.callback_query.answer()
    context.user_data['send_media'] = True
    await update.callback_query.edit_message_text("Foydalanuvchilarga yuboriladigan rasm va matnni yuboring (matn bilan birga rasm jo'nating):")

async def handle_admin_messages(update: Update, context):
    if context.user_data.get('send_media') and update.message.photo:
        photo = update.message.photo[-1].file_id
        caption = update.message.caption or ""

        for user in expressions.keys():
            await context.bot.send_photo(chat_id=user, photo=photo, caption=caption)

        context.user_data['send_media'] = False
        await update.message.reply_text("Rasm va matn yuborildi!")

if __name__ == '__main__':
    app = ApplicationBuilder().build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_password))
    app.add_handler(CallbackQueryHandler(button, pattern='button'))
    app.add_handler(CallbackQueryHandler(send_media, pattern='send_media'))
    app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, handle_admin_messages))

    app.run_polling()
