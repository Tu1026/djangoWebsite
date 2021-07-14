import discord
import os 
state = False
id = 0                  
def main(name, discrimnator):
  
    uid = int(os.getenv("uid"))
    TOKEN = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    
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
        
    client.run(TOKEN)    
    
    return state, id
    

    
