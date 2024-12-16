import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Lead, SalesPipeline, Contact
from .forms import LeadForm, ContactForm, SalesPipelineForm
from django.shortcuts import get_object_or_404
from django.db.models import Count


# Lead List View
@login_required
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'lead_management/leads.html', {'leads': leads})

# Add Lead View
@login_required
def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads')
    else:
        form = LeadForm()
    return render(request, 'lead_management/add_lead.html', {'form': form})

# Contact List View
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'lead_management/contacts.html', {'contacts': contacts})

# Add Contact View
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact added successfully.")
            return redirect('contacts')  # Redirect to the contacts list
    else:
        form = ContactForm()
    return render(request, 'lead_management/add_contact.html', {'form': form})

# Edit Contact View
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully.")
            return redirect('contacts')  # Redirect to the contacts list
    else:
        form = ContactForm(instance=contact)
    return render(request, 'lead_management/edit_contact.html', {'form': form})

# Delete Contact View
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    messages.success(request, "Contact deleted successfully.")
    return redirect('contacts')  # Redirect to the contacts list

# Edit Lead View
@login_required
def edit_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads')
    else:
        form = LeadForm(instance=lead)
    return render(request, 'lead_management/edit_lead.html', {'form': form})

# Delete Lead View
@login_required
def delete_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()
    return redirect('leads')

# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'lead_management/signup.html', {'form': form})

# Sales Pipeline View
def sales_pipeline(request):
    pipeline_data = SalesPipeline.objects.all().select_related('lead')  # Efficient query
    return render(request, 'lead_management/sales_pipeline.html', {'pipeline_data': pipeline_data})

# Add Sales Pipeline View
@login_required
def add_sales_pipeline(request):
    if request.method == 'POST':
        form = SalesPipelineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sales pipeline entry added successfully!')
            return redirect('sales_pipeline')
    else:
        form = SalesPipelineForm()
    return render(request, 'lead_management/add_sales_pipeline.html', {'form': form})

# Update Stage View
@login_required
def update_stage(request, pk):
    pipeline = get_object_or_404(SalesPipeline, pk=pk)
    if request.method == 'POST':
        form = SalesPipelineForm(request.POST, instance=pipeline)
        if form.is_valid():
            form.save()
            messages.success(request, "Sales stage updated successfully.")
            return redirect('sales_pipeline')
    else:
        form = SalesPipelineForm(instance=pipeline)
    return render(request, 'lead_management/update_stage.html', {'form': form, 'pipeline': pipeline})

# View Lead Progress
@login_required
def view_lead_progress(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    sales_pipeline = SalesPipeline.objects.filter(lead=lead)
    return render(request, 'lead_management/lead_progress.html', {'lead': lead, 'sales_pipeline': sales_pipeline})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'lead_management/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'lead_management/dashboard.html')

@login_required
def report_and_analytics(request):
    # Fetching lead count per status or an appropriate field
    # Replace 'status' with 'source' or another field if 'status' is not available
    lead_statuses = Lead.objects.values('source').annotate(count=Count('source'))
    statuses = [status['source'] for status in lead_statuses]
    counts = [status['count'] for status in lead_statuses]

    # Generate Lead Status Distribution Pie Chart
    fig, ax = plt.subplots()
    ax.pie(counts, labels=statuses, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Lead Status Distribution')

    # Save pie chart to a BytesIO object
    pie_img = io.BytesIO()
    plt.savefig(pie_img, format='png')
    pie_img.seek(0)
    pie_chart = base64.b64encode(pie_img.getvalue()).decode('utf8')

    # Generate Sales Pipeline Stage Metrics Bar Chart
    pipeline_stages = SalesPipeline.objects.values('stage').annotate(count=Count('stage'))
    stages = [stage['stage'] for stage in pipeline_stages]
    stage_counts = [stage['count'] for stage in pipeline_stages]

    fig2, ax2 = plt.subplots()
    ax2.bar(stages, stage_counts)
    ax2.set_xlabel('Pipeline Stage')
    ax2.set_ylabel('Number of Leads')
    ax2.set_title('Sales Pipeline Stage Metrics')

    # Save bar chart to a BytesIO object
    bar_img = io.BytesIO()
    plt.savefig(bar_img, format='png')
    bar_img.seek(0)
    bar_chart = base64.b64encode(bar_img.getvalue()).decode('utf8')

    # Pass the charts to the template
    return render(request, 'lead_management/report_and_analytics.html', {
        'pie_chart': pie_chart,
        'bar_chart': bar_chart
    })




