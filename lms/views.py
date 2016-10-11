from django.shortcuts import render
from django.views.generic import DetailView, View
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import User, UserProfile, Project, Lesson, Test

# Create your views here.

class ListProjects(View):
	'''
	List all public projects
	'''
	def get(self, request):
		project = Project.objects
		publicProjects = Project.objects.filter(isPublic=True).values()
		
		context = {
			'project': project,
			'publicProjects': publicProjects,
		}
		if request.user.is_authenticated:
			myPrivateProjects = Project.objects.filter(owner = request.user, isPublic = False).values()
			myPublicProjects = Project.objects.filter(owner = request.user, isPublic = True).values()
			context = {
				'project': project,
				'publicProjects': publicProjects,
				'myPrivateProjects' : myPrivateProjects,
				'myPublicProjects' : myPublicProjects,
			}
		return render(request, 'project_list.html', context)


class ProjectDetail(DetailView):
	model = Project
	template_name = 'project-detail.html'
	
class ListAllProjects(View):
	def get(self, request):
	
		project = Project.objects
		publicProjects = Project.objects.filter(isPublic=True).values()
		
		context = {
			'project': project,
			'publicProjects': publicProjects,
			
		}
		
		return render(request, 'project_list.html', context)
		
class ListLessons(View):
	'''
	List all public lessons
	'''
	def get(self, request):
		lesson = Lesson.objects
		publicLessons = Lesson.objects.filter(isPublic=True).values()

		
		if request.user.is_authenticated:
			myPrivateLessons = Lesson.objects.filter(owner = request.user, isPublic = False).values()
			myPublicLessons = Lesson.objects.filter(owner = request.user, isPublic = True).values()
			context = {
				'lesson': lesson,
				'publicLessons': publicLessons,
				'myPrivateLessons' : myPrivateLessons,
				'myPublicLessons' : myPublicLessons,
			}
		else:
			context = {
				'lesson': lesson,
				'publicLessons': publicLessons,
			}
		return render(request, 'lesson_list.html', context)


class LessonDetail(DetailView):
	model = Lesson
	template_name = 'lesson-detail.html'
	
class ListAllLessons(View):
	def get(self, request):
	
		lesson = Lesson.objects
		publicLessons = Lesson.objects.filter(isPublic=True).values()
		
		context = {
			'lesson': lesson,
			'publicLessons': publicLessons,
			
		}
		
		return render(request, 'lesson_list.html', context)
			
class ListTests(View):
	'''
	List all public tests
	'''
	def get(self, request):
		test = Test.objects
		publicTests = Test.objects.filter(isPublic=True).values()

		if request.user.is_authenticated:
			myPrivateTests = Test.objects.filter(owner = request.user, isPublic = False).values()
			myPublicTests = Test.objects.filter(owner = request.user, isPublic = True).values()
			context = {
				'test': test,
				'publicTests': publicTests,
				'myPrivateTests' : myPrivateTests,
				'myPublicTests' : myPublicTests,
			}
		else:
			context = {
				'test': test,
				'publicTests': publicTests,
			}
		
		return render(request, 'test_list.html', context)


class TestDetail(DetailView):
	model = Test
	template_name = 'test-detail.html'
	
class ListAllTests(View):
	def get(self, request):
	
		test = Test.objects
		publicTests = Test.objects.filter(isPublic=True).values()
		
		context = {
			'test': test,
			'publicTests': publicTests,
			
		}
		
		return render(request, 'test_list.html', context)
						
			
			
			
			
			
			