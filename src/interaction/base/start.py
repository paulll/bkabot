from src.interaction.react import react, reactFallback

@reactFallback('none')
async def handler(input, output):
	await output.answerText('base:mode', """
		Привет!
		Это наша первая встреча, а автор самого бота не умеет писать тексты, так что это просто заглушка.
		Итак, чем займемся?
	""")