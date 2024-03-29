from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print("中间件 process_request方法被调用！")
        print("路由是：", request.path)
        print("请求方式是：", request.method)
        if request.path == '/aaaa':
            return HttpResponse('当前路由是：/aaaa')

from django.http import HttpResponse
from django.http import Http404

class VisitLimit(MiddlewareMixin):
    # 此字典的键为IP地址，值为, 此IP地址的访问次数
    visit_times = {}
    def process_request(self, request):
        ip = request.META['REMOTE_ADDR']  # 得到客户端IP
        if request.path_info != '/test':
            return None
        # 获取以前的访问次数
        times = self.visit_times.get(ip, 0)
        print("IP", ip, '已访问过/test', times, '次')
        self.visit_times[ip] = times + 1
        if times < 5:
            return None
        return HttpResponse("您已经访问过："+ str(times)
                            + '次')


