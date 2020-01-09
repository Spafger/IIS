from django.forms import *
from LabaUD.models import *


class Receiving_transfer_Form(ModelForm):
    class Meta:
        model = Receiving_transfer
        fields = ["id_receivingtransfer", "client_id", "pc_id", "date_receive"]


class Pc_Form(ModelForm):
    class Meta:
        model = Pc
        fields = ["id_pc", "description_pc"]


class Client_Form(ModelForm):
    class Meta:
        model = Client
        fields = ["id_client", "phone_number", "card_id", "fio_client"]


class Discount_Form(ModelForm):
    class Meta:
        model = Discount
        fields = ["id_card", "bonuses", "reception_date"]


class Order_Form(ModelForm):
    class Meta:
        model = Order
        fields = ["id_order", "sum_order", "service_adress_id", "ordering_services_id", "receivingtransfer_id", "date_order"]


class Service_adress_Form(ModelForm):
    class Meta:
        model = Service_adress
        fields = ["id_service_adress", "service_adress", "phone_number_adress"]


class Ordering_services_Form(ModelForm):
    class Meta:
        model = Ordering_services
        fields = ["id_ordering_services", "work_id", "work_price", "worker_id", "compl_order_id", "note_ordering_services"]


class Worker_Form(ModelForm):
    class Meta:
        model = Worker
        fields = ["id_worker", "post", "phone_number_worker", "account_number_worker", "passport_worker", "dofb_worker", "fio_worker"]


class Work_Form(ModelForm):
    class Meta:
        model = Work
        fields = ["id_work", "detail", "work_name", "work_term", "work_price"]


class Compl_order_Form(ModelForm):
    class Meta:
        model = Compl_order
        fields = ["id_compl_order", "total_cost", "store_compl_id", "amount_compl"]


class Storage_Form(ModelForm):
    class Meta:
        model = Storage
        fields = ["id_store_compl", "compl_id", "stock_balance", "supplier_id"]


class Compl_Form(ModelForm):
    class Meta:
        model = Compl
        fields = ["id_compl", "compl_name", "compl_article", "compl_price", "compl_maker", "compl_description"]


class Supplier_Form(ModelForm):
    class Meta:
        model = Supplier
        fields = ["id_supplier", "supplier_name", "supplier_contact"]


class LoginForm(Form):
    username = CharField(label='username', max_length=100)
    password = CharField(label='password', widget=PasswordInput)
