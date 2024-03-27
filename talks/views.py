from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, UpdateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader

from datetime import datetime

from django.utils import timezone
from rest_framework import viewsets

from .serializers import TalkSerializer
from .models import *
from .models import Document
from .forms import DocumentForm
from .forms import ProposalForm
from .mixins import EditOwnTalksMixin
 
from django.views.generic.detail import DetailView  
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from next_prev import next_in_order, prev_in_order

#Sending html emails to user
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage 
from django.http import Http404
from .resources import ProposalResource
from home.models import EventYear 




@login_required
def submit_talk(request, year):
    try:
        event_year = EventYear.objects.get(year=year)
        # Fetch all submission periods for the event year and determine their status
        submission_periods = CFPSubmissionPeriod.objects.filter(event_year=event_year).order_by('start_date')
        active_period = None
        upcoming_period = None

        for period in submission_periods:
            if period.start_date <= timezone.now() <= period.end_date:
                active_period = period
                break
            elif timezone.now() < period.start_date and not upcoming_period:
                upcoming_period = period

        context = {
            'title': 'Submit a Talk',
            'year': year,
            'active_period': active_period,
            'upcoming_period': upcoming_period,
            'form': ProposalForm()  # Initialize the form outside the POST request scope to handle GET requests
        }

        if request.method == "POST" and active_period:
            form = ProposalForm(request.POST)
            if form.is_valid():
                proposal = form.save(commit=False)
                proposal.user = request.user
                proposal.event_year = event_year
                proposal.save()

                # Send confirmation email
                subject = 'Talk Submission Confirmation'
                html_content = render_to_string('emails/talks/submission_confirmation.html', {'user': request.user, 'proposal': proposal})
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(subject, text_content, to=[request.user.email])
                email.attach_alternative(html_content, "text/html")
                email.send()
 
                return redirect('talks:submitted', year=event_year.year)
            else:
                context['form'] = form  # Update context with the form containing validation errors
    except EventYear.DoesNotExist:
        return redirect(reverse_lazy('talks:no_event_year_error'))

    # Use dynamic path for template to allow customization per event year
    template_path = f"{year}/talks/talk_form.html"
    return render(request, template_path, context)

  

@login_required
def edit_talk(request, year, pk):
    proposal = get_object_or_404(Proposal, pk=pk)
    if str(proposal.event_year.year) != str(year):
        raise Http404("Proposal does not exist for the given year.")
    
    if request.method == "POST":
        form = ProposalForm(request.POST, instance=proposal)
        if form.is_valid():
            form.save()
            return redirect('talks:talk_list', year=proposal.event_year.year)
    else:
        form = ProposalForm(instance=proposal)
    
    template_prefix = f"{proposal.event_year.year}/talks/"
    context = {
        'form': form,
        'year': year,
        'proposal': proposal,  # Add the proposal to the context
    }
    return render(request, template_prefix + 'edit_talk.html', context)

