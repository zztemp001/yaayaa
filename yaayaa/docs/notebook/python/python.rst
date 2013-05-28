python 语言文档
**************

读取系统变量
==========

.. code-block:: python

    import os

    env_var = os.environ.get("VAR_NAME")
    print env_var
