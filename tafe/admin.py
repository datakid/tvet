from tafe.models import Student, Course, Subject, Enrolment, Grade, StaffAttendance, StudentAttendance, Result, Session, Timetable, Applicant, Staff, Credential, Assessment, StaffISLPR, StudentISLPR
from django.contrib import admin
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget 
from django.forms.widgets import RadioSelect

import datetime

today = datetime.date.today()
this_year = datetime.date.today().year
BIRTH_YEARS = range(this_year-51, this_year-15)

class StudentISLPRInline(admin.StackedInline):
    model = StudentISLPR
    extra = 1

class StaffISLPRInline(admin.StackedInline):
    model = StaffISLPR
    extra = 1

class ApplicantInline(admin.TabularInline):
    model = Applicant
    extra = 1

class AssessmentInline(admin.TabularInline):
    model = Assessment 

class CourseInline(admin.TabularInline):
    model = Course

class CredentialInline(admin.TabularInline):
    model = Staff.credential.through
    extra = 1

class EnrolmentInline(admin.TabularInline):
    model = Enrolment 
    extra = 1    

class GradeInline(admin.TabularInline):
    model = Grade
    fields = ('student','date_started','results')

class ResultInline(admin.StackedInline):
    model = Result
    template = 'admin/collapsed_tabular_inline.html'

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1
    fields = ('date', 'session_number','subject','timetable', 'room_number')
    template = 'admin/collapsed_tabular_inline.html'

class StaffAttendanceInline(admin.TabularInline):
    model = StaffAttendance
    exclude = ('slug',)
    extra = 1
    fields = ('staff_member','reason','absent')
    template = 'admin/collapsed_tabular_inline.html'

class StudentAttendanceInline(admin.TabularInline):
    model = StudentAttendance
    fields = ('student','reason','absent')
    exclude = ('slug',)
    template = 'admin/collapsed_tabular_inline.html'

class StudentInline(admin.StackedInline):
    model = Student
    extra = 1

class StaffInline(admin.StackedInline):
    model = Staff

class SubjectInline(admin.StackedInline):
    model = Subject

class ApplicantAdminForm(ModelForm):
    class Meta:
        model = Applicant 
        widgets = {
            'dob': SelectDateWidget(years=BIRTH_YEARS),
            'gender': RadioSelect(),
        }            

class EnglishTestFilter(admin.SimpleListFilter):
    title = 'english test' # human readable, right sidebar
    parameter_name = 'eng-result' # used in URL query

    def lookups(self, request, model_admin):
        '''Note: only show the field if there is someone with a mark in that range'''
        qs = model_admin.queryset(request) # these are the ranges in the right sidebar 
        if qs.filter(test_eng__lt=10).exists():
            yield ('10', '0 - 10')
        if qs.filter(test_eng__gte=10, test_ma__lt=20):
            yield ('20', '10 - 20')
        if qs.filter(test_eng__gte=20, test_eng__lt=30):
            yield ('30', '20 - 30')
        if qs.filter(test_eng__gte=30, test_eng__lt=40):
            yield ('40', '30 - 40')
        if qs.filter(test_eng__gte=40, test_eng__lt=50):
            yield ('50', '40 - 50')
        if qs.filter(test_eng__gte=50, test_eng__lt=60):
            yield ('60', '50 - 60')
        if qs.filter(test_eng__gte=60, test_eng__lt=70):
            yield ('70', '60 - 70')
        if qs.filter(test_eng__gte=70, test_eng__lt=80):
            yield ('80', '70 - 80')
        if qs.filter(test_eng__gte=80, test_eng__lt=90):
            yield ('90', '80 - 90')
        if qs.filter(test_eng__lte=100):
            yield ('100', '90 - 100')

    def queryset(self, request, queryset):
        if self.value() == '10':
            return queryset.filter(test_eng__lt=10)
        if self.value() == '20':
            return queryset.filter(test_eng__gte=10, test_eng__lt=20)
        if self.value() == '30':
            return queryset.filter(test_eng__gte=20, test_eng__lt=30)
        if self.value() == '40':
            return queryset.filter(test_eng__gte=30, test_eng__lt=40)
        if self.value() == '50':
            return queryset.filter(test_eng__gte=40, test_eng__lt=50)
        if self.value() == '60':
            return queryset.filter(test_eng__gte=50, test_eng__lt=60)
        if self.value() == '70':
            return queryset.filter(test_eng__gte=60, test_eng__lt=70)
        if self.value() == '80':
            return queryset.filter(test_eng__gte=70, test_eng__lt=80)
        if self.value() == '90':
            return queryset.filter(test_eng__gte=80, test_eng__lt=90)
        if self.value() == '100':
            return queryset.filter(test_eng__lte=100)

