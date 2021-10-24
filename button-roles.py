
@client.command()
async def button(ctx):
    await ctx.channel.send(
        "Rol Almak İçin Butonlara Tıkla!",
        components = [
            Button(style=ButtonStyle.blue, label="Rol Al")
        ]
    )


    res = await client.wait_for("button_click")
    if res.channel == ctx.channel:
        role = discord.utils.get(ctx.guild.roles, id = RolID) #buraya butona basinca alinacak rolün ID'sini girin
        await res.author.add_roles(role)
        await res.respond(
            type=4,
            content=f"{res.component.label} Tıklandı"
        )
#discord-components modülü gereklidir
