from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=70)
    class Sex(models.IntegerChoices):
        Male = 1,('male')
        Female = 2,('female')
        Other = 3,('other')
    sex = models.IntegerField(choices = Sex.choices)
        
    def __str__(self):
        return self.full_name

class Homework(models.Model):
    commit_date = models.DateField(auto_now=True)
    headline = models.CharField(max_length=200)#字段最长200,这里可以根据需要更改
    attach = models.FileField()
    remark = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
        #教程的第一步，定义好model文件
        #目的是为了通过简单的命令完成数据库的创建
        '''
        在此，我们在Article中定义了四个属性
        其中第一个是日期，第二个则规定了文本，字段最长200
        第三个则定义了文章的主体，最后加了一个外码，指向reporter，
        对应reporter中的记者表'''

