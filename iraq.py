import telebot,requests,sqlite3,glob
from telebot import types
def en(num):
 num = str(num)
 return num.replace('1','q').replace('2','w').replace('3','e').replace('4','r').replace('5','t').replace('6','y').replace('7','u').replace('8','i').replace('9','o').replace('0','p')
def de(num):
 return num.replace('q','1').replace('w','2').replace('e','3').replace('r','4').replace('t','5').replace('y','6').replace('u','7').replace('i','8').replace('o','9').replace('p','0')
id = '5108562302'
open(f'H/H{id}.txt','w').write('oooo')
token = '7020448295:AAHjo6Qf5hDiEi1OcMp1d7TUBlNIaaakBJU'
bot = telebot.TeleBot (token)
def ch(user_id):
   b=0
   f = open("ch.txt", "r")
   for huks in f:
    x = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{huks}&user_id={user_id}")
    
    if any(["member" in x.text, "administrator" in x.text, "creator" in x.text]):
        pass
    else:
     return huks
def search_card(fam_nos, place):
  conn = sqlite3.connect(f"{place}(skidrow).sqlite")
  cursor = conn.cursor()

  print(fam_nos)
  card = f"'{fam_nos}'" if str(fam_nos)[0] ==("0") else f"{fam_nos}"

  hh=(f"SELECT * FROM PERSON WHERE FAM_NO = {card}")
  cursor.execute(hh)
  rows = cursor.fetchall()
  print(hh)
  column_names = [column[0] for column in cursor.description]
  data = []
  for row in rows:
        
        data_row = {}
        data.append(row)
  cursor.close()
  conn.close()

  return data
def search_person(first_name, father_name, grand_name, birth, place):
    conn = sqlite3.connect(f"{place}(skidrow).sqlite")
    cursor = conn.cursor()
    sql_command = f"SELECT * FROM PERSON WHERE P_FIRST LIKE '{first_name}%' AND P_FATHER LIKE '{father_name}%' AND P_GRAND LIKE '{grand_name}%' AND P_BIRTH LIKE '{birth}%'"
    print(sql_command)
    cursor.execute(sql_command)
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data_row = {} 
        data.append(row)
    cursor.close()
    conn.close()
    return data
