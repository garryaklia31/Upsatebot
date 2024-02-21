import requests,json,os
import string,random,string,json,sys
from datetime import datetime ,timedelta
import requests,json,re,asyncio,time

#from telebot.async_telebot import AsyncTeleBot
#import asyncio
#from telebot.asyncio_filters import TextMatchFilter, TextFilter, IsReplyFilter

import wget,time
import asyncio
#from pyrogram import Client,filters
from telebot.custom_filters import TextFilter, TextMatchFilter ,IsReplyFilter

from telebot import TeleBot, types
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
import telebot
from telebot import util

auth='6819695620:AAHpNgX852w0MktEN8fFGWd4RzW3PtMoOTY'
bot = telebot.TeleBot(auth)
#bot.worker_pool = util.ThreadPool(bot ,num_threads=8)
 
#bot=AsyncTeleBot(auth)
# creating a instance
def markup(urlx,token):
    mark=InlineKeyboardMarkup()
    mark.width=2
    mark.add( InlineKeyboardButton('Click to get FREE Token ', url=urlx))
    mark.add(InlineKeyboardButton('HOW TO TAKE TOKEN CLIK HERE',url='t.me/japanese_live_actionz/12'))
    tym=datetime.now()
    os.system(f'echo "{token}" >> verify_{tym.strftime("%y")}_{tym.strftime("%m")}_{tym.strftime("%d")}.txt')

    return mark 




def get_shortlink( link):

    shor=f'https://instantearn.in/api?api=5a7978c7a9c8cc46c87802ee7fcd7a56e84be1a6&url={link}'
    r=requests.get(shor,headers={'Connection':'close'})
    js=json.loads(r.content)
    print(r.content)
    sh=js['shortenedUrl']
    #dbl= requests.get(f'https://omegalinks.in/api?api=c804e775efb5506dd2dd3b565cdedfea7807ef9b&url={sh}')                     
    #jx=json.loads(dbl.content)
    #kx=jx['shortenedUrl']
    return sh


def time_checker(yearx,monthx,dayx,hourx,mintx):
    tchk=datetime.now()
    y=tchk.strftime("%Y")
    m=tchk.strftime("%m")
    d=tchk.strftime("%d")
    h=tchk.strftime("%H")
    mi=tchk.strftime("%M")
    kk=datetime(int(y),int(m),int(d),int(h),int(mi))
    ik=datetime(int(yearx),int(monthx),int(dayx),int(hourx), int(mintx))
    if ik > kk:
        return True
    else:
        return False
    
def mid_chk(mid,table):
    tstr=datetime.now()
    ox=open(f"verify_{tstr.strftime('%y')}_{tstr.strftime('%m')}_{tstr.strftime('%d')}.txt",'r')
    prt= ox.read().splitlines()
    ox.close()
    os.system(f"sed -i '/{table}/d' verify_{tstr.strftime('%y')}_{tstr.strftime('%m')}_{tstr.strftime('%d')}.txt")
    if table in prt:
        result=datetime.now() + timedelta(hours=12)
        print(result) 
        os.system(f'echo "{result.strftime("%Y:%m:%d:%H:%M")}" > {mid}.txt')
        return True
   # else:
  #      return False
   




@bot.message_handler(commands=["start"])
def stt(message):

    try:
        thike=message.text.split()[1]
        ck=mid_chk(message.chat.id,thike)
        if ck:
            bot.reply_to(message,'BOT TOKEN VERIFIED SUCCESSFULLY')
 #       else:

#            bot.reply_to(message,"invalid Token ")
    except Exception as e:
        bot.reply_to(message, 'starting bot THIS IS TERABOX DOWNLOADER BOT SEND LINK to know usage')


import string
@bot.message_handler(commands=["kxzen"])
def strt(message):
    os.system('rm -rf *.tmp')
   # os.system('rm -rf *.txt')
    os.system('find . -type f ! -name "*.*" -delete')
    os.system('rm -rf *.mp4')
    bot.reply_to(message, 'executed')

#from pyrogram import Client

