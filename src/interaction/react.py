import importlib
import pkgutil
import sys

import src.interaction.base as base
import src.interaction.dating as dating 
import src.interaction.sexting as sexting

from functools import wraps
from collections import defaultdict


# dict<string context,dict<(list<string keyphrase>|"_image"|"_voice"|"_fallback"), callback(inputInterface, outputInterface)>> 
context_listeners = defaultdict(dict)


def react(context, keyphrases):
	"""Создает реакцию на определенные фразы пользователя в заданном контексте
	Args:
		context: Контекст, в котором рассматривается данная реакция
		keyphrases: Ключевые фразы, на которые здесь описывается реакция
	"""

	def decorator(func):
		if not '_keyphrases' in context_listeners[context]:
			context_listeners[context]['_keyphrases'] = []
		context_listeners[context]['_keyphrases'].append( (keyphrases, func) )

		@wraps(func)
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
		return wrapper
	return decorator


def reactImage(context):
	"""Создает реакцию на фотографию в заданном контексте
	Args:
		context: Контекст, в котором рассматривается данная реакция
	"""

	def decorator(func):
		context_listeners[context]['_image'] = func
		@wraps(func)
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
		return wrapper
	return decorator


def reactVoice(context):
	"""Создает реакцию на войс в заданном контексте
	Args:
		context: Контекст, в котором рассматривается данная реакция
	"""

	def decorator(func):
		context_listeners[context]['_voice'] = func
		@wraps(func)
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
		return wrapper
	return decorator


def reactFallback(context):
	"""Создает реакцию на случай если не нашлось другой подходящей реакции в заданном контексте
	Args:
		context: Контекст, в котором рассматривается данная реакция
	"""

	def decorator(func):
		context_listeners[context]['_fallback'] = func
		@wraps(func)
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
		return wrapper
	return decorator


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results

import_submodules(base)
import_submodules(dating)
import_submodules(sexting)
