from .views import ExpenseSummaryStatus, IncomeSourcesSummaryStatus
from django.urls import path


urlpatterns = [
    path('expenses_category_data', ExpenseSummaryStatus.as_view(), 
         name="expenses-category-summary"),
    path('incomes_source_data', IncomeSourcesSummaryStatus.as_view(),
          name="incomes-source-summary"),
]