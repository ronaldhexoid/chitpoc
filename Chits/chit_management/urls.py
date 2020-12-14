from django.urls import path
from .views import PanUpload,AadharUpload,AddressUpload,BankUpload


urlpatterns = [
    path('uploadPan/', PanUpload.as_view(), name="Upload Pan"),
    path('uploadAadhar/', AadharUpload.as_view(), name="Upload Aadhar"),
    path('uploadAddress/', AddressUpload.as_view(), name="Upload Address"),
    path('uploadBank/', BankUpload.as_view(), name="Upload Bank Statement"),
    ]