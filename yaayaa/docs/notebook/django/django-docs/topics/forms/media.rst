Form Media
==========

Rendering an attractive and easy-to-use Web form requires more than just
HTML - it also requires CSS stylesheets, and if you want to use fancy
"Web2.0" widgets, you may also need to include some JavaScript on each
page. The exact combination of CSS and JavaScript that is required for
any given page will depend upon the widgets that are in use on that page.

创建易用而引人注目的 Web 表单，单纯依靠纯 HTML 已经不够 - 还需要 CSS 样式表。如果
你还需要创建一些酷炫的 Web 2.0 部件，则还需要一些 javascript 。

This is where Django media definitions come in. Django allows you to
associate different media files with the forms and widgets that require
that media. For example, if you want to use a calendar to render DateFields,
you can define a custom Calendar widget. This widget can then be associated
with the CSS and JavaScript that is required to render the calendar. When
the Calendar widget is used on a form, Django is able to identify the CSS and
JavaScript files that are required, and provide the list of file names
in a form suitable for easy inclusion on your Web page.

这就是 Django media 的意义。Django 允许你将不同的 media 文件和相应的表单、部件关联起来。
例如：你打算通过一个日历部件来表示 DateFields， 你可以自定义一个日历部件。在这个部件中，
你可以将一些 CSS 样式表和 Javascript 关联起来。当这个日历部件在表单中被使用时，
Django 能够辨认出到底需要哪些 CSS 样式表和 Javascript，并且提供相关的文件列表，以便于
这些部件正常使用。

.. admonition:: Media 和 Django Admin

    The Django Admin application defines a number of customized widgets
    for calendars, filtered selections, and so on. These widgets define
    media requirements, and the Django Admin uses the custom widgets
    in place of the Django defaults. The Admin templates will only include
    those media files that are required to render the widgets on any
    given page.

    Django 的 Admin 应用程序定义了一些自定义的部件，比如：日历、筛选，等等。
    这些部件定义了到底需要哪些 media。Django Admin 在需要的地方使用了这些部件。
    Admin 的模板中，只有被需要的 media 文件会被使用。

    If you like the widgets that the Django Admin application uses,
    feel free to use them in your own application! They're all stored
    in ``django.contrib.admin.widgets``.

    如果你喜欢 Django Admin 自带部件，你也可以在自己的应用中使用。这些部件在
    ``django.contrib.admin.widgets`` 中定义。

.. admonition:: 选择哪一个 JavaScript 库？

    Many JavaScript toolkits exist, and many of them include widgets (such
    as calendar widgets) that can be used to enhance your application.
    Django has deliberately avoided blessing any one JavaScript toolkit.
    Each toolkit has its own relative strengths and weaknesses - use
    whichever toolkit suits your requirements. Django is able to integrate
    with any JavaScript toolkit.

    有很多的 Javascript 库，它们各有优缺点。你可以根据需要选择，Django 可以整合任何的
    Javascript 库。

.. _media-as-a-static-definition:

静态定义 Media
-------------

The easiest way to define media is as a static definition. Using this method,
the media declaration is an inner class. The properties of the inner class
define the media requirements.

最简单的定义 Media 的方法是进行静态定义。这种方法通过内部类来声明 media，通过内部类的属性
来定义需要哪些 media。

以下是一个例子 ::

    class CalendarWidget(forms.TextInput):
        class Media:
            css = {
                'all': ('pretty.css',)
            }
            js = ('animations.js', 'actions.js')

This code defines a ``CalendarWidget``, which will be based on ``TextInput``.
Every time the CalendarWidget is used on a form, that form will be directed
to include the CSS file ``pretty.css``, and the JavaScript files
``animations.js`` and ``actions.js``.

这段代码在 ``TextInput`` 部件的基础上，定义了一个 ``CalendarWidget`` 部件，当这个日历
部件每一次被使用时，表单将能直接包含 ``pretty.css`` 样式表和 JavaScript 文件
``animations.js`` 和 ``action.js`` 。

This static media definition is converted at runtime into a widget property
named ``media``. The media for a CalendarWidget instance can be retrieved
through this property.

这些 media 定义将在运行时转化为部件的 ``media`` 属性，可以通过这个属性取回该部件的 media ::

    >>> w = CalendarWidget()
    >>> print(w.media)
    <link href="http://static.example.com/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://static.example.com/animations.js"></script>
    <script type="text/javascript" src="http://static.example.com/actions.js"></script>

Here's a list of all possible ``Media`` options. There are no required options.

``css``
~~~~~~~

A dictionary describing the CSS files required for various forms of output
media.

一个用于描述部件所需 CSS 样式表文件的 ``dict`` 。

The values in the dictionary should be a tuple/list of file names. See
:ref:`the section on media paths <form-media-paths>` for details of how to
specify paths to media files.

