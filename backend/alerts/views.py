import json
from django.shortcuts import render
from .models import Stock


def home(request):
    top_stocks = list(Stock.objects.all().values('symbol', 'name', 'price'))
    stocks_json = json.dumps(top_stocks, ensure_ascii=False)  # ← هنا التحويل
    return render(request, 'home.html', {'stocks': stocks_json})