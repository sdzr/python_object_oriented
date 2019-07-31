# 创建共享的类级记录器
import logging

def logged(class_):
    class_.logger = logging.getLogger(class_.__qualname__)
    return class_

@logged
class Player:
    def __init__(self,test_str):
        self.logger.debug("debug test {}".format(test_str))



# 配置logging的handler
import sys
logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)

A = Player('AAAA')


