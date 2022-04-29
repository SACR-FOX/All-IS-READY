from rest_framework.pagination import PageNumberPagination


# 自定义普通分页
class TopicPageNumberPagination(PageNumberPagination):
    # 默认一页的条数
    page_size = 12
    # 用户可以自定义选择一页的条数，但最多显示10条
    page_size_query_param = 'page_size'
    max_page_size = 12
    # 获取页码数
    page_query_param = 'page'
    # 默认条数访问 /我们路由设置访问这个视图的路由/?page=页面号
    #       eg：/我们路由设置访问这个视图的路由/?page=1
    # 自定义条数访问 /我们路由设置访问这个视图的路由/?page=页面号&page_size=一页的条数
    #       eg：/我们路由设置访问这个视图的路由/?page=1&page_size=10

class CommunityNumberPagination(PageNumberPagination):

    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12
    page_query_param = 'page'