字典中的取值应该是一个 ``tuple`` 或是 ``list``，列表中的项目是文件。
请参照 :ref:`media 路径 <form-media-paths>` 获得配置路径和 media 文件的详细信息。

The keys in the dictionary are the output media types. These are the same
types accepted by CSS files in media declarations: 'all', 'aural', 'braille',
'embossed', 'handheld', 'print', 'projection', 'screen', 'tty' and 'tv'. If
you need to have different stylesheets for different media types, provide
a list of CSS files for each output medium. The following example would
provide two CSS options -- one for the screen, and one for print.

字典中的键用于指定输入 media 的用途类型，与 CSS 样式表中的声明类型一样，包括： 'all', 'aural',
'braille', 'embossed', 'handheld', 'print', 'projecttion', 'screen', 'tty' 和 'tv'。
如果需要为不同用途类型指定不同的 CSS 样式表，可通过以下形式来定义。下面的例子定义了两个 CSS 样式表，
一个用于 screen，一个用于 print ::

    class Media:
        css = {
            'screen': ('pretty.css',),
            'print': ('newspaper.css',)
        }

If a group of CSS files are appropriate for multiple output media types,
the dictionary key can be a comma separated list of output media types.
In the following example, TV's and projectors will have the same media
requirements::

    class Media:
        css = {
            'screen': ('pretty.css',),
            'tv,projector': ('lo_res.css',),
            'print': ('newspaper.css',)
        }

If this last CSS definition were to be rendered, it would become the following HTML::

    <link href="http://static.example.com/pretty.css" type="text/css" media="screen" rel="stylesheet" />
    <link href="http://static.example.com/lo_res.css" type="text/css" media="tv,projector" rel="stylesheet" />
    <link href="http://static.example.com/newspaper.css" type="text/css" media="print" rel="stylesheet" />

``js``
~~~~~~

A tuple describing the required JavaScript files. See :ref:`the section on
media paths <form-media-paths>` for details of how to specify paths to media
files.

``extend``
~~~~~~~~~~

A boolean defining inheritance behavior for media declarations.

用于指定是否继承父类的 media 定义。

By default, any object using a static media definition will inherit all the
media associated with the parent widget. This occurs regardless of how the
parent defines its media requirements. For example, if we were to extend our
basic Calendar widget from the example above.

缺省情况下，定义的部件将自动继承父类（上一级部件）的 media 定义。以下例子定义的新部件，
将拥有上一级部件 ``CalendarWidget`` 的 media 定义 ::

    >>> class FancyCalendarWidget(CalendarWidget):
    ...     class Media:
    ...         css = {
    ...             'all': ('fancy.css',)
    ...         }
    ...         js = ('whizbang.js',)

    >>> w = FancyCalendarWidget()
    >>> print(w.media)
    <link href="http://static.example.com/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <link href="http://static.example.com/fancy.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://static.example.com/animations.js"></script>
    <script type="text/javascript" src="http://static.example.com/actions.js"></script>
    <script type="text/javascript" src="http://static.example.com/whizbang.js"></script>

The FancyCalendar widget inherits all the media from it's parent widget. If
you don't want media to be inherited in this way, add an ``extend=False``
declaration to the media declaration.

如果你不想继承，则可以声明 ``extend=False`` ::

    >>> class FancyCalendarWidget(CalendarWidget):
    ...     class Media:
    ...         extend = False
    ...         css = {
    ...             'all': ('fancy.css',)
    ...         }
    ...         js = ('whizbang.js',)

    >>> w = FancyCalendarWidget()
    >>> print(w.media)
    <link href="http://static.example.com/fancy.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://static.example.com/whizbang.js"></script>

If you require even more control over media inheritance, define your media
using a :ref:`dynamic property <dynamic-property>`. Dynamic properties give
you complete control over which media files are inherited, and which are not.

.. _dynamic-property:

Media as a dynamic property
---------------------------

If you need to perform some more sophisticated manipulation of media
requirements, you can define the media property directly. This is done
by defining a widget property that returns an instance of ``forms.Media``.
The constructor for ``forms.Media`` accepts ``css`` and ``js`` keyword
arguments in the same format as that used in a static media definition.

For example, the static media definition for our Calendar Widget could
also be defined in a dynamic fashion::

    class CalendarWidget(forms.TextInput):
        def _media(self):
            return forms.Media(css={'all': ('pretty.css',)},
                               js=('animations.js', 'actions.js'))
        media = property(_media)

See the section on `Media objects`_ for more details on how to construct
return values for dynamic media properties.

.. _form-media-paths:

Paths in media definitions
--------------------------

Paths used to specify media can be either relative or absolute. If a path
starts with ``/``, ``http://`` or ``https://``, it will be interpreted as an
absolute path, and left as-is. All other paths will be prepended with the value
of the appropriate prefix.