class MathTestFilter(admin.SimpleListFilter):
    title = 'math test' # human readable, right sidebar
    parameter_name = 'math-result' # used in URL query

    def lookups(self, request, model_admin):
        '''Note: only show the field if there is someone with a mark in that range'''
        qs = model_admin.queryset(request)
        if qs.filter(test_ma__lt=10).exists():
            yield ('10', '0 - 10')
        if qs.filter(test_ma__gte=10, test_ma__lt=20):
            yield ('20', '10 - 20')
        if qs.filter(test_ma__gte=20, test_ma__lt=30):
            yield ('30', '20 - 30')
        if qs.filter(test_ma__gte=30, test_ma__lt=40):
            yield ('40', '30 - 40')
        if qs.filter(test_ma__gte=40, test_ma__lt=50):
            yield ('50', '40 - 50')
        if qs.filter(test_ma__gte=50, test_ma__lt=60):
            yield ('60', '50 - 60')
        if qs.filter(test_ma__gte=60, test_ma__lt=70):
            yield ('70', '60 - 70')
        if qs.filter(test_ma__gte=70, test_ma__lt=80):
            yield ('80', '70 - 80')
        if qs.filter(test_ma__gte=80, test_ma__lt=90):
            yield ('90', '80 - 90')
        if qs.filter(test_ma__lte=100):
            yield ('100', '90 - 100')

    def queryset(self, request, queryset):
        if self.value() == '10':
            return queryset.filter(test_ma__lt=10)
        if self.value() == '20':
            return queryset.filter(test_ma__gte=10, test_ma__lt=20)
        if self.value() == '30':
            return queryset.filter(test_ma__gte=20, test_ma__lt=30)
        if self.value() == '40':
            return queryset.filter(test_ma__gte=30, test_ma__lt=40)
        if self.value() == '50':
            return queryset.filter(test_ma__gte=40, test_ma__lt=50)
        if self.value() == '60':
            return queryset.filter(test_ma__gte=50, test_ma__lt=60)
        if self.value() == '70':
            return queryset.filter(test_ma__gte=60, test_ma__lt=70)
        if self.value() == '80':
            return queryset.filter(test_ma__gte=70, test_ma__lt=80)
        if self.value() == '90':
            return queryset.filter(test_ma__gte=80, test_ma__lt=90)
        if self.value() == '100':
            return queryset.filter(test_ma__lte=100)

class IslandFilter(admin.SimpleListFilter):
    title = 'islands'
    parameter_name = 'island'
    
    def lookups(self, request, model_admin):
        return (
            ('tarawa', 'Tarawa'),
            ('outer-islands', 'Outer Islands'),
        )

    def queryset(self, request, queryset):
        if self.value == 'tarawa':
            return queryset.filter(island__iexact='tarawa')
        if self.value == 'outer-islands':
            return queryset.exclude(island__iexact='tarawa')

class ApplicantAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Bio', {'fields':(('first_name','surname'),('dob','gender', 'island'))}),
        ('Contact Information', { 'fields':(('phone', 'phone2', 'email'),)}),
        ('Other Information', { 'fields':(('disability','disability_description'), 'education_level')}),
        ('Course Applied For', { 'fields':(('applied_for', 'date_of_application'),)}),
        ('Education and experience information', {'fields':(('test_ma','test_eng'),('experience','other_courses'))}),
        ('Short Listing', {'fields':(('short_listed','test_ap'),)}),
        ('Ranking, Eligibility and Success', {'fields':(('ranking','eligibility','successful'),)}),
        ('Offer details', {'fields':(('date_offer_sent','date_offer_accepted'),)}),
        ('Admin (non editable)', {'fields':(('added', 'updated','last_change_by','penultimate_change_by'),)}),
    )
    form = ApplicantAdminForm
    list_display = ('__unicode__', 'gender', 'disability', 'applied_for', 'island', 'successful', 'test_ma', 'test_eng')
    list_filter = ('gender', 'disability', MathTestFilter, EnglishTestFilter, IslandFilter, 'successful', 'applied_for', 'eligibility')
    readonly_fields = ('added', 'updated','last_change_by','penultimate_change_by')
    actions = ['make_student', 'mark_unsuccessful']
    inlines = ( StudentInline, )

    def mark_unsuccessful(self, request, queryset):
        '''Marks a group of applicants as unsuccessful'''
        rows_updated = 0
        for applicant in queryset:
            applicant.successful = 0 #0 == FALSE
            applicant.save()
            rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 applicant was"
        else:
            message_bit = "%s applicants were" % rows_updated
        self.message_user(request, "%s marked unsuccessful." % message_bit)

    def make_student(self, request, queryset):
        '''Creates a convert to student option for applicants on the admin screen'''
        rows_updated = 0
        for applicant in queryset:
            applicant.convert_to_student()
            rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 applicant was"
        else:
            message_bit = "%s applicants were" % rows_updated
        self.message_user(request, "%s successfuly converted to students." % message_bit)
    
    def save_model(self, request, obj, form, change): 
        try:
            obj.last_change_by
        except:
            pass
        else:
            obj.penultimate_change_by = obj.last_change_by 
        obj.last_change_by = request.user 
        obj.save()

