django 概览
***********

models
======

基本应用 ::

    from geography.models import ZipCode    # 可以跨文件引用 models

    class Human(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        gentle = models.BooleanField()

        class Meta:
            # 作为基类，通过声明 abstract=True 来避免为其生成数据表
            abstract = True
            orderging = ['last_name']

    class Musician(Human):
        # 继承自 Human，增加一些属性
        instrument = models.CharField(max_length=100)

        class Meta:
            verbose_name = u'音乐家'   # 子类将会继承父类 Human 的 Meta 属性，abstract 除外

        def __unicode__(self):
            return self.first_name + self.last_name

    class Tag(models.Model):
        tag_name = models.CharField(max_length=50)
        tag_date = models.models.DateField()

        def __unicode__(self):
            return self.tag_name

    class Album(models.Model):
        PACKAGE_SIZES = (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
        )
        artist = models.ForeignKey(Musician, verbose_name=u"专辑音乐家")
        name = models.CharField(max_length=100)
        release_date = models.DateField()
        num_stars = models.IntegerField()
        package_size = models.CharField(max_length=2, choices=PACKAGE_SIZES)
        tag = models.ManyToManyField(Tag)
        zipcode = models.ForeinKey(ZipCode) # 可与外部文件的数据表建立联系

        Class Meta:
            ordering = ['release_date']
            verbose_name_plural = u'专辑大全'

        # 个性化 save 操作，也可以使用 signal 来实现
        def save(self, *args, **kwargs):
            if self.name == u"飞扬音乐":
                return # 用户不能以“飞扬音乐”为名建立专辑
            else:
                do_something()
                super(Blog, self).save(*args, **kwargs) # 调用真正的 save 动作
                do_something_else()

        def __unicode__(self):
            return self.name

        def album_age_status(self):
            # 返回专辑所属年代
            import datetime
            if self.release_date < datetime.date(1945, 8, 1):
                return u'怀旧'
            elif self.release_date < datetime.date(1965, 1, 1):
                return u"经典"
            else:
                return u"现代"

        def is_recommend(self):
            # 返回专辑是否属于推荐的
            return self.name in (u'张学友', u'王菲', u'老狼')

        def _get_musician_full_name(self):
            # 内部函数，返回专辑音乐家的全名
            return '%s %s' % (self.artist.first_name, self.artist.last_name)
        musician_full_name = property(_get_musician_full_name)  # 定义一个属性 musician_full_name

    # 字段名不能包含 python 保留关键字，如 pass 等
    # 字段名不能包含双下划线，这会与 django 的查找形式冲突
    # Meta 可以是任何非字段的定义
    # 如果在父类中为 ForeignKey 和 ManyToMany 设置了 related_name
    # 则需要在任何子类中都要设置一个 unique 的 related_name，以免发生冲突

contrib
=======