As part of the introduction of the
:doc:`staticfiles app </ref/contrib/staticfiles>` two new settings were added
to refer to "static files" (images, CSS, Javascript, etc.) that are needed
to render a complete web page: :setting:`STATIC_URL` and :setting:`STATIC_ROOT`.

To find the appropriate prefix to use, Django will check if the
:setting:`STATIC_URL` setting is not ``None`` and automatically fall back
to using :setting:`MEDIA_URL`. For example, if the :setting:`MEDIA_URL` for
your site was ``'http://uploads.example.com/'`` and :setting:`STATIC_URL`
was ``None``::

    >>> class CalendarWidget(forms.TextInput):
    ...     class Media:
    ...         css = {
    ...             'all': ('/css/pretty.css',),
    ...         }
    ...         js = ('animations.js', 'http://othersite.com/actions.js')

    >>> w = CalendarWidget()
    >>> print(w.media)
    <link href="/css/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://uploads.example.com/animations.js"></script>
    <script type="text/javascript" src="http://othersite.com/actions.js"></script>

But if :setting:`STATIC_URL` is ``'http://static.example.com/'``::

    >>> w = CalendarWidget()
    >>> print(w.media)
    <link href="/css/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://static.example.com/animations.js"></script>
    <script type="text/javascript" src="http://othersite.com/actions.js"></script>


Media objects
-------------

When you interrogate the media attribute of a widget or form, the value that
is returned is a ``forms.Media`` object. As we have already seen, the string
representation of a Media object is the HTML required to include media
in the ``<head>`` block of your HTML page.

However, Media objects have some other interesting properties.

Media subsets
~~~~~~~~~~~~~

If you only want media of a particular type, you can use the subscript operator
to filter out a medium of interest. For example::

    >>> w = CalendarWidget()
    >>> print(w.media)
    <link href="http://static.example.com/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://static.example.com/animations.js"></script>
    <script type="text/javascript" src="http://static.example.com/actions.js"></script>

    >>> print(w.media)['css']
    <link href="http://static.example.com/pretty.css" type="text/css" media="all" rel="stylesheet" />

When you use the subscript operator, the value that is returned is a new
Media object -- but one that only contains the media of interest.

Combining media objects
~~~~~~~~~~~~~~~~~~~~~~~

Media objects can also be added together. When two media objects are added,
the resulting Media object contains the union of the media from both files::

    >>> class CalendarWidget(forms.TextInput):
    ...     class Media:
    ...         css = {
    ...             'all': ('pretty.css',)
    ...         }
    ...         js = ('animations.js', 'actions.js')

    >>> class OtherWidget(forms.TextInput):
    ...     class Media:
    ...         js = ('whizbang.js',)

    >>> w1 = CalendarWidget()
    >>> w2 = OtherWidget()
    >>> print(w1.media + w2.media)
    <link href="http://static.example.com/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://static.example.com/animations.js"></script>
    <script type="text/javascript" src="http://static.example.com/actions.js"></script>
    <script type="text/javascript" src="http://static.example.com/whizbang.js"></script>

Media on Forms
--------------

Widgets aren't the only objects that can have media definitions -- forms
can also define media. The rules for media definitions on forms are the
same as the rules for widgets: declarations can be static or dynamic;
path and inheritance rules for those declarations are exactly the same.

Regardless of whether you define a media declaration, *all* Form objects
have a media property. The default value for this property is the result
of adding the media definitions for all widgets that are part of the form::

    >>> class ContactForm(forms.Form):
    ...     date = DateField(widget=CalendarWidget)
    ...     name = CharField(max_length=40, widget=OtherWidget)

    >>> f = ContactForm()
    >>> f.media
    <link href="http://static.example.com/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://static.example.com/animations.js"></script>
    <script type="text/javascript" src="http://static.example.com/actions.js"></script>
    <script type="text/javascript" src="http://static.example.com/whizbang.js"></script>

If you want to associate additional media with a form -- for example, CSS for form
layout -- simply add a media declaration to the form::

    >>> class ContactForm(forms.Form):
    ...     date = DateField(widget=CalendarWidget)
    ...     name = CharField(max_length=40, widget=OtherWidget)
    ...
    ...     class Media:
    ...         css = {
    ...             'all': ('layout.css',)
    ...         }

    >>> f = ContactForm()
    >>> f.media
    <link href="http://static.example.com/pretty.css" type="text/css" media="all" rel="stylesheet" />
    <link href="http://static.example.com/layout.css" type="text/css" media="all" rel="stylesheet" />
    <script type="text/javascript" src="http://static.example.com/animations.js"></script>
    <script type="text/javascript" src="http://static.example.com/actions.js"></script>
    <script type="text/javascript" src="http://static.example.com/whizbang.js"></script>