@bot.message_handler(text=TextFilter(contains=['tera']))
def linkx(message):
    try:
        o=open(f'{message.chat.id}.txt','r')
        s=o.read().split(":")
        print('->',s[4].strip('\n'))
        o.close()
    except:
        
        token=  ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#      print(token)
        urlx=get_shortlink(f'https://telegram.me/terabox_link_download_bot?start={token}')
 
        bot.send_message(message.chat.id,'Your Ads token is expired, refresh your token and try again.\n\nToken Timeout: 12 hours \nWhat is the token?\n\nThis is an ads token. If you pass 1 ad, you can use the bot for 12 Hour after passing the ad.' ,reply_markup=markup(urlx,token.strip()))
        return False
    tf=time_checker(s[0],s[1],s[2],s[3],s[4])
    print(tf)
    
    if tf:
            
            bot.send_message(message.chat.id,'LINK RECEIVED FETCHING')
    #bot.reply_to(message,'FETCHING')
            mid=message.chat.id
            global a
            nm=str(random.randint(1,100))
            res= ''.join(random.choices(string.ascii_lowercase,k=4))
            nametxt=res+nm
            os.system('service tor reload')
            time.sleep(1)
            os.system(f"torsocks python3 spt.py {message.text} {nametxt}.txt " )
#    os.system('service tor reload')
      #      except:
               # bot.reply_to(message,"Re Send Link")

            time.sleep(10)
            a=eval(open(f"{nametxt}.txt",'r').read())


            os.system(f'rm -rf {nametxt}.txt')

           
            siz=a.get('size')
            file=a.get('file_name')
            thumb=a.get('thumb')  
            capt=file
         
         #   nfile=nametxt+'.'+extsp
      
   # except:
    #            bot.reply_to(message,'INTERNAL ERROR SEND again') 
     #           return False
#                continue
            tdown=wget.download(thumb)
  		    				             				                  		
            bot.send_photo(mid,thumb, caption=f'Downloading->{file} \n size -> {siz}')
            file=file.split(".")[-1]
            filex=nametxt+"."+file
          #  print(file)
          
            mid=message.chat.id
            def link(urlz,count=0):
                count+=1
                if count>3:
                    bot.reply_to(message,"TOTAL ERROR OCCURED BOT DAMAGED")
                    return False
                try:
             
                    filw=wget.download(urlz,out=filex)
 
                    bot.reply_to(message,'download complete uploading here')
                    os.system(f'python3 pyr.py "{mid}" "{filex}" "{tdown}" "{capt}"')
  

                except:
                    link(urlz,count)
 
            def ld(urlx,count=0):
                count+=1
                if count>4:
                    bot.reply_to(message,"THIS FILE DOWNLOAD TAKES TIME DOWNLOADING ") #eply_to(message,"ERORR Try again ")
                    link(a.get("link"))
                    return False
							      
                try:
                    #print(file)
                    filedown=wget.download(urlx,out=filex)
                    bot.reply_to(message,'uploading the video sending u wait !! \n')
                    time.sleep(1)
                    os.system(f'python3 pyr.py "{mid}" "{filex}" "{tdown}" "{capt}"')
            												 
                except:
                    ld(urlx,count)
	 		      				                            
            ld(a.get('direct_link'))
            os.system(f'rm -rf *.tmp')
    else:
            token=  ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#      print(token)
            urlx=get_shortlink(f'https://telegram.me/terabox_link_download_bot?start={token}')
						  
            bot.send_message(message.chat.id,'Your Ads token is expired, refresh your token and try again.\n\nToken Timeout: 24 hours \nWhat is the token?\n\nThis is an ads token. If you pass 1 ad, you can use the bot for 24 Hour after passing the ad.' ,reply_markup=markup(urlx,token.strip()))
    #except:
     #   bot.reply_to(message,'ERROR IN LINK TRY AGAIN SENDING ANOTHER')
bot.add_custom_filter(TextMatchFilter())
#import asyncio
bot.infinity_polling()
#asyncio.run(bot.polling)
