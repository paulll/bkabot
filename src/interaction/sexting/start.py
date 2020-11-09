from src.interaction.react import react

@react('base:mode', ['Хочу сессию'])
async def handler(input, output):
	await output.answerText('dating:placeholder', """
		Сессии пока в разработке, но скоро будет готово
	""")

@react('sexting:placeholder', ['Подожду разработку..'])
async def handler(input, output):
	await output.answerText('sexting:placeholder', """
		Хм.. ну, ждём
	""")

@react('sexting:placeholder', ['Хочу обратно'])
async def handler(input, output):
	await output.answerText('none', """
		Окей, забудем что было раньше
		Чем займемся?
	""")