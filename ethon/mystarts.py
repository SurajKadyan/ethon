#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.send_message(st)
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")]])
    
