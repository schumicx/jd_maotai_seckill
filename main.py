import sys

from maotai.jd_spider_requests import JdSeckill

def get_choice_from_arg():
    """
        添加带参数快速启动脚本的特性，可以搭配Windows任务计划程序，早上定时触发抢茅台。
    """
    import argparse
    parser = argparse.ArgumentParser(description='Automatic seckill maotai on jd.com, good luck!')
    parser.add_argument("-c", "--choice", type=str, default=None, help="id of the choice_function, '1' for resrve and '2' for seckill.")
    args = parser.parse_args()
    return args.choice

if __name__ == '__main__':
    a = """

       oooo oooooooooo.            .oooooo..o                     oooo         o8o  oooo  oooo  
       `888 `888'   `Y8b          d8P'    `Y8                     `888         `"'  `888  `888  
        888  888      888         Y88bo.       .ooooo.   .ooooo.   888  oooo  oooo   888   888  
        888  888      888          `"Y8888o.  d88' `88b d88' `"Y8  888 .8P'   `888   888   888  
        888  888      888 8888888      `"Y88b 888ooo888 888        888888.     888   888   888  
        888  888     d88'         oo     .d8P 888    .o 888   .o8  888 `88b.   888   888   888  
    .o. 88P o888bood8P'           8""88888P'  `Y8bod8P' `Y8bod8P' o888o o888o o888o o888o o888o 
    `Y888P                                                                                                                                                  
                                               
功能列表：                                                                                
 1.预约商品
 2.秒杀抢购商品
    """
    print(a)

    jd_seckill = JdSeckill()
    choice_from_arg = get_choice_from_arg()
    choice_function = choice_from_arg if choice_from_arg else input('请选择:')
    if choice_function == '1':
        jd_seckill.reserve()
    elif choice_function == '2':
        jd_seckill.seckill_by_proc_pool()
    else:
        print('没有此功能')
        sys.exit(1)

