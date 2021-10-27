from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField




class Classification(models.Model):

    cname = models.CharField(max_length=128,verbose_name='数据分类')


    def __str__(self):
        return self.cname



    class Meta:
        verbose_name = "数据分类"
        verbose_name_plural = "数据分类"




class Tag_name(models.Model):

    tname=models.CharField(max_length=128,verbose_name="数据标签")



    def __str__(self):
        return self.tname



    class Meta:
        verbose_name = "数据标签"
        verbose_name_plural = "数据标签"





class My_data(models.Model):

    title = models.CharField(max_length=128,verbose_name='标题')
    # author = models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE)
    body = RichTextUploadingField(verbose_name='正文')
    img = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name='配图')
    abstract = models.TextField(max_length=256,blank=True,null=True,verbose_name='摘要')
    visiting = models.PositiveIntegerField(default=0,verbose_name='访问量')
    category = models.ManyToManyField('Classification',verbose_name='分类')
    tags = models.ManyToManyField('Tag_name',verbose_name='标签')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创造时间')
    modified_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')



    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('MY_Data:data_detail', kwargs={'pk': self.pk})

    def increase_visiting(self):
        self.visiting+=1
        self.save(update_fields=['visiting'])



    class Meta:
        ordering=['-created_time']
        verbose_name = "我的数据"
        verbose_name_plural = '我的数据'
