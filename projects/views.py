from django.shortcuts import render
from projects.dao.ontology import Ontology

onto = Ontology('quanlidetai_goc2.owl')

# Create your views here.
def teacher_search(request):
    query = request.POST.get('q')
    teachers = onto.search_teachers(query)
    context = {
        'teachers': teachers
    }
    return render(request, 'teacher_index.html', context)

def teacher_index(request):
    teachers = onto.get_teachers()

    context = {
        'teachers': teachers
    }

    return render(request, 'teacher_index.html', context)

def teacher_detail(request, id):
    teacher = onto.get_teacher(id)

    context = {
        'teacher': teacher
    }

    return render(request, 'teacher_detail.html', context)

def product_search(request):
    query = request.POST.get('q')
    products = onto.search_products(query)
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)

def product_index(request):
    products = onto.get_products()
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)

def product_detail(request, id):
    product = onto.get_product(id)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def subject_index(request):
    subjects = onto.get_subjects()
    context = {
        'subjects': subjects
    }
    return render(request, 'subject_index.html', context)

def subject_detail(request, id):
    subject = onto.get_subject(id)
    context = {
        'subject': subject
    }
    return render(request, 'subject_detail.html', context)
