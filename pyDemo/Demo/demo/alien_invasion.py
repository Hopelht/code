import sys  # 玩家退出时，使用模块sys退出游戏
import pygame
from .testww import tse    #记住引用模块的写法


def run_game():
    # 初始化游戏并创建一个频幕对象
    pygame.init()  # 初始化背景设置
    screen = pygame.display.set_mode((1000, 600))  # 创建显示窗口，并指定了游戏窗口的尺寸px，注意使用了两个括号
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 玩家单击游戏窗口关闭按钮时检测到
                sys.exit()

        # 不断更新屏幕，让最近绘制的屏幕可见
        pygame.display.flip()


run_game()