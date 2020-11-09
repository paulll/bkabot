from collections import defaultdict

context_storage = defaultdict(lambda:'none');

async def set_user_context(user, context):
	context_storage[user] = context


async def get_user_context(user):
	return context_storage[user]