from pyecharts import options
from pyecharts.charts import Line, Bar, Scatter


def draw(xlist, ylist):
    line = Line()
    line.add_xaxis(xlist)  # x坐标名称
    line.add_yaxis("线名称", ylist, is_smooth=True)  # 线名称、各点数值、是否平滑
    line.set_global_opts(title_opts=options.TitleOpts(title='name'))  # 表名称
    line.render('xxx.html')  # 生成html文件


def main():
    xlist = ['一', '二', '三', '四', '五']
    ylist = [3, 9, 15, 21, 27]
    draw(xlist, ylist)


if __name__ == '__main__':
    main()