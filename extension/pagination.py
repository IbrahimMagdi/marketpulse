from django.core.paginator import Paginator, EmptyPage

class PaginatorService:
    def __init__(self, per_page=10):
        self.per_page = per_page

    def paginate_with_response(self, items, page_number):
        paginator = Paginator(items, self.per_page)
        try:
            page_obj = paginator.page(page_number)
            items_list = list(page_obj)
        except EmptyPage:
            items_list = []
        return {
            "list_items": items_list,
            "page": page_number,
            "total_pages": paginator.num_pages
        }