@bot.message_handler(commands = ['start'])
def phone(message):
 kl = ch(message.from_user.id)
 if kl == None:
  if glob.glob(f'H/H{message.from_user.id}.txt'):
   u = open('pay.txt').read()
   key = types.InlineKeyboardMarkup()
   key.row_width = 3
   hUkS = de(open(f'H/H{message.from_user.id}.txt').read())
   a1 = types.InlineKeyboardButton(text="- أربيل🏔️.",callback_data='erbil;')
   a2 = types.InlineKeyboardButton(text="- الانبار🧨.",callback_data="al-anbar;")
   a3 = types.InlineKeyboardButton(text="- النجف🕌.",callback_data="najaf;")
   a4= types.InlineKeyboardButton(text="- بابل🏳️‍🌈 .",callback_data="babylon;")
   a5 = types.InlineKeyboardButton(text="- البصرة🌅.",callback_data="basra;")
   a6 = types.InlineKeyboardButton(text="- دهوك🌄 .",callback_data="duhok;")
   a7 = types.InlineKeyboardButton(text="- ديالى🍊.",callback_data='diyala;')
   a8 = types.InlineKeyboardButton(text="- ذي قار🍋.",callback_data='dhiqar;')
   a9 = types.InlineKeyboardButton(text="- سليمانية🍻.",callback_data='sulaymaniyah;')
   a10 = types.InlineKeyboardButton(text="- صلاح الدين🛕.",callback_data='salah-aldeen;')
   a11 = types.InlineKeyboardButton(text="- القادسية🗿.",callback_data="qadisiya;")
   a12 = types.InlineKeyboardButton(text="- كربلاء🕌.",callback_data="karbalaa;")
   a13 = types.InlineKeyboardButton(text="- كركوك☄️.",callback_data="kirkuk;")
   a14 = types.InlineKeyboardButton(text="- المثنى🏞️.",callback_data="muthana;")
   a15 = types.InlineKeyboardButton(text="- ميسان⚡.",callback_data="mesan;")
   a16 = types.InlineKeyboardButton(text="- نينوى🧨.",callback_data="nineveh;")
   a17 = types.InlineKeyboardButton(text="- واسط🫥.",callback_data="wasit;")
   a18 = types.InlineKeyboardButton(text="- بغداد🌆.",callback_data="baghdad;")
   #ah= types.InlineKeyboardButton(text=f"- محاولاتك ({hUkS}) .",callback_data="nothing")
   key.add(a1,a2,a3,a4,a5,a18,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,)
   if str(message.from_user.id)== id:
      hk = types.InlineKeyboardMarkup()
      hk.row_width = 1
      ooi = open("pay.txt", "r")
      o = len(ooi.readlines())
      btn3 = types.InlineKeyboardButton(text=f"- {o} فعلوا البوت 🫡.",callback_data='nothing')
      btn2 = types.InlineKeyboardButton(text="- ارسل التخزين 💾️ .",callback_data="t5")
      hk.add(btn2,btn3)
      bot.reply_to(message,'- اهلا بك ذوالفقار في لوحة الادمن ❤️‍🔥.',reply_markup=hk)
      bot.reply_to(message,'- اختر المحافظة و ابدأ بالبحث! .',reply_markup=key)  
   elif str(message.from_user.id) in u:
      bot.reply_to(message,'- اختر المحافظة و ابدأ بالبحث! ⚡ .',reply_markup=key)
   else:
           keyboard = types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True)
           button_phone = types.KeyboardButton (text = "مشاركة رقمي📱", request_contact = True)
           keyboard.add (button_phone)
           
           bot.send_message (message.chat.id, '''- 🪐 أهلاً بك عزيزي في بوت بيانات العراق الاكثر تطوراً⚡.
- 📌 بأستخدامك للبوت انت توافق على مشاركة رقمك!
- وذلك لغرض مشاركته مع الجهات الامنية في حال استخدمت البوت بشكل خاطئ ⚠️.
- اضغط على الزر ادناه لمشاركة رقمك.''', reply_markup = keyboard)
  else:
   bot.reply_to(message,'-تم تفعيل البوت مجاناً ⚡ ، للأستمرار ارسل /start ')
   open(f'H/H{message.from_user.id}.txt','w').write('tp')
 else:bot.reply_to(message,f'''- مرحباً عزيزي 💘

 🔅| لازم تشترك بقنوات المطورين حتى تگدر تستخدم البوت⚠️
- @FP_BH

   📌| اشترك ثم ارسل /start''')

def search_person_accdb(last_name):
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=path_to_file\1.accdb;')
    cursor = conn.cursor()
    sql_command = f"SELECT * FROM PERSON WHERE LAST_NAME LIKE '{last_name}%'"
    print(sql_command)
    cursor.execute(sql_command)
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data_row = {}
        data.append(row)
    cursor.close()
    conn.close()
    return data

