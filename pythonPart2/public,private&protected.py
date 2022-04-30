class dad:
    basketball = 1
    _protec= 12
    __private = 34


class son(dad):
    dance = 1
    basketball = 3

    def isdance(self):
        return f"you dance {self.dance} times better"


class grandson(son):
    dance = 6
    def isdance(self):
        return f"grandson dance {self.dance} times beetter than the son"
darry =dad()
karry =son()
marry =grandson()
print(darry.__private)