from django.urls import path
from .views import CakeAPIView, CakeDetailsAPIView


urlpatterns = [
    path(
        "cakes/", 
        CakeAPIView.as_view()
    ),
    path(
        "cakes/<int:cake_id>/", # http://127.0.0.1:8000/cakes/21/
        CakeDetailsAPIView.as_view()
    ),    
]

# cake_id = 1
# url = f"cakes/{cake_id}/"
# "cakes/1/"

# "cakes/150/"

# "cakes/4192/"

# "cakes/8892912/"