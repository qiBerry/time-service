# This is a sample Python script.
from datetime import datetime,tzinfo,timedelta
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name


moscow = Zone(3,False,'MSK')
def main_time():
    return 'Текущее время (✿◡‿◡) --> ' + str(datetime.now(moscow).time())


if __name__ == '__main__':
    print(main_time())
