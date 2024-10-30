import random, json, os, requests,brawlstats, re
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes, CallbackContext

botphase = 0
botsubphase = 0

buttons = [["My Statistics📊","My Club Statistics📊"],["Brawlers Wiki🔎"]]
cancelbutton = [["Back🔙"]]
howtogetclub = [["Enter Club Tag"], ["Get Club Info Via Player Tag"], ["Back🔙"]]




client = brawlstats.Client("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImY2ZjljNGMxLTQwMmYtNDdiZC1hOWRmLWU5NTYwZjlmMDAzMyIsImlhdCI6MTczMDI3NDM5Mywic3ViIjoiZGV2ZWxvcGVyLzJlNDc3NGVkLWFlNmMtOWU0Yy00N2YxLWU1NjA2NzI4ZmExOCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg1LjIxMy4yMzAuMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.cXkYsfORhQWcFjchOEjIWw_cTEeZDH1_g0GXcA3bVFHJEmYqsqq1FVmfa250P1bd699H_rbvTWpHcNkyRgjujg", is_async=True)
sections = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
cancel = ReplyKeyboardMarkup(cancelbutton, resize_keyboard=True)
getclubmethod = ReplyKeyboardMarkup(howtogetclub, resize_keyboard=True)




async def start(update: Update, context):
    global botphase
    botphase = 0
    await update.message.reply_text("Choose an option:", reply_markup=sections)
#phase 0 ----> idle
#phase 1 ----> stats
#phase 2 ----> club stats
#phase 3 ----> brawlers
async def process(update: Update, context):
    global botphase, cancel, buttons, getclubmethod, botsubphase
    msg = update.message.text
    chatid = update.effective_chat.id
    if botphase == 0:
        if msg == "My Statistics📊":
            await update.message.reply_text("Please Enter Your Player Tag", reply_markup=cancel)
            botphase = 1
        elif msg == "My Club Statistics📊":
            await update.message.reply_text("Choose One Of The Options Below", reply_markup=getclubmethod)
            botphase = 2
    elif botphase == 1:
        if msg == "Back🔙":
            await update.message.reply_text("Choose an option:", reply_markup=sections)
            botphase = 0
        else:
            try:
                try:
                    playerprofile = await client.get_profile(msg.upper())
                    name = playerprofile["name"]
                    trophies = playerprofile["trophies"]
                    triplevictories = playerprofile["3vs3Victories"]
                    douvictories = playerprofile["duoVictories"]
                    solovictories = playerprofile["soloVictories"]
                    icon = playerprofile["icon"].id
                    imagedirectory = f"profileicons/{icon}.png"
                    explevel = playerprofile["expLevel"]
                    clubname = playerprofile["club"].name
                    caption = (f"Name: {name}\n🏆Trophies: {trophies}\n⚽️3vs3 Victories: {triplevictories}\n👥Duo Victories: {douvictories}\n👤Solo Victories: {solovictories}\n⬆️Level: {explevel}\n🏟Club: {clubname}")
                    await context.bot.send_photo(chat_id=chatid, photo=open(imagedirectory, 'rb'), caption=caption)
                except:
                    playerprofile = await client.get_profile(msg.upper())
                    name = playerprofile["name"]
                    trophies = playerprofile["trophies"]
                    triplevictories = playerprofile["3vs3Victories"]
                    douvictories = playerprofile["duoVictories"]
                    solovictories = playerprofile["soloVictories"]
                    icon = playerprofile["icon"].id
                    imagedirectory = f"profileicons/{icon}.png"
                    explevel = playerprofile["expLevel"]
                    clubname = playerprofile["club"].name
                    caption = (f"Name: {name}\n🏆Trophies: {trophies}\n⚽️3vs3 Victories: {triplevictories}\n👥Duo Victories: {douvictories}\n👤Solo Victories: {solovictories}\n⬆️Level: {explevel}\n🏟Club: {clubname}")
                    await update.message.reply_text("Profile Picture Is Not Avialable:(")
                    await update.message.reply_text(caption, disable_web_page_preview=True)
            except:
                await update.message.reply_text("Please Enter Valid Player Tag")
    elif botphase == 2:
        if botsubphase == 0:
            if msg == "Enter Club Tag":
                await update.message.reply_text("Please Enter Your Club Tag", reply_markup=cancel)
                botsubphase = 1
            elif msg == "Get Club Info Via Player Tag":
                await update.message.reply_text("Please Enter Your Player Tag", reply_markup=cancel)
                botsubphase = 2
            if msg == "Back🔙":
                await update.message.reply_text("Choose an option:", reply_markup=sections)
                botphase = 0
        elif botsubphase == 1:
            club = await client.get_club(msg.upper())
            iteration = 1
            clubname = club["name"]
            clubtrophies = club["trophies"]
            club_description = club["description"]
            clubrequiredtrophies = club["requiredTrophies"]
            clubmembers = f"Club Members:"
            for member in club.members:
                clubmembers = clubmembers + f"\n{iteration}. {member.name} | {member.tag} | {member.role.upper()}"
                iteration += 1
            await update.message.reply_text(f"Club Name: {clubname}\nDescription: {club_description}\nClub Trophies: {clubtrophies}\nRequired Trophies To Join: {clubrequiredtrophies}\n Club Members List: {clubmembers}", disable_web_page_preview=True)



if __name__ == '__main__':
    app = ApplicationBuilder().token("7818134232:AAFM6ufKSfDHwa7Jp08fAkphRZqNLC01fv8").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, process))
    app.run_polling(poll_interval=1)