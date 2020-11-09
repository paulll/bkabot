import textwrap
from telethon import Button

from .context_storage import set_user_context

from src.interaction.react import context_listeners

class Output(object):
	"""Функции вывода ответа для пользователя"""
	def __init__(self, event):
		super(Output, self).__init__()
		self.source_message = event.message

	async def answerText(self, new_context, text):
		text = textwrap.dedent(text)
		reactions = []
		if '_keyphrases' in context_listeners[new_context]:
			for (kp, _) in context_listeners[new_context]['_keyphrases']:
				reactions.append([Button.text(kp[0])])

		if not len(reactions):
			await self.source_message.respond(text)
		else:
			await self.source_message.respond(text, buttons=reactions)	
		await set_user_context(self.source_message.from_id, new_context)
