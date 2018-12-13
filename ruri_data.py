# 마치 은행처럼 데이터 예금과 인출을 하는 역할
class Ruri_Data:
    def __init__(self, cno, clink, ctitle, cthumb, ccontent, clinks, creplies):
        self.__cno = cno
        self.__clink = clink
        self.__ctitle = ctitle
        self.__cthumb = cthumb
        self.__ccotent = ccontent
        self.__creplies = creplies

    #setter/getter
    @property
    def cno(self):
        return self.__cno

    @cno.setter
    def cno(self, value):
        self.__cno = value

    @property
    def clink(self):
        return self.__clink

    @clink.setter
    def clink(self, value):
        self.__clink = value

    @property
    def ctitle(self):
        return self.__ctitle

    @ctitle.setter
    def ctitle(self, value):
        self.__ctitle = value

    @property
    def cthumb(self):
        return self.__cthumb

    @cthumb.setter
    def cthumb(self, value):
        self.__cthumb = value

    @property
    def ccontent(self):
        return self.__ccontent

    @ccontent.setter
    def ccontent(self, value):
        self.__ccontent = value

    @property
    def clinks(self):
        return self.__clinks

    @clinks.setter
    def clinks(self, value):
        self.__clinks = value

    @property
    def creplies(self):
        return self.__creplies

    @creplies.setter
    def creplies(self, value):
        self.__creplies = value


    def __str__(self):
        data = '%s %s %s %s %s %s' % (
            self.__cno, 
            self.__clink, 
            self.__ctitle, 
            self.__cthumb, 
            self.__ccotent, 
            self.__creplies)
        return data


    