@bot.callback_query_handler(func=lambda m:True)
def qu(call):
     kl = ch(call.from_user.id)
     if kl == None:
      if glob.glob(f'H/H{call.from_user.id}.txt'):
        u = open('pay.txt').read()
        if str(call.message.chat.id) in u or str(call.message.chat.id) == id:
         
         if ';' in call.data:
          place = call.data.split(';')[0]
          h = bot.send_message(call.message.chat.id,'''أدخل المعلومات بهذا الشكل:
- احمد محمد احمد 1940 .
- تگدر ترسل بدون مواليد فقط الاسم الثلاثي .
- الاسماء المركبة تُدمج مثل:
زين العابدين يصير زينالعابدين .
- تحياتي ذوالفقار @IraqsGodFather''')
          bot.register_next_step_handler(h,huks, place)
         if ':' in call.data:
            hU= de(open(f'H/H{call.from_user.id}.txt').read())
            hUKs = en(int(hU)-1)
            open(f'H/H{call.from_user.id}.txt','w').write(f'{hUKs}')
            print(hUKs)
            bot.send_message(call.message.chat.id,'-⚡جارِ جمع معلومات العائلة...')
            place, fam_no = call.data.split(":")
            if fam_no == '':bot.reply_to(call.message,' لا ادود ما تمشي عليه 🗿.')
            else:
             card_info = search_card(fam_no, place)
             message = """"""
             for row in card_info:
                 if place == 'baghdad':
                     h = row[2].replace("\x84", "").strip() if isinstance(row[2], str) else ''
                     u = row[3].replace("\x84", "").strip() if isinstance(row[3], str) else ''
                     ks = row[4].replace("\x84", "").strip() if isinstance(row[4], str) else ''
                     Lives = row[11].replace("\x84", "").strip() if isinstance(row[11], str) else ''
                     area = row[12].replace(" ", "").strip() if isinstance(row[12], str) else ''
                     streat = row[13].replace(" ", "").strip() if isinstance(row[13], str) else ''
                     house = row[14].replace(" ", "").strip() if isinstance(row[14], str) else ''
                     Your_Namper_In_Famliy = row[5]#.replace(" ", "").strip() if isinstance(row[5], str) else ''
                     birth_year = str(int(row[6]))[:-2] if isinstance(row[6], float) else ''
                     results = f"- الاسم : {h} {u} {ks}\n- مواليد : {birth_year}\n- محل الولادة : {Lives}\n- تسلسل الفرد : {Your_Namper_In_Famliy}\n- المحله : {area}\n- الزقاق : {streat}\n- الدار : {house}\n- رقم التموينيه : {row[1]}\n- المطور @z1zziz"
                     bot.send_message(call.message.chat.id, results)
                 else:
                     h = row[3].replace("\x84", "").strip() if isinstance(row[3], str) else ''
                     u = row[4].replace("\x84", "").strip() if isinstance(row[4], str) else ''
                     ks = row[5].replace("\x84", "").strip() if isinstance(row[5], str) else ''
                     Lives = row[22].replace(" ", "").strip() if isinstance(row[22], str) else ''
                     Your_Namper_In_Famliy = row[2]#.replace(" ", "").strip() if isinstance(row[2], str) else ''
                     birth_year = str(int(row[7]))[:-2] if isinstance(row[7], float) else ''
                     results = f"- الاسم : {h} {u} {ks}\n- مواليد : {birth_year}\n- اسم محل الولادة : {Lives}\n- تسلسل الفرد : {Your_Namper_In_Famliy}\n- رقم التموينيه : {row[1]}\n- أشترك للمزيد @z1zziz"
                     bot.send_message(call.message.chat.id, results)



         
         if call.data == 't5': 
            bot.send_document(call.message.chat.id, open('pay.txt','rb'))
         if call.data == 't5': 
            bot.send_document(call.message.chat.id, open('ids.txt','rb'))
        else:
         bot.answer_callback_query(call.id, f"- لازم تتحقق ⚠️.", show_alert=True)
      else:bot.reply_to(call.message,'- ارسل /start .')
     else:bot.reply_to(call.message,f'''- مرحباً عزيزي 💘

 🔅| لازم تشترك بقنوات المطورين حتى تگدر تستخدم البوت⚠️
- @FP_BH

   📌| اشترك ثم ارسل /start''')
def delm7a(message):
 id = (message.text).split(':')[0]
 m= int((message.text).split(':')[1])
 hy=int(de(open(f'H/H{id}.txt','r').read()))
 if m<=hy:
  m7=hy-m
 else:
  m7 = m-hy
 m7 = en(m7)
 print(m7);print(de(m7))
 open(f'H/H{id}.txt','w').write(m7)
def m7a(message):
 id = (message.text).split(':')[0]
 m7 = en((message.text).split(':')[1])
 print(m7)
 open(f'H/H{id}.txt','w').write(m7)
 bot.reply_to(message,f'- تم اضافة {(message.text).split(":")[1]} محاولة الى {id} بنجاح .')
def delqna(message):
 f = open("ch.txt", "r").read()
 HU=(f.replace(f'\n{message.text}',''))
 open('ch.txt','w').write(HU)
 bot.reply_to(message,f'تم حذف القناة {message.text} بنجاح .')
def qna(message):
 open('ch.txt','a').write(f'{message.text}\n')
 bot.reply_to(message,f'تم اضافة القناة {message.text} بنجاح .')
def hukss(message):
 bot.reply_to(message,'انتظر من فضلك...')
 open('pay.txt','a').write(f'{message.text}\n')
 bot.send_message(message.chat.id,f'- تم التفعيل بنجاح ل{message.text}')

 
    
