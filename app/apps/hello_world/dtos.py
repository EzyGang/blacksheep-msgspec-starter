import msgspec


class HelloWorld(msgspec.Struct):
    hello: str = 'world'
