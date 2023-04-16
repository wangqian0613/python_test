from abc import ABCMeta
from abc import abstractmethod


class Payment:
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self, money):
        print(f"this is Alipay, money is {money}")


class WechatPay(Payment):
    pass


p = Alipay()
print(p.pay(20))


class User(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class VIPUser(User):
    def swim(self):
        return "this is  VIP swim"

    def fly(self):
        return "this is VIP fly"


class SIPUser(User):
    def swim(self):
        return "this is  SIP swim"

    def fly(self):
        return "this is SIP fly"


def func(user: User):
    return print(user.fly(), user.swim())

