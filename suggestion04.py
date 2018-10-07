# coding: utf-8
"""
建议4：在代码中适当添加注释

在代码里面适当的添加注释，避免以下情况：
1，代码即注释，也就是不写注释
2，注释与代码重复，注释应该是用来解释代码的功能，原因以及想法的，而不是对代码本身的解释
3，利用注释语法快速删除代码，对于不再需要的代码，应该将其删除，而不是将其注释掉，即使你担心以后还会用到，版本控制工具也可以让你轻松的找回
4，代码不断更新而注释却没有更新；
5，注释比代码本身还复杂烦琐；
6，将别处的注释和代码一起拷贝过来，但上下文的变更导致注释与代码不同步；
7，将注释当做自己的娱乐空间从而留下个性特征等。
"""


# 给外部可访问的函数和方法（无论是否简单）添加文档注释。注释要清楚地描述方法的功能，并对
# 参数，返回值以及可能发生的异常进行说明，使得外部调用它的人员仅仅看docstring就能正确使用。
def FuncName(param1, param2):
    """
    Describe what this function does.
    # such as "Find whether the special string is in queue or not"
    Args:
        param1: param type, what is this param used for.
            # such as strqueue: str, str queue list for search
        param2: param type, what is this param used for.
            # such as str: str, str to find
    Returns:
        return type, return value.
        # such as boolean, special str     found return True, else return False
    """
    pass
