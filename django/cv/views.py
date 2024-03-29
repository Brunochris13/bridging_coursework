from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from .models import *

# Create your views here.
def home_page(request):
    bio = Bio.objects.all()
    education = EducationPost.objects.all()
    work = WorkPost.objects.all()
    profEngagements = ProfessionalEngagementsPost.objects.all()
    workProjects = WorkProjectPost.objects.all()
    achievements = AchievementPost.objects.all()
    qualifications = QualificationPost.objects.all()
    skills = SkillPost.objects.all()
    interests = InterestPost.objects.all()
    add_activities = AddActivitiesPost.objects.all()
    projects = ProjectPost.objects.all()
    cv_pdf = CvPdf.objects.all()

    return render(request, 'cv/home_page.html', {
        'bio': bio,
        'education': education,
        'work': work,
        'profEngagements': profEngagements,
        'workProjects' : workProjects,
        'achievements': achievements,
        'qualifications': qualifications,
        'skills': skills,
        'interests': interests,
        'projects': projects,
        'cv_pdf': cv_pdf,
        'add_activities': add_activities,
    })

@staff_member_required
def bio_edit(request):
    bio = Bio.objects.first()
    if request.method == 'POST':
        form = BioForm(request.POST, instance=bio)
        if form.is_valid():
            bio = form.save(commit=False)
            bio.save()
            return redirect('home_page')
    else:
        form = BioForm(instance=bio)
    return render(request, 'cv/cv_post_edit.html', {
        'form': form
    })

@staff_member_required
def cv_post_edit(request, category, pk):
    form_class = get_form_class(category)
    post = get_object_or_404(get_post_class(category), pk=pk)
    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home_page')
    else:
        form = form_class(instance=post)
    return render(request, 'cv/cv_post_edit.html', {'form': form})

@staff_member_required
def cv_post_new(request, category):
    form_class = get_form_class(category)
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home_page')
    else:
        form = form_class()
    return render(request, 'cv/cv_post_edit.html', {'form': form})

@staff_member_required
def cv_post_delete(request, category, pk):
    post = get_object_or_404(get_post_class(category), pk=pk)
    if request.method == "GET":
        if (category == "Project"):
            post.removeImage()
        post.delete()
    return redirect('home_page')

def get_form_class(category):
    switcher = {
        'Education' : EducationPostForm,
        'Work' : WorkPostForm,
        'ProfEngagements' : ProfessionalEngagementsPostForm,
        'WorkProject' : WorkProjectPostForm,
        'Achievement' : AchievementPostForm,
        'Qualification' : QualificationPostForm,
        'Skill' : SkillPostForm,
        'Interest' : InterestPostForm,
        'Project' : ProjectPostForm,
        'Add_Activities' : AddActivitiesPostForm,
    }
    return switcher.get(category, "Invalid category")

def get_post_class(category):
    switcher = {
        'Education' : EducationPost,
        'Work' : WorkPost,
        'ProfEngagements' : ProfessionalEngagementsPost,
        'WorkProject' : WorkProjectPost,
        'Achievement' : AchievementPost,
        'Qualification' : QualificationPost,
        'Skill' : SkillPost,
        'Interest' : InterestPost,
        'Project' : ProjectPost,
        'Add_Activities' : AddActivitiesPost,
    }
    return switcher.get(category, "Invalid category")

@staff_member_required
def cv_pdf_upload(request):
    cv_pdf = CvPdf.objects.first()
    if request.method == 'POST':
        form = CvPdfForm(request.POST, request.FILES, instance=cv_pdf)
        if form.is_valid():
            cv_pdf = form.save(commit=False)
            cv_pdf.save()
            return redirect('home_page')
    else:
        form = CvPdfForm(instance=cv_pdf)
    return render(request, 'cv/cv_post_edit.html', {
        'form': form
    })