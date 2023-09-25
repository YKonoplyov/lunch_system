from django.urls import path

from vote_service.views import VoteCreateView

urlpatterns = [
    path("vote", VoteCreateView.as_view(), name="make_vote")
]

app_name = "vote-service"
