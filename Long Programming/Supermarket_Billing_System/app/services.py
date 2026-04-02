from app.repository import create_bill, get_all_bills

def generate_bill(request):
    return create_bill(request)

def fetch_bills():
    return get_all_bills()