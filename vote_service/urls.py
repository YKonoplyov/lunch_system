from django.urls import path

from vote_service.views import VoteCreateView, GetVoteResultsView

urlpatterns = [
    path("vote/", VoteCreateView.as_view(), name="make_vote"),
    path("results/", GetVoteResultsView.as_view(), name="voting_results"),
]

app_name = "vote-service"
