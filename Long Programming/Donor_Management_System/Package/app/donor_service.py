from app.donor_repository import DonorCreate, DonorOut
def add_donor(request):
    return DonorCreate(request)

def fetch_donors():
    return DonorOut()