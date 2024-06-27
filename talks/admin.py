from django.contrib import admin
from .models import Proposal, CFPSubmissionPeriod, Speak, SpeakerInvitation, Proposing_talk, Reviewer, Review, Recording
from import_export.admin import ImportExportModelAdmin
from .forms import ReviewForm
from markdownx.admin import MarkdownxModelAdmin

class TalkAdmin(ImportExportModelAdmin):
    list_display = ("title", "user", 'list_speakers', "talk_type", "intended_audience", "status", 'created_date', 'date_updated')
    list_editable = ["status"]
    list_filter = ("talk_type",  'created_date', "status")

    def list_speakers(self, obj):
        return ", ".join([speaker.username for speaker in obj.speakers.all()])
    list_speakers.short_description = 'Speakers'

admin.site.register(Proposal, TalkAdmin)

class CFPSubmissionPeriodAdmin(admin.ModelAdmin):
    list_display = ('event_year', 'start_date', 'end_date', 'is_active_period')
    list_filter = ('event_year',)
    search_fields = ('event_year__year',)

    def is_active_period(self, obj):
        """Utility method to display if the submission period is currently active."""
        return obj.is_active()
    is_active_period.boolean = True
    is_active_period.short_description = 'Is active?'

admin.site.register(CFPSubmissionPeriod, CFPSubmissionPeriodAdmin)

class SpeakAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')  
    ordering = ['-date_created']

admin.site.register(Speak, SpeakAdmin)

class SpeakerInvitationAdmin(admin.ModelAdmin):
    list_display = ('talk', 'invitee', 'status', 'invitation_sent')  
    ordering = ['-invitation_sent']

admin.site.register(SpeakerInvitation, SpeakerInvitationAdmin)

class ProposingTalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')  
    ordering = ['-date_created']

admin.site.register(Proposing_talk, ProposingTalkAdmin)

class ReviewerAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_email']
    search_fields = ['user__username', 'user__email']

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'  # Allows column order sorting
    get_email.short_description = 'Email Address'  # Renames column head

admin.site.register(Reviewer, ReviewerAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['talk', 'get_reviewer_name', 'score', 'get_hashid', 'short_comment']

    def get_reviewer_name(self, obj):
        return obj.reviewer.user.get_full_name() or obj.reviewer.user.username
    get_reviewer_name.admin_order_field = 'reviewer__user__username'  # Allows column order sorting by username
    get_reviewer_name.short_description = 'Reviewer Name'  # Renames column head

    def get_hashid(self, obj):
        return str(obj.id)  # Assuming 'id' is a Hashid field
    get_hashid.admin_order_field = 'id'  # Allows column order sorting
    get_hashid.short_description = 'ID'  # Renames column head

    def short_comment(self, obj):
        return obj.comments[:50] + '...' if len(obj.comments) > 50 else obj.comments
    short_comment.short_description = 'Comments'

    def score(self, obj):
        return obj.score  # Assuming 'score' is a field in the Review model
    score.admin_order_field = 'score'  # Allows column order sorting
    score.short_description = 'Score'

admin.site.register(Review, ReviewAdmin)

class RecordingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')  
    ordering = ['-date_created']

admin.site.register(Recording, RecordingAdmin)
