# Care Learning
## Day 1
- 搭好 WSL2+Ubuntu 环境,建虚拟环境,完成 git 首次提交
- 学到:Linux 命令基础、venv 隔离、git 工作流
## Day 2
- 完成 wordcount.py:文件读取、字典计数、排序、Top N 输出
- 学到:字典/循环/切片/f-string/sorted,把C式for切换成Python式
## Day 3
- 完成 D1-D2 五道练习题:字符统计、成绩分级(含 json 读文件)、词频统计升级(小写/过滤/去标点)、去重统计、文本分析器
- 完成 D3:check.py(交互式判断)、guess.py + guess2.py(猜数字游戏,含次数限制与输入校验)、comprehension.py(列表推导式)
- 学到:
  - 控制流:if/elif/else 的兜底设计、and/or/not、链式比较、while 循环、break 与 continue 的区别
  - 交互:input() 返回的永远是字符串,必须显式转换;用 isdigit() 校验输入,配合 continue 让无效输入不消耗次数
  - 列表推导式:[表达式 for 元素 in 集合 if 条件],第一个位置不能空
  - 类型意识:字符串 vs 列表 vs 集合,遍历它们拿到的东西完全不同——这是我今天所有 bug 的共同根源
  - 数据流水线:过滤时机决定结果(要在统计阶段过滤,而非打印阶段);清洗要在使用之前
  - 工程原则:DRY(别重复自己)、避免 magic number、变量命名要能说出内容
  - 读报错三步法:看错误类型 → 看行号 → 把描述翻译成人话