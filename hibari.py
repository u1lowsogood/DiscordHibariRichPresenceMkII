from pypresence import Presence
import time
import random

client_id = '1013299986882113646'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop
print("RPC Connected!")

def setRandomPRC():
    large_text = random.choice(["デビュー前","AI化直前","ヒバライザー","サバイバルマッチ","ひばり～終焉～","天誅ひばり","殲滅ひばり"])
    state = random.choice(["アルティメットアビリティ","キラーマシン起動","タクティカルニューク発動","DEFCON1","みそらひばれ"])
    detail = random.choice(["濁流","氾濫","決壊","泥水","汚染水","工業排水"])

    large_face = random.choice(["1","2","3","4","5","6","front","left_upper","right1","right2"])
    small_koukandos = random.choice([["koukando","ごきげん"],["koukando2","ごきげんななめ"],["koukando3","恋心"],["koukando4","恋人未満"],["koukando5","メンヘラ"]])

    partysize = [random.randint(1,15),random.randint(1,15)]

    label = random.sample(["美空ひばり 名曲９００選","美空ofMontage","汚地ひばらず","味噌らひばり","みそら日払い","MISORA","みそらペンタキル","みみみそそそららら"],2)
    url = "https://youtu.be/Pb-N5VPy-40?t=71"

    buttons=[{"label": label[0], "url": url}, {"label": label[1], "url": url}]

    RPC.update(large_text=large_text,state=state,details=detail,large_image=large_face,small_image=small_koukandos[0],small_text=small_koukandos[1],party_size=partysize,buttons=buttons)
    print("RPC UPDATED")

while True:  # The presence will stay on as long as the program is running
    setRandomPRC()
    time.sleep(4) # Can only update rich presence every 15 seconds



