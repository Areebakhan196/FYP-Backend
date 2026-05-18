from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import TruncDate
from complaints.models import Complaint
from core.permissions import IsStaffUserOrDevOpen


class AnalyticsSummaryView(APIView):
    permission_classes = [IsStaffUserOrDevOpen]

    def get(self, request):
        total_complaints = Complaint.objects.count()
        status_breakdown = Complaint.objects.values('status').annotate(count=Count('status'))

        daily_stats = (
            Complaint.objects.annotate(day=TruncDate('created_at'))
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )

        data = {
            "total_complaints": total_complaints,
            "status_breakdown": {item['status']: item['count'] for item in status_breakdown},
            "daily_trend": list(daily_stats),
        }
        return Response(data)
