# nonebot_plugin_weather_lite

使用wttr.in的天气查询 ，支持大部分wttr.in的用法。

使用://github.com/chubin/wttr.in

## 安装：

pip：

```
pip install nonebot-plugin-weather-lite
```


## 命令：

注：

1. 以下`天气`命令均可以使用`wttr`、`weather`、`tianqi`等效替代,
​2. `城市名`可以使用各种语言，例如`Beijing`、`Peking`、`北京`是等效的。
​3. 支持查询全球各种地区。例如莫斯科什么的都可以。
​4. 本项目只是wttr.in在线服务的一个简陋包装。后端代码是人家写的。如果因为各种原因实现不了功能，除了确定是插件的缺陷都不要找我。

### 基础：

`天气 城市名(可选，如不给出机器人会提示获取)`


### 高级一点点:

`天气 城市名 format=2`


`天气 城市名 format=3`


### 指定语言:

`天气 城市名 lang=语言`	语言可选于：

> ```
> am ar af be bn ca da de el et fr fa hi hu ia id it lt mg nb nl oc pl pt-br ro ru ta tr th uk vi zh-cn zh-tw
> ```

例如俄文查询北京：

`天气 北京 lang=ru`


### 多格式联动:

wttr.in支持多种格式联动：

使用2格式、俄文来查询北京：

`天气 北京 format=2 lang=ru`


### 甚至支持看月相：

`天气 Moon`


## 更多用法请参考wttr.in的文档！

地址：https://github.com/chubin/wttr.in

## 缺陷：

1.无法使用`%`自定义格式。

2.其他暂时应该用不上我也没测试的功能。
