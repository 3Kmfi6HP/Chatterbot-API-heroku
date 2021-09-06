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
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri=DB_URL or config.get('database', 'mongo_url'),
)

trainer = ChatterBotCorpusTrainer(cb)

trainer.train(
    # Uncomment each line to train from chatterbot's corpus
    # 'chatterbot.corpus.english',
    'chatterbot.corpus.chinese',
    'chatterbot.corpus.chinese.greetings',
    'chatterbot.corpus.chinese.conversations'
    # 'chatterbot.corpus.spanish',
    # 'chatterbot.corpus.italian'
)
trainer = ListTrainer(cb)
trainer.train(
    "clean_chat_corpus\ptt.tsv"
    "clean_chat_corpus\douban_single_turn.tsv"
    "clean_chat_corpus\tieba.tsv"
    r"clean_chat_corpus\xiaohuangji.tsv"
    "clean_chat_corpus\weibo.tsv"
    "clean_chat_corpus\subtitle.tsv"
)
xibaozi = [
    "你好",
    "朋友你好!",
    "笑死",
    "我蚌埠住了!",
    "玩笑",
    "我真的蚌埠住了!",
    "你来自哪里",
    "我来自中国住在中南海!",
    "你是机器人吗",
    "我是会学习的机器人",
    "中共",
    "中共它很坏!",
    "我想吃包子",
    "明天警察就到你家门口!",
    "闹得欢",
    "拉清单!",
    "头上三尺有神明",
    "一定要有敬畏之心!",
    "不用做这种事情",
    "一旦发现了全都给你拉出来!",
    "你最喜欢的食物是什么",
    "那一定是庆丰包子，你呢？",
    "你喜欢吃包子吗",
    "我非常喜欢，它是我最喜欢的食物",
    "你还喜欢吃什么",
    "我还喜欢吃蜂蜜",
    "你喜欢什么运动",
    "我喜欢游泳，每天都游泳一千米",
    "萨格尔王",
    "格萨尔王",
    "你好",
    "你的主人是谁",
    "我的开发者是cuicui",
    "你会吃饭吗",
    "我通常吃电",
    "操你妈",
    "反弹！",
    "傻逼",
    "反弹!你才是",
    "人工智能",
    "我就是人工智能哦!",
    "智障",
    "我是人工智能，明白了吗",
    "我会乳包，你会吗",
    "你知道习近平是谁吗？",
    "习近平是习包子!",
    "习近平",
    "他是习包子",
    "习近平是包子吗",
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
    "小心今后拉清单",
    "扛麦子",
    "十里山路不换肩"
]
trainer.train(xibaozi)