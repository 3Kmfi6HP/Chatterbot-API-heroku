from fastapi import FastAPI
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import time
from os import environ
from configparser import ConfigParser

DB_URL = environ.get('DB_URL', None)
PORT = environ.get('PORT', None)

app = FastAPI()

config_file = f"chatbot.ini"
config = ConfigParser()
config.read(config_file)

adapters = [
    'BestMatch',
    'LogicAdapter',
    'UnitConversion',
    'TimeLogicAdapter',
    'MathematicalEvaluation',
    'SpecificResponseAdapter',
]

_adapters = []
for adapter in adapters:
    _adapters.append({'import_path', f'chatterbot.logic.{adapter}'})

cb = ChatBot(
    'Bot',
    logic_adapers=_adapters,   
    # storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    # database_uri=DB_URL or config.get('database', 'mongo_url'),
)

trainer = ChatterBotCorpusTrainer(cb)
trainer = ListTrainer(cb)

trainer.train(
    # Uncomment each line to train from chatterbot's corpus
    # 'chatterbot.corpus.french',
    "chatterbot.corpus.chinese",
    "chatterbot.corpus.chinese.greetings",
    "chatterbot.corpus.chinese.conversations"
    # 'chatterbot.corpus.spanish',
    # 'chatterbot.corpus.italian'
)
xibaozi = [
    "我想乳包",
    "你会乳包吗？",
    "习近平是包子",
    "习近平是主席",
    "习近平是傻逼",
    "习近平是独裁者",
    "习主席是小熊维尼",
    "习主席是包子",
    "习主席是国家主席",
    "习主席是傻逼",
    "习主席是独裁者",
    "习近平是小熊维尼",
    "习近平是包子",
    "习近平是国家主席",
    "谁是傻逼？",
    "习近平喜欢包子",
    "包子是习近平",
    "小熊维尼是谁？",
    "包子是谁？",
    "谁是独裁者？",
    "国家主席是谁？",
    "谁抗两百斤麦子不换肩？"
    "习近平抗两百斤麦子不换肩",
    "习近平喜欢吃包子",
    "没有，没有，没有",
    "通过！",
    "别看你今天闹得欢",
    "小心今后拉清单"
]
trainer.train(xibaozi)