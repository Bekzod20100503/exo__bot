from telebot import TeleBot
from telebot.types import Message


TOKEN = 'YOU TOKEN'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def reaction_start(message : Message):
    chat_id = message.chat.id
    first_tname = message.from_user.first_name
    bot.send_message(chat_id, f"salom, {first_tname}")


@bot.message_handler(regexp='Salom')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Salom qalesiz yaxshimiz BITTA ESLATMA Men bilan yozishyotganda imloviy hato qilmang')

@bot.message_handler(regexp='Ishla qale')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Ishla zo'r OLLOHGA shkur")

@bot.message_handler(regexp="Nega")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Shunga")

@bot.message_handler(regexp="Yolg'on gapirma")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men rost gapiraman ")

@bot.message_handler(regexp="yolgon gapirma")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men rost gapiraman")

@bot.message_handler(regexp="Aldayabsan")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "EEE ushol")

@bot.message_handler(regexp='Pashol')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "EEE usho'la 😂")

@bot.message_handler(regexp="Dnx")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "🖕")

@bot.message_handler(regexp="Dnh")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "🖕")

@bot.message_handler(regexp='Qanaqa mashinani ')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "BMW va MERS ni")

@bot.message_handler(regexp="Men ham BMW ni yaxshi ko'raman")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Fukusimiz bir xil akana")

@bot.message_handler(regexp="Men ham BMW ni yaxshi koraman")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Fukusimiz bir xil akana")

@bot.message_handler(regexp="Men xam BMW ni yaxshi ko'raman")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Fukusimiz bir xil akana")

@bot.message_handler(regexp="Men ham BMW ni yahshi ko'raman")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Fukusimiz bir xil akana")

@bot.message_handler(regexp="Men xam BMW ni yahshi ko'raman")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Fukusimiz bir xil akana")

@bot.message_handler(regexp='Arzimidi')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Ok boldi yozisheli")

@bot.message_handler(regexp='Bekzod kim u')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "U meni yaratgan odam 'sen qanday yaratilgansan' deb savol bering toliqroq aytaman")

@bot.message_handler(regexp='Mazalarin yaxshimi')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Ha raxmat siz yaxshimisiz")

@bot.message_handler(regexp='Mazalarin yahshimi')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Ha raxmat siz yaxshimisiz")

@bot.message_handler(regexp='Ha raxmat')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men bilan yozishasmi")

@bot.message_handler(regexp='Ha rahmat')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men bilan yozishasmi")

@bot.message_handler(regexp='Xa raxmat')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men bilan yozishasmi")

@bot.message_handler(regexp='Ha yaxshi')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men bilan yozishasmi")

@bot.message_handler(regexp='Ha yahshi')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men bilan yozishasmi")

@bot.message_handler(regexp='Xa yaxshi')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men bilan yozishasmi")

@bot.message_handler(regexp='Xa yahshi')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men bilan yozishasmi")

@bot.message_handler(regexp="Yo'q")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Nima yo'q Ha deb yozin iyaa")

@bot.message_handler(regexp="Yoq")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Nima yo'q Ha deb yozin iyaa")

@bot.message_handler(regexp="O'zing haqinda malimot ber")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Meni Bekzod Saidkarimov yaratgan men u odamni 1-chi botiman")

@bot.message_handler(regexp="O'zing xaqinda malimot ber")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Meni Bekzod Saidkarimov yaratgan men u odamni 1-chi botiman")

@bot.message_handler(regexp="Ozing haqinda malimot ber")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Meni Bekzod Saidkarimov yaratgan men u odamni 1-chi botiman")

@bot.message_handler(regexp="Ozing xaqinda malimot ber")
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Meni Bekzod Saidkarimov yaratgan men u odamni 1-chi botiman")

@bot.message_handler(regexp='Xa rahmat')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men bilan yozishasmi")

@bot.message_handler(regexp='Musiqa aytib ber')
def reaction_hello(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Men musiqa aytmayman lekn do'tim Tarona bot ga yossez musiqalar chiqarib beradi ")

@bot.message_handler(regexp='Rahmat')
def reaction_raxmat_2(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Arzimidi ☺️")






bot.polling()