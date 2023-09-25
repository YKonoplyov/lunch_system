from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from vote_service.models import Votes


def has_user_voted(request) -> bool:
    try:
        Votes.objects.select_related("employee").get(
            employee_id=request.user.id, date_voted=timezone.now().date()
        )
        return False
    except ObjectDoesNotExist:
        return True
