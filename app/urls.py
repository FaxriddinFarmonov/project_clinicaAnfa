from django.urls import path

from .services.auto import gets, auto_form, auto_del
from .services.auth import profile,sign_up,sign_in,sign_out,search,otp
from .services.client import client_doc
from .services.derector import list_members,banned,grader

from .views import index



urlpatterns = [

    path("", index, name="home"),
    path('otp/',otp ,name='otp'),

    # user
    path("auth/",sign_in, name="login"),
    path("auto/regis/", sign_up, name="regis"),
    path("auto/logout/", sign_out, name="logout"),
    path("auto/profile/", profile, name="profile"),
    
    #auto
    path("auto/<key>/",gets,name="dashboard-auto-list" ),
    path("auto/<key>/detail/<int:pk>/",gets,name="dashboard-auto-detail" ),
    path("auto/<key>/add/",auto_form,name="dashboard-auto-add" ),
    path("auto/<key>/edit/<int:pk>/",auto_form,name="dashboard-auto-edit" ),
    path("auto/<key>/del/<int:pk>/",auto_del,name="dashboard-auto-delete" ),

    #member
    path("member/<int:tpe>/",list_members,name='members'),
    path("member/new/<int:new>/",list_members,name='members-new'),
    path("banner/u-<int:user_id>/t-<int:tpe>/s-<int:status>/",banned,name='banned'),
    path("grader/<int:pk>/<int:ut>/<int:dut>/",grader,name='grader'),
    # path("spammer/<int:pk>/<int:dut>/",spammer,name='spammer'),

    #search
    path("search/",search,name="search_wor"),

    #client
    path("client/doc/<int:service>/",client_doc,name='servicedocs')


]
