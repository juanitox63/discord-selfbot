import discord, os, asyncio
from discord.ext import commands

# Usar el nombre de la variable de entorno "token" aquí, no el valor del token directamente.
token = "put your token here "
# Verificar si el token es None
if token is None:
    print("Token no encontrado, asegúrate de haber configurado la variable de entorno correctamente.")
    exit()

client = commands.Bot(command_prefix='s', self_bot=True)


#in this lines you can put commands 

@client.command()
async def purge(ctx, limit: int):
    counter = 0
    await ctx.message.delete()
    async for message in ctx.channel.history(limit=limit):
        if message.author == ctx.author:
            try:
                await message.delete()
                counter += 1
            except:
                await asyncio.sleep(3)
                continue
    await ctx.send(f"` Se eliminaron {counter} mensajes. `", delete_after=5)

@client.command()
async def flud(ctx, cantidad: int, *, mensaje: str):
    if cantidad < 1 or cantidad > 30:
        await ctx.send("La cantidad debe estar entre 1 y 30.")
        return

    grupos_de_mensajes = (cantidad + 4) // 5

    for i in range(grupos_de_mensajes):
        mensajes_a_enviar = min(cantidad - i * 5, 5)
        mensajes = [mensaje] * mensajes_a_enviar
        await asyncio.gather(*[ctx.send(msg) for msg in mensajes])

@client.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    await ctx.send(member.avatar.url)  # Actualiza a 'avatar.url'


class RepetirTarea:
    def __init__(self, ctx, tiempo, mensaje):
        self.ctx = ctx
        self.tiempo = tiempo
        self.mensaje = mensaje
        self._task = None

    async def iniciar(self):
        while True:
            await self.ctx.send(self.mensaje)
            await asyncio.sleep(self.tiempo)

    def cancelar(self):
        if self._task:
            self._task.cancel()


# Ejecuta el bot con el token cargado
client.run(token)