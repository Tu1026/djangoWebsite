from logging import fatal
import discord
import os 
import asyncio
from concurrent.futures import ThreadPoolExecutor
def main(name, discrimnator):
    state = False
    id = 0
    def check_valid_name():
        asyncio.set_event_loop(asyncio.new_event_loop())

        uid = int(os.getenv("uid"))
        TOKEN = os.getenv("DISCORD_TOKEN")
        intents = discord.Intents.all()
        client = discord.Client(intents=intents)
        state = False
        id = 0
        @client.event 
        async def on_ready():
            guild = client.get_guild(uid)
            for member in guild.members:
                if member.name == name and member.discriminator == discrimnator:
                    global state 
                    state = True
                    print(f'state inside of on read {state}')
                    global id 
                    id = member.id
                    print(f'id inside of on ready {id}')
                    await member.send("Thank you for registering! You have entered correct username")
            await client.close()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.start(TOKEN))
        print(f'state and id outside {state} , {id}')
        return state, id
        
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(check_valid_name)
        print(future.result())
        
    return state, id
    

    
