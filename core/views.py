# views.py
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from core.models import Portfolio, Certificate, Project, Info

def home(request):
    portfolios = Portfolio.objects.all()
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    info = Info.objects.all()

    context = {
        'portfolios': portfolios,
        'projects': projects,
        'certificates': certificates,
        'info': info,
    }

    return render(request, 'index.html', context)

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__"

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = "__all__"


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = "__all__"

# ... other form classes

def manage_portfolio(request):
    # Get or create the single objects
    portfolio, created = Portfolio.objects.get_or_create(defaults={'title': 'My Portfolio', 'description': 'A new portfolio'})
    info, created = Info.objects.get_or_create(portfolio=portfolio, defaults={'leet_code': 0, 'professional_exp': 0, 'intern_ship': 0})
    
    # Create forms with existing instances
    portfolio_form = PortfolioForm(request.POST or None, request.FILES or None, instance=portfolio)
    info_form = InfoForm(request.POST or None, instance=info)
    project_form = ProjectForm(request.POST or None)
    certificate_form = CertificateForm(request.POST or None, request.FILES or None) # Pass files here for the form to validate

    # Handle form submissions
    if request.method == "POST":
        if "save_portfolio" in request.POST and portfolio_form.is_valid():
            try:
                portfolio_form.save()
            except ValidationError as e:
                portfolio_form.add_error(None, e)
            return redirect("manage_portfolio")

        elif "save_info" in request.POST and info_form.is_valid():
            try:
                info_form.save()
            except ValidationError as e:
                info_form.add_error(None, e)
            return redirect("manage_portfolio")

        elif "add_project" in request.POST and project_form.is_valid():
            project = project_form.save(commit=False)
            project.portfolio = portfolio
            project.save()
            return redirect("manage_portfolio")

        elif "add_certificate" in request.POST:
            if certificate_form.is_valid():
                certificate = certificate_form.save(commit=False)
                certificate.portfolio = portfolio # Now 'portfolio' is guaranteed to exist
                certificate.save()
                return redirect("manage_portfolio")
            else:
                print(certificate_form.errors) # print errors in console

    # Fetch all existing objects
    projects = Project.objects.all()
    certificates = Certificate.objects.all()

    return render(
        request,
        "manage_portfolio.html",
        {
            "portfolio_form": portfolio_form,
            "info_form": info_form,
            "project_form": project_form,
            "certificate_form": certificate_form,
            "projects": projects,
            "certificates": certificates,
        },
    )

# from django.shortcuts import render, redirect
# from django.forms import ModelForm
# from django.core.exceptions import ValidationError
# from core.models import Portfolio, Certificate, Project, Info

# def home(request):

#     portfolios = Portfolio.objects.all()
#     projects = Project.objects.all()
#     certificates = Certificate.objects.all()
#     info = Info.objects.all()

#     context = {
#         'portfolios': portfolios,
#         'projects': projects,
#         'certificates': certificates,
#         'info': info,
#     }

#     return render(request, 'index.html', context)

# class PortfolioForm(ModelForm):
#     class Meta:
#         model = Portfolio
#         fields = "__all__"


# class ProjectForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = "__all__"


# class CertificateForm(ModelForm):
#     class Meta:
#         model = Certificate
#         fields = "__all__"


# class InfoForm(ModelForm):
#     class Meta:
#         model = Info
#         fields = "__all__"


# def manage_portfolio(request):
#     # Get existing single objects (if any)
#     portfolio = Portfolio.objects.first()
#     info = Info.objects.first()

#     # Create forms with existing instances
#     portfolio_form = PortfolioForm(request.POST or None, request.FILES or None, instance=portfolio)
#     info_form = InfoForm(request.POST or None, instance=info)
#     project_form = ProjectForm(request.POST or None)
#     certificate_form = CertificateForm(request.POST or None)

#     # Handle form submissions
#     if request.method == "POST":
#         if "save_portfolio" in request.POST and portfolio_form.is_valid():
#             try:
#                 portfolio_form.save()
#             except ValidationError as e:
#                 portfolio_form.add_error(None, e)
#             return redirect("manage_portfolio")

#         elif "save_info" in request.POST and info_form.is_valid():
#             try:
#                 info_form.save()
#             except ValidationError as e:
#                 info_form.add_error(None, e)
#             return redirect("manage_portfolio")

#         elif "add_project" in request.POST and project_form.is_valid():
#             project_form.save()
#             return redirect("manage_portfolio")

#         elif "add_certificate" in request.POST:
#             certificate_form = CertificateForm(request.POST, request.FILES)
#             if certificate_form.is_valid():
#                 certificate = certificate_form.save(commit=False)
#                 certificate.portfolio = portfolio
#                 certificate.save()
#                 if certificate.certificate_image:  # assuming your field is named `image`
#                     print("Uploaded certificate image URL:", certificate.certificate_image.url)
#                 return redirect("manage_portfolio")
#             else:
#                 print(certificate_form.errors)  # 👈 print errors in console


#     # Fetch all existing objects
#     projects = Project.objects.all()
#     certificates = Certificate.objects.all()

#     return render(
#         request,
#         "manage_portfolio.html",
#         {
#             "portfolio_form": portfolio_form,
#             "info_form": info_form,
#             "project_form": project_form,
#             "certificate_form": certificate_form,
#             "projects": projects,
#             "certificates": certificates,
#         },
#     )
