try:
    from .core import MaximumFlow as CMaximumFlow
    from .core import MinimumCostFlow as CMinimumCostFlow
    from .core import BaseNetwork as CBaseNetwork
except Exception as e:
    import sys

    """
    在调用 setup.py 的时候需要读取 flow_network.__version__
    于是 flow_network.__init__.py 会被同时调用，然后一直执行到这里
    但在调用 setup.py 的时候 core.i 还没被编译成 _core
    所以在这里 mock 一些 _core 里面的对象，否则会报错
    """
    if 'setup.py' in sys.argv:
        CMaximumFlow = CMinimumCostFlow = CBaseNetwork = None
    else:
        print(f'sys.argv = {sys.argv}')
        raise e