def huks(message, place):
    bot.reply_to(message, 'جارِ البحث ⚡...')
    n = message.text
    h = 0
    try:
        HUKs = n.split(' ')[3]
    except IndexError:
        HUKs = ''
    u = search_person(n.split(' ')[0], n.split(' ')[1], n.split(' ')[2], HUKs, place)
    for person in u:
        if place == 'baghdad':
            name_parts = [part.replace('', '').replace('', '') for part in [person[2], person[3], person[4]] if part]
            name = ' '.join(name_parts)
            Name = f"- الاسم: {name}" if name else ""
            birth_year = str(int(person[6]))[:-2] if isinstance(person[6], float) else ''
            md = f"- المواليد: {birth_year}" if birth_year else ""
            np_t = f"- رقم التموينية: {person[1]}" if person[1] else ""
            Lives = f"- محل الولادة: {person[11]}".strip() if person[11] else ""
            Mathe_Name = f"- اسم الأم: {person[8]} {person[9]}".replace('', '') if person[8] and person[9] else ""
            Work = f"- العمل: {person[7]}" if person[7] else ""
            Muniy = "- الراتب: لا يوجد"
            all_parts = [Name, md, np_t, Lives]
            if Mathe_Name:
                all_parts.append(Mathe_Name)
            if Work:
                all_parts.append(Work)
            all_parts.append(Muniy)
            all_parts = [part for part in all_parts if part]
            all = '\n'.join(all_parts)
            if all.strip():
                fam_no = person[1]
                markup = telebot.types.InlineKeyboardMarkup()
                btn_get_info = telebot.types.InlineKeyboardButton("جلب العائلة 🗂️", callback_data=f"{place}:{fam_no}")
                markup.add(btn_get_info)
                bot.send_message(message.chat.id, all, reply_markup=markup)
        else:
            name_parts = [part.replace('', '').replace('', '') for part in [person[3], person[4], person[5]] if part]
            name = ' '.join(name_parts)
            Name = f"- الاسم: {name}" if name else ""
            birth_year = str(int(person[7]))[:-2] if isinstance(person[7], float) else ''
            md = f"- المواليد: {birth_year}" if birth_year else ""
            np_t = f"- رقم التموينية: {person[1]}" if person[1] else ""
            Lives = f"- محل الولادة: {person[22]}".strip() if person[22] else ""
            Mathe_Name = f"- اسم الأم: {person[18]} {person[19]}".replace('', '').replace('', '')if person[18] and person[19] else ""
            Work = f"- العمل: {person[17]}" if person[17] else ""
            Muniy = f"- الراتب: {int(person[16])}" if person[16] else ""
            all_parts = [Name, md, np_t]
            if Mathe_Name:
                all_parts.append(Mathe_Name)
            all_parts.append(Lives)
            if Work:
                all_parts.append(Work)
            if Muniy:
                all_parts.append(Muniy)
            all_parts = [part for part in all_parts if part]
            all = '\n'.join(all_parts)
            if all.strip():
                fam_no = person[1]
                markup = telebot.types.InlineKeyboardMarkup()
                btn_get_info = telebot.types.InlineKeyboardButton("جلب العائلة 🗂️", callback_data=f"{place}:{fam_no}")
                markup.add(btn_get_info)
                bot.send_message(message.chat.id, all, reply_markup=markup)

        h += 1

    if h == 0:
        bot.reply_to(message, '- لم يتم العثور على نتائج!!\n- اذا متأكد من المعلومات اذن لو الشخص انتقل لغير محافظة\nلو بسبب خطأ في نقل المعلومات من المصدر الرأيسي!\n- تحياتي ذوالفقار @IraqsGodFather')
    else:
        bot.send_message(message.chat.id, "- تم البحث في كل القاعدة،\n-ارسل /start للبحث مرة اخرى ⚡")
    print(h) 

@bot.message_handler(func=lambda message: message.chat.type == 'private',content_types=['contact'])
def forward(message):
     uu=str(message.from_user.id)
     rp = open(f"pay.txt").read()
     if str(uu) in rp:
         print('')
     else:
         print(message.contact)
         if message.contact.user_id == message.from_user.id:
          bot.reply_to(message,'- ارسل /start .')
          rp=open("pay.txt","a").write(f"ID:{message.from_user.id}, Number:{message.contact.phone_number}, Username:@{message.from_user.username}\n")
          rp=open("ids.txt","a").write(f"{message.from_user.id}\n")
          requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=- New one
 - رقمة📱 : {message.contact.phone_number}
 - اسمة📝 : {message.chat.first_name}
 - يوزرة🔗 : @{message.from_user.username}
 - ايدية🪪 : {message.from_user.id}
 - المطور : @z1zziz''')
          
         else:bot.reply_to(message,'شنو صاير ذكي؟\n-ارسل /start و جر عدل')
@bot.message_handler(func=lambda m: True)
def h(message):bot.reply_to(message,'- أرسل /start ⚡')
bot.infinity_polling()

