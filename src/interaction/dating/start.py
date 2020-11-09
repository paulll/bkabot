from src.interaction.react import react

@react('base:mode', ['Знакомства'])
async def handler(input, output):
	await output.answerText('dating:placeholder', """
		Знакомства пока в разработке :c
	""")

@react('dating:placeholder', ['Подожду разработку..'])
async def handler(input, output):
	await output.answerText('dating:placeholder', """
		Хм.. ну, ждём
	""")

@react('dating:placeholder', ['Хочу обратно'])
async def handler(input, output):
	await output.answerText('base:mode', """
		Окей, забудем что было раньше.
		Чем займемся?
	""")