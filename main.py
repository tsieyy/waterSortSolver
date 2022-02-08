from model import Cups
from solver.solver import Solver
from util import env
from adbConnector.Connector import Connector
from openCVParser import cvParser
import time
# test data
# 把试管抽象为一个特殊的栈(直接用数组来代替，因为数组就有append pop方法，将数组的尾部作为栈顶即试管顶部)
# 将颜色抽象为数字
test_waters = [
    [1, 2, 3, 4],
    [5, 4, 6, 1],
    [1, 7, 2, 8],
    [3, 8, 8, 5],
    [7, 9, 9, 3],
    [1, 8, 6, 2],
    [2, 9, 4, 5],
    [7, 6, 9, 6],
    [3, 5, 7, 4],
    [],
    []
]

envmanager = env.EnvManager()
cups = Cups.Cups(test_waters)


def initEnv():
    if not envmanager.checkAdbEnv():
        envmanager.setAdbEnv()
    Connector.connect()


if __name__ == '__main__':
    # 初始化环境
    initEnv()

    # 截图
    Connector.screencap()

    # 解析数据
    data,pos = cvParser.parse()

    cups = Cups.Cups(data)

    # 进行求解
    Solver.sort(cups)

    # 输出求解答案
    Solver.output(test_waters)

    for action in Solver.res:
        Connector.tap(pos[action[0]][0],pos[action[0]][1])
        time.sleep(1)
        Connector.tap(pos[action[1]][0],pos[action[1]][1])
        time.sleep(1)