class ApplicantSuccess(admin.TabularInline):
    model = Student
    fields = ('__unicode__','successful')

class AssessmentAdmin(admin.ModelAdmin):
    model = Assessment
    fields = ('name','slug','subject','date_given','date_due')
    list_display = ('name','subject','date_given','date_due')
    list_filter = ('name','subject')
    prepopulated_fields = {'slug': ('name',)}

class StudentAttendanceAdmin(admin.ModelAdmin):
    model = StudentAttendance
    list_display = ('student','session','reason','absent')
    list_filter = ('reason','absent')
    
    def save_model(self, request, obj, form, change): 
        try:
            obj.last_change_by
        except:
            pass
        else:
            obj.penultimate_change_by = obj.last_change_by 
        obj.last_change_by = request.user 
        obj.save()

class CourseAdmin(admin.ModelAdmin):
    inlines = (EnrolmentInline,
               ApplicantInline,
        )
    filter_horizontal = ('subjects',)
    fieldsets = (
        ('', { 'fields':(('name','year', 'slug'),)}),
        ('Subjects', { 'fields':('subjects',)}),
    )
    list_display = ('name', 'count_students', 'count_males', 'count_females', 'subjects_available')
    model = Course 
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True

    def save_formset(self, request, form, formset, change): 
        if formset.model == Enrolment:
            instances = formset.save(commit=False)
            for instance in instances:
                try:
                    instance.last_change_by
                except:
                    pass
                else:   
                    instance.penultimate_change_by = instance.last_change_by
                instance.last_change_by = request.user
                instance.save()
        else:
            formset.save()

class CredentialAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',{'fields':[('aqf_level','institution'),('name','year'),'type']}),
    ]

    def save_model(self, request, obj, form, change): 
        try:
            obj.last_change_by
        except:
            pass
        else:
            obj.penultimate_change_by = obj.last_change_by 
        obj.last_change_by = request.user 
        obj.save()

class EnrolmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',{'fields':['student','course','date_started','date_ended','mark']}),
        ('Admin (non editable)', {'fields':(('last_change_by','penultimate_change_by'),)}),
    ]
    list_display = ('student', 'course', 'date_started')
    list_filter = ('course', 'date_started')
    readonly_fields = ('last_change_by','penultimate_change_by')
    
    def save_model(self, request, obj, form, change): 
        try:
            obj.last_change_by
        except:
            pass
        else:
            obj.penultimate_change_by = obj.last_change_by 
        obj.last_change_by = request.user 
        obj.save()

class GradeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',{'fields':['student','subject','date_started','results',]}),
        ('Admin (non editable)', {'fields':(('last_change_by','penultimate_change_by'),)}),
    ]
    list_display = ('student','subject','date_started','results')
    list_filter = ('subject','date_started','results')
    readonly_fields = ('last_change_by','penultimate_change_by')
     
    def save_model(self, request, obj, form, change): 
        try:
            obj.last_change_by
        except:
            pass
        else:
            obj.penultimate_change_by = obj.last_change_by 
        obj.last_change_by = request.user 
        obj.save()
    
class ResultAdmin(admin.ModelAdmin):
    model = Result

    def save_model(self, request, obj, form, change): 
        try:
            obj.last_change_by
        except:
            pass
        else:
            obj.penultimate_change_by = obj.last_change_by 
        obj.last_change_by = request.user 
        obj.save()
    
class SessionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Subject and time', { 'fields': (('subject','date','session_number','room_number'),'timetable',)}),
    )
    list_display = ('subject', 'day_of_week','date','timetable','get_session_number_display')
    list_filter = ('date','session_number','students', 'room_number')
    inlines = (StaffAttendanceInline, StudentAttendanceInline,)
    model = Session
    unique_together = ('subject','date','session_number')
    save_on_top = True

    def save_formset(self, request, form, formset, change): 
        if formset.model == StudentAttendance or formset.model == StaffAttendance:
            instances = formset.save(commit=False)
            for instance in instances:
                try:
                    instance.last_change_by
                except:
                    pass
                else:   
                    instance.penultimate_change_by = instance.last_change_by
                instance.last_change_by = request.user
                instance.save()
        else:
            formset.save()

