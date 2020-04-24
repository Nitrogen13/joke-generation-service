import unittest

import logging
import unittest
from pathlib import Path
import pytest
import pook
from aiogram import Bot
import json

API_TOKEN = "1488228:vaLeRaaniMeboY"


logger = logging.getLogger('__telegram_test__')
logger.setLevel(logging.DEBUG)

logging_path = Path('telegram.log')

def get_mock_message(text):
    return {'caption': '',
            'channel_chat_created': False,
            'chat': {'first_name': 'Anime',
                     'id': 167777762,
                     'last_name': 'Boy',
                     'title': '',
                     'type': 'private',
                     'username': 'animeboy'},
            'date': 1473531115,
            'delete_chat_photo': False,
            'entities': [],
            'from': {'first_name': 'Anime',
                     'id': 167777762,
                     'last_name': 'Boy',
                     'type': '',
                     'is_bot': False,
                     'username': 'animeboy'},
            'group_chat_created': False,
            'message_id': 1488,
            'migrate_from_chat_id': 0,
            'migrate_to_chat_id': 0,
            'new_chat_photo': [],
            'new_chat_title': '',
            'photo': [],
            'supergroup_chat_created': False,
            'text': text}


	
    
@pytest.yield_fixture(name='bot')
async def bot_fixture():
    """ Bot fixture """
    pook.on()
    _bot = Bot(API_TOKEN)
    yield _bot
    await _bot.close()
    pook.off()

@pytest.mark.asyncio
async def test_me(bot):
	pook.post(f'https://api.telegram.org/bot{API_TOKEN}/getMe',
	             response_json={
	                 'ok': True,
	                 'result': {
	                     'id': 1,
	                     'is_bot': True,
	                     'first_name': 'Test Bot',
	                     'username': 'test_bot'
	                 }
	             })


	res = json.loads(str(await bot.me))
	assert(res['username'] == 'test_bot')


@pytest.mark.asyncio
async def test_updates(bot):
	pook.post(f'https://api.telegram.org/bot{API_TOKEN}/getFile',
	          response_json={
	              'ok': True,
	              'result': {
	                  'file_id': "id",
	                  'file_size': 0,
	                  'file_path': "path"
	              }
	          })

	pook.post(f'https://api.telegram.org/bot{API_TOKEN}/sendMessage',
	          times=3,
	          response_json={
	              'ok': True,
	              'result': {
	                  'chat_id': 167777762,
	                  'text': '...',
	                  'reply_markup': {
	                      'remove_keyboard': True,
	                      'selective': False
	                  }
	              }
	          })
	pook.post(f'https://api.telegram.org/bot{API_TOKEN}/getUpdates',
	          response_json={
	              'ok': True,
	              'result': [
	                  {
	                      'update_id': 919389466,
	                      'message': get_mock_message('/start')
	                  }, {
	                      'update_id': 919389467,
	                      'message': get_mock_message('/help')
	                  },
	                  {
	                      'update_id': 919389468,
	                      'message': get_mock_message('common phrase')
	                  }
	              ]
	          })
	res = await bot.get_updates()
	res = [json.loads(str(x))['update_id'] for x in res]
	assert(res == [919389466, 919389467, 919389468])
