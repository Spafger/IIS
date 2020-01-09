from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user

from LabaUD.forms import *
from LabaUD.models import *
import random

# Create your views here.

def index(request):
    cur_user = get_user(request)
    number = random.randint(1, 100)
    return render(request, "index.html", locals())


def mainmenu(request):
    cur_user = get_user(request)
    return render(request, "mainmenu.html", locals())


def failed_my(request):
    cur_user = get_user(request)
    return render(request, "failed.html", locals())


def outpc(request):
    cur_user = get_user(request)
    pc_list = Pc.objects.all()
    return render(request, "bdedit/PC/outpc.html", locals())


def addpc_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Pc_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/PC/addpc.html", locals())
        return render(request, "bdedit/PC/addpc.html", locals())
    else:
        return redirect("../../failed")


def editpc_form(request, pc_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        pc = Pc.objects.get(id_pc=pc_name)
        form = Pc_Form(instance=pc)
        flag = False
        if request.method == "POST":
            form = Pc_Form(request.POST, instance=pc)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/PC/editpc.html", locals())
        return render(request, "bdedit/PC/editpc.html", locals())
    else:
        return redirect("../../../failed")


def deletepc(request, pc_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        pc = Pc.objects.get(pk=pc_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                pc.delete()
                flag = True
                return redirect("../outpc")
            else:
                return redirect("../outpc")
        return render(request, "bdedit/PC/deletepc.html", locals())
    else:
        return redirect("../../../failed")


def outdisc(request):
    cur_user = get_user(request)
    disc_list = Discount.objects.all()
    return render(request, "bdedit/Disc/outdisc.html", locals())


def adddisc_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Discount_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Disc/adddisc.html", locals())
        return render(request, "bdedit/Disc/adddisc.html", locals())
    else:
        return redirect("../../failed")


def editdisc_form(request, disc_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        disc = Discount.objects.get(id_card=disc_name)
        form = Discount_Form(instance=disc)
        flag = False
        if request.method == "POST":
            form = Discount_Form(request.POST, instance=disc)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Disc/editdisc.html", locals())
        return render(request, "bdedit/Disc/editdisc.html", locals())
    else:
        return redirect("../../../failed")


def deletedisc(request, disc_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        disc = Discount.objects.get(pk=disc_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                disc.delete()
                flag = True
                return redirect("../outdisc")
            else:
                return redirect("../outdisc")
        return render(request, "bdedit/Disc/deletedisc.html", locals())
    else:
        return redirect("../../../failed")


def outclient(request):
    cur_user = get_user(request)
    client_list = Client.objects.all()
    return render(request, "bdedit/Client/outclient.html", locals())


def addclient_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Client_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Client/addclient.html", locals())
        return render(request, "bdedit/Client/addclient.html", locals())
    else:
        return redirect("../../failed")


def editclient_form(request, client_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        client = Client.objects.get(id_client=client_name)
        form = Client_Form(instance=client)
        flag = False
        if request.method == "POST":
            form = Client_Form(request.POST, instance=client)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Client/editclient.html", locals())
        return render(request, "bdedit/Client/editclient.html", locals())
    else:
        return redirect("../../../failed")


def deleteclient(request, client_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        client = Client.objects.get(pk=client_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                client.delete()
                flag = True
                return redirect("../outclient")
            else:
                return redirect("../outclient")
        return render(request, "bdedit/Client/deleteclient.html", locals())
    else:
        return redirect("../../../failed")


def outrest(request):
    cur_user = get_user(request)
    rest_list = Receiving_transfer.objects.all()
    return render(request, "bdedit/Rest/outrest.html", locals())


def addrest_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Receiving_transfer_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Rest/addrest.html", locals())
        return render(request, "bdedit/Rest/addrest.html", locals())
    else:
        return redirect("../../failed")


def editrest_form(request, rest_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        rest = Receiving_transfer.objects.get(id_receivingtransfer=rest_name)
        form = Receiving_transfer_Form(instance=rest)
        flag = False
        if request.method == "POST":
            form = Receiving_transfer_Form(request.POST, instance=rest)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Rest/editrest.html", locals())
        return render(request, "bdedit/Rest/editrest.html", locals())
    else:
        return redirect("../../../failed")


def deleterest(request, rest_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        rest = Receiving_transfer.objects.get(pk=rest_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                rest.delete()
                flag = True
                return redirect("../outrest")
            else:
                return redirect("../outrest")
        return render(request, "bdedit/Rest/deleterest.html", locals())
    else:
        return redirect("../../../failed")


def outsera(request):
    cur_user = get_user(request)
    sera_list = Service_adress.objects.all()
    return render(request, "bdedit/Sera/outsera.html", locals())


def addsera_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Service_adress_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Sera/addsera.html", locals())
        return render(request, "bdedit/Sera/addsera.html", locals())
    else:
        return redirect("../../failed")


def editsera_form(request, sera_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        sera = Service_adress.objects.get(id_service_adress=sera_name)
        form = Service_adress_Form(instance=sera)
        flag = False
        if request.method == "POST":
            form = Service_adress_Form(request.POST, instance=sera)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Sera/editsera.html", locals())
        return render(request, "bdedit/Sera/editsera.html", locals())
    else:
        return redirect("../../../failed")


def deletesera(request, sera_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        sera = Service_adress.objects.get(pk=sera_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                sera.delete()
                flag = True
                return redirect("../outsera")
            else:
                return redirect("../outsera")
        return render(request, "bdedit/Sera/deletesera.html", locals())
    else:
        return redirect("../../../failed")


def outworker(request):
    cur_user = get_user(request)
    worker_list = Worker.objects.all()
    return render(request, "bdedit/Worker/outworker.html", locals())


def addworker_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Worker_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Worker/addworker.html", locals())
        return render(request, "bdedit/Worker/addworker.html", locals())
    else:
        return redirect("../../failed")


def editworker_form(request, worker_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        worker = Worker.objects.get(id_worker=worker_name)
        form = Worker_Form(instance=worker)
        flag = False
        if request.method == "POST":
            form = Worker_Form(request.POST, instance=worker)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Worker/editworker.html", locals())
        return render(request, "bdedit/Worker/editworker.html", locals())
    else:
        return redirect("../../../failed")


def deleteworker(request, worker_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        worker = Worker.objects.get(pk=worker_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                worker.delete()
                flag = True
                return redirect("../outworker")
            else:
                return redirect("../outworker")
        return render(request, "bdedit/Worker/deleteworker.html", locals())
    else:
        return redirect("../../../failed")


def outwork(request):
    cur_user = get_user(request)
    work_list = Work.objects.all()
    return render(request, "bdedit/Work/outwork.html", locals())


def addwork_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Work_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Work/addwork.html", locals())
        return render(request, "bdedit/Work/addwork.html", locals())
    else:
        return redirect("../../failed")


def editwork_form(request, work_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        work = Work.objects.get(id_work=work_name)
        form = Work_Form(instance=work)
        flag = False
        if request.method == "POST":
            form = Work_Form(request.POST, instance=work)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Work/editwork.html", locals())
        return render(request, "bdedit/Work/editwork.html", locals())
    else:
        return redirect("../../../failed")


def deletework(request, work_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        work = Work.objects.get(pk=work_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                work.delete()
                flag = True
                return redirect("../outwork")
            else:
                return redirect("../outwork")
        return render(request, "bdedit/Work/deletework.html", locals())
    else:
        return redirect("../../../failed")


def outcompl(request):
    cur_user = get_user(request)
    compl_list = Compl.objects.all()
    return render(request, "bdedit/Compl/outcompl.html", locals())


def addcompl_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Compl_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Compl/addcompl.html", locals())
        return render(request, "bdedit/Compl/addcompl.html", locals())
    else:
        return redirect("../../failed")


def editcompl_form(request, compl_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        compl = Compl.objects.get(id_compl=compl_name)
        form = Compl_Form(instance=compl)
        flag = False
        if request.method == "POST":
            form = Compl_Form(request.POST, instance=compl)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Compl/editcompl.html", locals())
        return render(request, "bdedit/Compl/editcompl.html", locals())
    else:
        return redirect("../../../failed")


def deletecompl(request, compl_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        compl = Compl.objects.get(pk=compl_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                compl.delete()
                flag = True
                return redirect("../outcompl")
            else:
                return redirect("../outcompl")
        return render(request, "bdedit/Compl/deletecompl.html", locals())
    else:
        return redirect("../../../failed")


def outsupp(request):
    cur_user = get_user(request)
    supp_list = Supplier.objects.all()
    return render(request, "bdedit/Supp/outsupp.html", locals())


def addsupp_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Supplier_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Supp/addsupp.html", locals())
        return render(request, "bdedit/Supp/addsupp.html", locals())
    else:
        return redirect("../../failed")


def editsupp_form(request, supp_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        supp = Supplier.objects.get(id_supplier=supp_name)
        form = Supplier_Form(instance=supp)
        flag = False
        if request.method == "POST":
            form = Supplier_Form(request.POST, instance=supp)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Supp/editsupp.html", locals())
        return render(request, "bdedit/Supp/editsupp.html", locals())
    else:
        return redirect("../../../failed")


def deletesupp(request, supp_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        supp = Supplier.objects.get(pk=supp_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                supp.delete()
                flag = True
                return redirect("../outsupp")
            else:
                return redirect("../outsupp")
        return render(request, "bdedit/Supp/deletesupp.html", locals())
    else:
        return redirect("../../../failed")


def outstor(request):
    cur_user = get_user(request)
    stor_list = Storage.objects.all()
    return render(request, "bdedit/Stor/outstor.html", locals())


def addstor_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Storage_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Stor/addstor.html", locals())
        return render(request, "bdedit/Stor/addstor.html", locals())
    else:
        return redirect("../../failed")


def editstor_form(request, stor_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        stor = Storage.objects.get(id_store_compl=stor_name)
        form = Storage_Form(instance=stor)
        flag = False
        if request.method == "POST":
            form = Storage_Form(request.POST, instance=stor)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Stor/editstor.html", locals())
        return render(request, "bdedit/Stor/editstor.html", locals())
    else:
        return redirect("../../../failed")


def deletestor(request, stor_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        stor = Storage.objects.get(pk=stor_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                stor.delete()
                flag = True
                return redirect("../outstor")
            else:
                return redirect("../outstor")
        return render(request, "bdedit/Stor/deletestor.html", locals())
    else:
        return redirect("../../../failed")


def outcomo(request):
    cur_user = get_user(request)
    como_list = Compl_order.objects.all()
    return render(request, "bdedit/Como/outcomo.html", locals())


def addcomo_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Compl_order_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Como/addscomo.html", locals())
        return render(request, "bdedit/Como/addcomo.html", locals())
    else:
        return redirect("../../failed")


def editcomo_form(request, como_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        como = Compl_order.objects.get(id_compl_order=como_name)
        form = Compl_order_Form(instance=como)
        flag = False
        if request.method == "POST":
            form = Compl_order_Form(request.POST, instance=como)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Como/editcomo.html", locals())
        return render(request, "bdedit/Como/editcomo.html", locals())
    else:
        return redirect("../../../failed")


def deletecomo(request, como_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        como = Compl_order.objects.get(pk=como_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                como.delete()
                flag = True
                return redirect("../outcomo")
            else:
                return redirect("../outcomo")
        return render(request, "bdedit/Como/deletecomo.html", locals())
    else:
        return redirect("../../../failed")


def outorse(request):
    cur_user = get_user(request)
    orse_list = Ordering_services.objects.all()
    return render(request, "bdedit/Orse/outorse.html", locals())


def addorse_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Ordering_services_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Orse/addsorse.html", locals())
        return render(request, "bdedit/Orse/addorse.html", locals())
    else:
        return redirect("../../failed")


def editorse_form(request, orse_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        orse = Ordering_services.objects.get(id_ordering_services=orse_name)
        form = Ordering_services_Form(instance=orse)
        flag = False
        if request.method == "POST":
            form = Ordering_services_Form(request.POST, instance=orse)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Orse/editorse.html", locals())
        return render(request, "bdedit/Orse/editorse.html", locals())
    else:
        return redirect("../../../failed")


def deleteorse(request, orse_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        orse = Ordering_services.objects.get(pk=orse_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                orse.delete()
                flag = True
                return redirect("../outorse")
            else:
                return redirect("../outorse")
        return render(request, "bdedit/Orse/deleteorse.html", locals())
    else:
        return redirect("../../../failed")


def outorder(request):
    cur_user = get_user(request)
    order_list = Order.objects.all()
    return render(request, "bdedit/Order/outorder.html", locals())


def addorder_form(request):
    cur_user = get_user(request)
    if cur_user.is_staff:
        form = Order_Form(request.POST or None)
        flag = False
        if request.method == "POST":
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Order/addorder.html", locals())
        return render(request, "bdedit/Order/addorder.html", locals())
    else:
        return redirect("../../failed")


def editorder_form(request, order_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        order = Order.objects.get(id_order=order_name)
        form = Order_Form(instance=order)
        flag = False
        if request.method == "POST":
            form = Order_Form(request.POST, instance=order)
            if form.is_valid():
                form.save()
                flag = True
            else:
                return render(request, "bdedit/Order/editorder.html", locals())
        return render(request, "bdedit/Order/editorder.html", locals())
    else:
        return redirect("../../../failed")


def deleteorder(request, order_name):
    cur_user = get_user(request)
    if cur_user.is_staff:
        order = Order.objects.get(pk=order_name)
        flag = False
        if request.method == "POST":
            print(request.POST)
            if 'Yes' in request.POST.keys() and request.POST['Yes']:
                order.delete()
                flag = True
                return redirect("../outorder")
            else:
                return redirect("../outorder")
        return render(request, "bdedit/Order/deleteorder.html", locals())
    else:
        return redirect("../../../failed")


def login_my(request):
    if request.user.id is not None:
        logout(request)
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=raw_password)
        if user and user.is_active:
            login(request, user)
            return redirect('mainmenu')
    return render(request, 'log_in.html', locals())


def logout_my(request):
    logout(request)
    return redirect('mainmenu')