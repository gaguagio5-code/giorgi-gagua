def greeter_bot():
    name = yield ""         
    while True:
        name = yield f"Hello, {name}!"
bot = greeter_bot()
print(next(bot))
print(bot.send("Ana"))
