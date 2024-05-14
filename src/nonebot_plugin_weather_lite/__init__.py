from nonebot import get_plugin_config, require, get_driver
from nonebot.adapters import Bot
from nonebot.drivers import Request, HTTPClientMixin
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require('nonebot_plugin_alconna')

from arclet.alconna import Alconna, Args, CommandMeta, MultiVar, KeyWordVar
from nonebot_plugin_alconna import  Match, UniMessage, on_alconna

from .config import Config


__plugin_meta__ = PluginMetadata(
    name="简易天气",
    description="利用 wttr.in 查询天气",
    usage="天气 [城市] [查询项=参数]",
    homepage="https://github.com/noneplugin-renew/nonebot_plugin_weather_lite",
    type="library",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={
        "author": "zjkwdy",
        "priority": 1,
        "version": "0.1.1",
    },
)

_pconfig = get_plugin_config(Config)

wettr = on_alconna(
    Alconna(
        "天气", 
        Args["city?", str]["query?", MultiVar(KeyWordVar(str), "*")], 
        meta=CommandMeta(
            "利用 wttr. in 查询天气",
            compact=True,
            usage="天气 [城市] [查询项=参数]",
            example="""\
北京天气
天气 北京 format=v2
"""
        )
    ), 
    aliases={'wttr', 'weather', 'tianqi'},
    use_cmd_start=True,
    auto_send_output=True
)

wettr.shortcut(r"(?P<city>\w+?)天气", prefix=True, arguments=["{city}"], humanized="<城市>天气")
wettr.shortcut("月相", prefix=True, fuzzy=False, arguments=["Moon"])


@wettr.handle()
async def _handle(city: Match[str]):
    if city.available:
        wettr.set_path_arg('city', city.result)


@wettr.got_path('city', prompt='你想查询哪个城市的天气呢？')
async def _(bot: Bot, city: str, query: Match[dict[str, str]]):
    if city[0]!='_':
        await UniMessage.text('少女观星中...').send(at_sender=True)
        url = f'http://zh.wttr.in/{city}'
        if _pconfig.wttr_image_output:
            if query.available and query.result:
                url += "_"
                url += "_".join([f"{k}={v}" for k, v in query.result.items()])
                url += ".png"
            await UniMessage.image(url=url).finish(at_sender=True)
        else:
            url += "?T&tqp0"
            if query.available and query.result:
                url += "&"
                url += "&".join([f"{k}={v}" for k, v in query.result.items()])
            text = await bot.adapter.request(Request('GET', url))
            await UniMessage.text(text.content.decode()).finish(at_sender=True)  # type: ignore
    else:
        await wettr.reject_path('city',prompt='不能使用“_”作为查询前缀！请重新输入！')


driver = get_driver()

@driver.on_startup
async def check_config():
    if not isinstance(driver, HTTPClientMixin):
        raise ValueError(f"Current driver {driver} does not support HTTPClientMixin")
