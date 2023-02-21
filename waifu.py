import requests,os
from datetime import datetime

response=""

numbers=0
i=0


def ask_category():
    global category
    category=input("\nChoose category:\n1.versatile\n2.nfsw\n[typetype your choice | eg:versatile]\n")
    os.system('cls')

ask_category()

def ask_tags_versatile():
    global tags_versatile
    tags_versatile=input("\nChoose tag:\n1.maid\n2.waifu\n3.oppai\n4.selfies\n5.uniform\n[type your choice | eg:waifu]\n")
    os.system('cls')

def ask_tags_nsfw():
    global tags_nsfw
    tags_nsfw=input("\nChoose tag:\n1.ass\n2.hentai\n3.milf\n4.oral\n5.ecchi\n6.ero\n[type your choice | eg:hentai]\n")
    os.system('cls')

def ask_gif_or_img():
    global gif_or_img
    gif_or_img=input("\nChoose category:\n1.image\n2.gif\n[type your choice | eg.gif]\n")
    os.system('cls')
    return (gif_or_img=="gif")

def ask_numbers():
    global numbers
    numbers=int(input("\nHow many photos do you want ?\n[type your choice | eg:5]\n"))
    os.system('cls')

def set_nfsw_base_URL(tag,bool):
    global base_URL_nfsw
    base_URL_nfsw="https://api.waifu.im/search/?included_tags="+tag+"&is_nsfw=true&gif="+str(bool)

def set_versatile_base_URL(tag,bool):
    global base_URL_versatile
    base_URL_versatile="https://api.waifu.im/search/?included_tags="+tag+"&is_nsfw=false&gif="+str(bool)

def get_response():
    global response
    if category=="versatile":
        response=requests.get(base_URL_versatile)
    else:
        response=requests.get(base_URL_nfsw)


def start_download(n):
    while (n>0):
        now = datetime.now()
        get_response()
        response_json=response.json()
        pic_url=response_json['images'][0]['url']
        response_link=requests.get(pic_url)
        with open(str(now.microsecond)+".jpg","wb") as f:
            f.write(response_link.content)
        n=n-1



if category=="versatile":
    ask_tags_versatile()
    gif_or_img=ask_gif_or_img()
    set_versatile_base_URL(tags_versatile,gif_or_img)
    ask_numbers()
    start_download(numbers)
    
elif category=="nfsw":
    ask_tags_nsfw()
    gif_or_img=ask_gif_or_img()
    set_nfsw_base_URL(tags_nsfw,gif_or_img)
    ask_numbers()
    start_download(numbers)
    
else:
    print("Type correctly")






    








