from django.urls import path
from .views import *

app_name = "ecomapp"

urlpatterns = [

    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("all-products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCart.as_view(), name="emptycart"),
    path("checkout/", CheckOut.as_view(), name="checkout"),
    path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),

    path("regiter/", CustomerRegistration.as_view(), name="customerregistration"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("profile/", CustomerProfile.as_view(), name="customerprofile"),
    path("profile/order/<int:pk>/", CustomerOrderDetail.as_view(), name="customerorderdetail"),
    path("search/", SearchView.as_view(), name="search"),


    #Admin
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-logout/", AdminLogoutView.as_view(), name="adminlogout"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetail.as_view(), name="adminorderdetail"),
    path("admin-order-/<int:pk>-change/", AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange"),








]