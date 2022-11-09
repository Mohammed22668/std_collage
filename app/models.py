
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

########################################################################
class Department(models.Model):
    Dname = models.CharField(max_length=100,verbose_name="القسم")

    
    def __str__(self):
        return self.Dname
    
    class Meta:
        verbose_name_plural = "الاقسام العلمية"
    
#############################################################################    

class City(models.Model):
    Cname = models.CharField(max_length=100,verbose_name="المحافظة")
    
    
    def __str__(self):
        return self.Cname
    
    class Meta:
        verbose_name_plural = "المحافظات"
    

######################################################################    
    

class StudentDocument(models.Model):
    user = models.CharField(max_length=100,verbose_name="اسم المستخدم")
    name = models.CharField(max_length=100,verbose_name="اسم الطالب/ة" )
    Dname = models.CharField(max_length=100,verbose_name="القسم")
    Cname = models.CharField(max_length=100,verbose_name="المحافظة")
    graduate_year = models.CharField(max_length=100,verbose_name="سنة التخرج")
    to = models.CharField(max_length=250 , verbose_name="الجهة المصدر اليها")
    Dnumber = models.CharField(max_length=20,verbose_name="رقم الوثيقة")
    Ddate = models.DateField(verbose_name="تاريخ الوثيقة",blank=True,null=True)
    note = models.TextField(blank=True,null=True)
    check_post = models.BooleanField(blank=True,null=True,default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "جدول وثائق الطلبة"
    
# Department,on_delete=models.PROTECT,    
# City,on_delete=models.PROTECT

################################# User Profile  #####################################################
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT,verbose_name="اسم المستخدم")
    Dname = models.ForeignKey(Department,on_delete=models.PROTECT,verbose_name="القسم")
    Cname = models.ForeignKey(City,on_delete=models.PROTECT,verbose_name="المحافظة")
    
    
    def __str__(self):
        return str(self.user)  +" / "+ str(self.Dname) +" / "+str(self.Cname)
    
    class Meta:
        verbose_name_plural = "بروفايل المستخدمين"
    
    
################################ Status for students ##################################################

class StudentStatus(models.Model):
    state_list = (
        ("استضافة","استضافة"),
        ("نقل", "نقل"),
        ("تأجيل", "تأجيل"),
        ("رسوب", "رسوب"),
        ("ترقين قيد", "ترقين قيد"),
    )
    stage_list = (
        ("الاولى", "الاولى"),
        ("الثانية", "الثانية"),
        ("الثالثة", "الثالثة"),
        ("الرابعة", "الرابعة"),
        
    )
    study_list = (
        ("الصباحية", "الصباحية"),
        ("المسائية", "المسائية"),
       
       

    )
    user = models.CharField(max_length=100, verbose_name="اسم المستخدم")
    name = models.CharField(max_length=100, verbose_name="اسم الطالب/ة")
    Dname = models.CharField(max_length=100, verbose_name="القسم")
    Cname = models.CharField(max_length=100, verbose_name="المحافظة")
    stage = models.CharField(max_length=50, verbose_name="المرحلة", choices=stage_list)
    state = models.CharField(max_length=100, verbose_name="حالة الطالب",choices=state_list)
    year = models.CharField(max_length=50, verbose_name="العام الدراسي")
    study = models.CharField(max_length=20,verbose_name="الدراسة", choices=study_list,null=True)
    note = models.TextField(blank=True, null=True, verbose_name="الملاحظات")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "حالات الطلبة"
        
        
        
####################### Notifications class  #####################################        
class Notifications(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان")
    Dname = models.ForeignKey(Department,verbose_name="القسم",on_delete=models.PROTECT)
    Cname = models.ForeignKey(City, verbose_name="المحافظة", on_delete=models.PROTECT)
    get_from = models.CharField(max_length=200, verbose_name="الجهة")
    year = models.CharField(max_length=200, verbose_name="العام الدراسي")
    date = models.DateField(verbose_name="تاريخ التنفيذ", null=True, blank=True)
    note = models.TextField(verbose_name="الملاحظات", null=True, blank=True)
    file = models.FileField(upload_to='files/%y/%m',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='التعميم/الاشعارات'
        
    
###########################################################
class TasjilDocuments(models.Model):
    list_study = (
        ("الصباحية","الصباحية"),
        ("المسائية","المسائية"),
    )
    list_type = (
        ("وثيقة بالدرجات","وثيقة بالدرجات"),
        ("وثيقة بالتسلسل","وثيقة بالتسلسل"),
        ("وثيقة بالمعدل","وثيقة بالمعدل"),
    )
    name = models.CharField(max_length=200, verbose_name="الاسم")
    Dname = models.ForeignKey(Department,on_delete=models.PROTECT,verbose_name="القسم")  
    Cname = models.ForeignKey(City,on_delete=models.PROTECT,verbose_name="المحافظة")
    study = models.CharField(max_length=50,verbose_name="الدراسة",choices=list_study)
    year_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    to = models.CharField(max_length=300,verbose_name="الجهة/الى")
    docType = models.CharField(max_length=50,verbose_name="نوع الوثيقة",choices=list_type)
    note = models.TextField(null=True,blank=True)
    img = models.ImageField(upload_to="TasjilDocument/%y/%m",null=True,blank=True)
    
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "وثائق التسجيل العام"
        
        
            
    
    
       



############################################################
class Patient(models.Model):
    Gender=(
        ('F','F'),
        ('M','M'),
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,null=True,choices=Gender)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