class TalkList(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(TalkList, self).get_context_data(**kwargs)
        # Assuming 'year' is passed as a URL parameter, otherwise default to the current year
        year = self.kwargs.get('year', timezone.now().year)
        context['year'] = year

        # Get all proposals submitted by the user for the specific year
        context['submitted_talks'] = Proposal.objects.filter(user=self.request.user, event_year__year=year)
        
        return context

    def get_template_names(self):
        # Use the year from the context to determine the template path
        year = self.kwargs.get('year', timezone.now().year)
        template_path = f"{year}/talks/talk_list.html"
        return [template_path]
    
     


class TalkView(UpdateView):
    form_class = ProposalForm
    model = Proposal
    slug_field = 'slug'
    # Assuming you have a method or logic within EditOwnTalksMixin that correctly identifies the object

    def get_success_url(self):
        # Dynamically redirect to a success page, potentially including the year
        proposal = self.get_object()
        return reverse_lazy('talks:submitted', kwargs={'year': proposal.event_year.year})

    def get_template_names(self):
        proposal = self.get_object()
        # Dynamically select the template based on the event year of the proposal
        return [f"{proposal.event_year.year}/talks/talk.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proposal = self.get_object()
        context['title'] = "Talk Details"
        context['year'] = proposal.event_year.year  # Use the event year of the proposal
        return context
 

class TalkDetailView(TemplateView):
    def get_template_names(self):
        proposal = get_object_or_404(Proposal, proposal_id=self.kwargs.get('pk'))  
        event_year = proposal.event_year.year
        return [f"{event_year}/talks/talk_details.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proposal = get_object_or_404(Proposal, proposal_id=self.kwargs.get('pk')) 
        context['title'] = "Accepted Talks"
        context['year'] = proposal.event_year.year
        context['talk'] = proposal
        return context
     
class TalksDetailView(DetailView):
    model = Proposal
    context_object_name = 'schedule'
    slug_field = 'proposal_id'
    # Removed static template_name to dynamically set it in get_template_names
    # Assuming count_hit and paginate_by are handled elsewhere or part of HitCountDetailView specifics

    def get_template_names(self):
        # Assuming the proposal ID is used to fetch the object, not a slug
        proposal = self.get_object()
        proposal_year = proposal.event_year.year
        return [f"{proposal_year}/schedule/talk_details.html"]

    def get_context_data(self, **kwargs):
        context = super(TalksDetailView, self).get_context_data(**kwargs)
        context['title'] = "Talk Detail Details"
        context['year'] = self.object.event_year.year  # Use the event year from the proposal
        context['related_talks'] = Proposal.objects.filter(status='A', event_year=self.object.event_year).order_by('?')[:5]
        return context
 
class SuccessView(TemplateView):
    def get_template_names(self):
        # Attempt to fetch the event year from URL kwargs
        year = self.kwargs.get('year', timezone.now().year)
        # Verify if the EventYear exists, raise 404 if not
        if not EventYear.objects.filter(year=year).exists():
            raise Http404("Event year does not exist.")
        # Construct the template path using the event year
        return [f"{year}/talks/success.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Assuming 'year' is passed as a URL parameter, otherwise default to the current year
        year = self.kwargs.get('year', timezone.now().year)
        context['title'] = 'Talk Submission Successful'
        context['year'] = year
        return context


class TalkViewsSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = TalkSerializer
    queryset = Proposal.objects.all()


class AcceptedTalksView(TemplateView):
    template_name = "talks/accepted_talks.html"

    def get_context_data(self, **kwargs):
        context = super(AcceptedTalksView, self).get_context_data(**kwargs)
        context['title'] = "Accepted Talks"
        context['year'] = datetime.now().year
        talks_list = Proposal.objects.filter(status='A').select_related('user')

        paginator = Paginator(talks_list, 10)  # Show 10 posts per page
        page = self.request.GET.get('page')
        try:
            accepted_talks = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            accepted_talks = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            accepted_talks = paginator.page(paginator.num_pages)
        context['accepted_talks'] = accepted_talks
        return context



def export(request):
    proposal_resource = ProposalResource()
    dataset = proposal_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="proposals.csv"'
    return response
 


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })



def home(request):
    documents = Document.objects.all()
    return render(request, 'upload/home.html', { 'documents': documents })
 
def redirect_to_current_year_speaking(request):
    current_year = timezone.now().year
    return redirect('speaking', year=current_year)
 
def redirect_to_current_year_proposing(request):
    current_year = timezone.now().year
    return redirect('proposing', year=current_year)

def redirect_to_current_year_recording(request):
    current_year = timezone.now().year
    return redirect('recording', year=current_year)

def speaking(request, year=None):
    year = year or timezone.now().year
    event_year = get_object_or_404(EventYear, year=year)
    speaks = Speak.objects.filter(event_year=event_year).order_by('-date_created')
    template_name = f'{year}/talks/talks.html'
    return render(request, template_name, {'speaks': speaks, 'event_year': event_year})

def recording(request, year=None):
    year = year or timezone.now().year
    event_year = get_object_or_404(EventYear, year=year)
    recordings = Recording.objects.filter(event_year=event_year).order_by('-date_created')
    template_name = f'{year}/talks/recordings.html'
    return render(request, template_name, {'recordings': recordings, 'event_year': event_year})

def proposing(request, year=None):
    year = year or timezone.now().year
    event_year = get_object_or_404(EventYear, year=year)
    proposing_talks = Proposing_talk.objects.filter(event_year=event_year).order_by('-date_created')
    template_name = f'{year}/talks/proposing_a_talk.html'
    return render(request, template_name, {'proposing_talks': proposing_talks, 'event_year': event_year})
 

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload/model_form_upload.html', {
        'form': form
    })
