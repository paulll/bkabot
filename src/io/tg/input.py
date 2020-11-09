from telethon import events, functions

from src.client import client
from src.interaction.react import context_listeners

from .output import Output
from .context_storage import get_user_context

class Input(object):
	"""Поступивший от пользователя ввод"""
	def __init__(self, event):
		super(Input, self).__init__()
		print(event)


async def on_unhandled(input, output):
	print('unhandled', input)

@client.on(events.NewMessage)
async def input_handler(event):
	user_context = await get_user_context(event.message.from_id)
	
	input_handle = Input(event)
	output_handle = Output(event)

	message = event.message.message
	if event.message.photo:
		message = '_image'
	if event.message.voice:
		message = '_voice'

	# todo: log the last case
	listener = context_listeners[user_context].get(message, on_unhandled)
	if listener == on_unhandled and '_keyphrases' in context_listeners[user_context]:
		for (kp_list, callback) in context_listeners[user_context]['_keyphrases']:
			print('check', message, kp_list)
			if message in kp_list:
				listener = callback

	if listener == on_unhandled and '_fallback' in context_listeners[user_context]:
		listener = context_listeners[user_context]['_fallback']

	await listener(input_handle, output_handle)
