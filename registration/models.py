from django.db import models
from sparrow_admin.models import SchoolsModel


# Create your models here.
class ParentsModel(models.Model):
    """"""
    TITLE = (
        ('MR', 'MR'), ('MRS', 'MRS'), ('MISS', 'MISS'), ('MS', 'MS'),   ('DOC', 'DOC'),
        ('BARR', 'BARR'), ('PST', 'PST'), ('PROF', 'PROF'),  ('ENGR', 'ENGR'),
    )
    title = models.CharField(max_length=10, choices=TITLE)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    image = models.FileField(blank=True, null=True, upload_to='images/parent_images')
    residential_address = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True,)
    email = models.CharField(max_length=100, null=True, blank=True)
    office_address = models.CharField(max_length=200, null=True, blank=True)
    office_mobile = models.CharField(max_length=20, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    RELIGION = (
        ('CHRISTIANITY', 'CHRISTIANITY'), ('ISLAM', 'ISLAM'), ('OTHERS', 'OTHERS')
    )
    religion = models.CharField(max_length=20, choices=RELIGION, null=True, blank=True)
    nationality = models.CharField(max_length=100, default='Nigerian')
    STATE_OF_ORIGIN = (
        ('ab', 'ABIA'), ('an', 'ANAMBRA'), ('be', 'BENUE'), ('cr', 'CROSS RIVER'),
    )
    LGA = (
         ('ab', 'ABIA'), ('an', 'ANAMBRA'), ('be', 'BENUE'), ('cr', 'CROSS RIVER'),
    )
    state_of_origin = models.CharField(max_length=50, choices=STATE_OF_ORIGIN, blank=True, null=True)
    lga = models.CharField(max_length=50, choices=LGA, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=15, blank=True, default='active')
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)

    def __str__(self):
        if self.middle_name:
            return self.title + ' ' + self.surname + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.title + ' ' + self.surname + ' ' + self.last_name


class StaffModel(models.Model):
    """"""
    TITLE = (
        ('MR', 'MR'), ('MRS', 'MRS'), ('MISS', 'MISS'), ('MS', 'MS'),   ('DOC', 'DOC'),
        ('BARR', 'BARR'), ('PST', 'PST'), ('PROF', 'PROF'),  ('ENGR', 'ENGR'),
    )
    title = models.CharField(max_length=10, choices=TITLE)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True, default='')
    last_name = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/staff_images', blank=True, null=True)
    residential_address = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    SECTION = (
        ('a', 'Academic'), ('n', 'Non Academic')
    )
    POSITION = (
        ('', '----------'), ('TEACHER', 'TEACHER'), ('LAB ATTENDANT', 'LAB ATTENDANT'), ('PSYCHOLOGIST', 'PSYCHOLOGIST'),
        ('NANNY', 'NANNY'), ('PRINCIPAL', 'PRINCIPAL'), ('VICE PRINCIPAL ACADEMIC', 'VICE PRINCIPAL ACADEMIC'),
        ('VICE PRINCIPAL ADMINISTRATION', 'VICE PRINCIPAL ADMINISTRATION'), ('DIRECTOR', 'DIRECTOR'),
        ('PROPRIETOR', 'PROPRIETOR'), ('ACCOUNTANT', 'ACCOUNTANT'), ('BURSARY', 'BURSARY'), ('REGISTRAR', 'REGISTRAR'),
        ('RECEPTIONIST', 'RECEPTIONIST'), ('ICT', 'ICT'), ('CHIEF SECURITY OFFICER', 'CHIEF SECURITY OFFICER'),
        ('SECURITY OFFICER', 'SECURITY OFFICER'), ('CHEF', 'CHEF'), ('OTHERS', 'OTHERS')
    )
    section = models.CharField(max_length=20, choices=SECTION)
    position = models.CharField(max_length=100, choices=POSITION)
    salary = models.BigIntegerField(blank=True, null=True)
    registration_number = models.CharField(max_length=50,  blank=True, null=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    RELIGION = (
        ('CHRISTIANITY', 'CHRISTIANITY'), ('ISLAM', 'ISLAM'), ('OTHERS', 'OTHERS')
    )
    GENDER = (
        ('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')
    )
    religion = models.CharField(max_length=20, choices=RELIGION,  blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    nationality = models.CharField(max_length=100, default='Nigerian')
    STATE_OF_ORIGIN = (
         ('ab', 'ABIA'), ('ANAMBRA', 'ANAMBRA'), ('be', 'BENUE'), ('cr', 'CROSS RIVER'),
    )
    LGA = (
         ('ab', 'ABIA'), ('an', 'ANAMBRA'), ('be', 'BENUE'), ('cr', 'CROSS RIVER'),
    )
    state_of_origin = models.CharField(max_length=50, choices=STATE_OF_ORIGIN, blank=True, null=True)
    lga = models.CharField(max_length=50, choices=LGA, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, default='active')
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)

    def __str__(self):
        if self.middle_name:
            return self.surname + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.surname + ' ' + self.last_name


class ClassesModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25)
    subjects = models.ManyToManyField(to='basic.SubjectsModel', blank=True)
    form_teacher = models.ForeignKey(StaffModel, null=True, blank=True, on_delete=models.SET_NULL)
    assistant_form_teacher = models.ForeignKey(StaffModel, related_name='assistant_form_teacher', null=True, blank=True, on_delete=models.SET_NULL)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)
    publish_result = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StudentsModel(models.Model):
    """"""
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='images/student_images')
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    RELATIONSHIP_WITH_PARENT = (
        ('father', 'FATHER'), ('mother', 'MOTHER'), ('sister', 'SISTER'), ('brother', 'BROTHER'), ('uncle', 'UNCLE'),
        ('aunty', 'AUNTY'), ('pastor', 'PASTOR'), ('others', 'OTHERS')
    )
    GENDER = (
        ('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    relationship_with_parent = models.CharField(max_length=20, choices=RELATIONSHIP_WITH_PARENT)
    RELIGION = (
         ('CHRISTIANITY', 'CHRISTIANITY'), ('ISLAM', 'ISLAM'), ('OTHERS', 'OTHERS')
    )
    religion = models.CharField(max_length=20, choices=RELIGION, blank=True, null=True)
    nationality = models.CharField(max_length=50, default='Nigerian', blank=True, null=True)
    STATE_OF_ORIGIN = (
         ('ab', 'ABIA'), ('an', 'ANAMBRA'), ('be', 'BENUE'), ('cr', 'CROSS RIVER'),
    )
    LGA = (
        ('ab', 'ABIA'), ('an', 'ANAMBRA'), ('be', 'BENUE'), ('cr', 'CROSS RIVER'),
    )
    state_of_origin = models.CharField(max_length=50, choices=STATE_OF_ORIGIN, blank=True, null=True)
    lga = models.CharField(max_length=50, choices=LGA, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    student_class = models.ForeignKey(ClassesModel, null=True, on_delete=models.CASCADE, related_name='class_student')
    status = models.CharField(max_length=15, blank=True, default='active')
    previous_classes = models.JSONField(null=True, blank=True)
    parent = models.ForeignKey(ParentsModel, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)
    # results = models.ForeignKey(TermResult, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.middle_name:
            return self.surname + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.surname + ' ' + self.last_name
