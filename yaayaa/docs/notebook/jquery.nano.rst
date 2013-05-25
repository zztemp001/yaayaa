jquery.nano.js - 小巧可爱的json渲染引擎
====================================

基础用法
-------

假设有以下json数据 ::

    data = {
      user: {
        login: "tomek",
        first_name: "Thomas",
        last_name: "Mazur",
        account: {
          status: "active",
          expires_at: "2009-12-31"
        }
      }
    }

使用以下模板进行包装 ::

  $.nano("&lt;p&gt;Hello {user.first_name} {user.last_name}! Your account is &lt;strong&gt;{user.account.status}&lt;/strong&gt;&lt;/p&gt;", data)

渲染结果将会是 ::

  &lt;p&gt;Hello Thomas! Your account is &lt;strong&gt;active&lt;/strong&gt;&lt;/p&gt;

**很简单的模板，好用，可以提前做一些bootstrap的模板**


一个获取twitter数据并渲染的例子： http://jsfiddle.net/UXZDy/1/