class StaffAdminForm(ModelForm):
    class Meta:
        model = Staff
        widgets = {
            'dob': SelectDateWidget(years=BIRTH_YEARS),
            'gender': RadioSelect(),
        }            

class StaffAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Bio', { 'fields':(('first_name','surname'),('dob','gender'), ('island',))}),
        ('Contact Information', { 'fields':(('phone','phone2','email'),)}),
        ('Other Information', { 'fields':(('disability','disability_description'),('classification'))}),
        ('Admin (non editable)', {'fields':(('added', 'updated','last_change_by','penultimate_change_by'),)}),
    )
    form = StaffAdminForm
    list_display = ('__unicode__', 'gender', 'disability')
    list_filter = ('gender', 'disability')
    readonly_fields = ('added', 'updated','last_change_by','penultimate_change_by')
    inlines = (CredentialInline, StaffISLPRInline,)
    
    def save_model(self, request, obj, form, change): 
        try:
            obj.last_change_by
        except:
            pass
        else:
            obj.penultimate_change_by = obj.last_change_by 
        obj.last_change_by = request.user 
        obj.save()

    def save_formset(self, request, form, formset, change): 
        if formset.model == Credential:
            instances = formset.save(commit=False)
            for instance in instances:
                try:
                    instance.last_change_by
                except:
                    pass
                else:   
                    instance.penultimate_change_by = instance.last_change_by
                instance.last_change_by = request.user
                instance.save()
        else:
            formset.save()

class StudentAdminForm(ModelForm):
    class Meta:
        model = Student
        widgets = {
            'dob': SelectDateWidget(years=BIRTH_YEARS),
            'gender': RadioSelect(),
        }            

class StudentAdmin(admin.ModelAdmin):
    inlines = (EnrolmentInline, StudentISLPRInline, GradeInline, StudentAttendanceInline, )
    fieldsets = (
        ('Bio', { 'fields':(('first_name','surname'),('dob','gender'), ('island', 'slug'))}),
        ('Contact Information', { 'fields':(('phone','phone2','email'),)}),
        ('Other Information', { 'fields':(('disability','disability_description'), 'education_level', 'application_details')}),
        ('Admin (non editable)', {'fields':(('added', 'updated','last_change_by','penultimate_change_by'),)}),
    )
    form = StudentAdminForm
    list_display = ('__unicode__', 'slug', 'gender', 'disability')
    list_filter = ('gender', 'disability')
    ordering = ('-slug',) 
    readonly_fields = ('slug','added', 'updated','last_change_by','penultimate_change_by',)
    
    def save_model(self, request, obj, form, change): 
        try:
            obj.last_change_by
        except:
            pass
        else:
            obj.penultimate_change_by = obj.last_change_by 
        obj.last_change_by = request.user 
        obj.save()

    def save_formset(self, request, form, formset, change): 
        '''note that the following if isn't needed since all inlines use this, but is left as a bookmark'''
        if formset.model == Grade or formset.model == Enrolment or formset.model == StudentAttendance:
            instances = formset.save(commit=False)
            for instance in instances:
                try:
                    instance.last_change_by
                except:
                    pass
                else:   
                    instance.penultimate_change_by = instance.last_change_by
                instance.last_change_by = request.user
                instance.save()
        else:
            formset.save()

class SubjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', { 'fields': (('name','slug'),('year','semester'), 'staff_member')}),
    )

    list_display = ('name','year','semester')
    list_filter = ('year', 'semester', 'name')
    model = Subject
    prepopulated_fields = {'slug': ('name','year')}
    inlines = [ AssessmentInline, SessionInline, GradeInline,]
    
    def save_formset(self, request, form, formset, change): 
        if formset.model == Grade:
            instances = formset.save(commit=False)
            for instance in instances:
                try:
                    instance.last_change_by
                except:
                    pass
                else:   
                    instance.penultimate_change_by = instance.last_change_by
                instance.last_change_by = request.user
                instance.save()
        else:
            formset.save()

class TimetableAdmin(admin.ModelAdmin):
    model = Timetable
    prepopulated_fields = {'slug': ('year','term')}

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Credential, CredentialAdmin)
admin.site.register(Enrolment, EnrolmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(StudentISLPR)
admin.site.register(StaffISLPR)
admin.site.register(StaffAttendance)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentAttendance, StudentAttendanceAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Timetable, TimetableAdmin)
