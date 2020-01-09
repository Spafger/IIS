from django.db import models

# Create your models here.


class Pc(models.Model):
    id_pc = models.AutoField(primary_key=True)
    description_pc = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id_pc)


class Discount(models.Model):
    id_card = models.AutoField(primary_key=True)
    bonuses = models.IntegerField()
    reception_date = models.DateField()

    def __str__(self):
        return str(self.id_card) + ";  " + str(self.bonuses)


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=12)
    card_id = models.ForeignKey(Discount, on_delete=models.CASCADE)
    fio_client = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id_client) + ", " + self.fio_client


class Receiving_transfer(models.Model):
    id_receivingtransfer = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    pc_id = models.ForeignKey(Pc, on_delete=models.CASCADE)
    date_receive = models.DateField()

    def __str__(self):
        return str(self.id_receivingtransfer) + ", " + str(self.date_receive)


class Service_adress(models.Model):
    id_service_adress = models.AutoField(primary_key=True)
    service_adress = models.CharField(max_length=128)
    phone_number_adress = models.CharField(max_length=13)

    def __str__(self):
        return self.service_adress


class Worker(models.Model):
    id_worker = models.AutoField(primary_key=True)
    post = models.CharField(max_length=64)
    phone_number_worker = models.CharField(max_length=13)
    account_number_worker = models.CharField(max_length=20)
    passport_worker = models.CharField(max_length=128)
    dofb_worker = models.DateField()
    fio_worker = models.CharField(max_length=128)

    def __str__(self):
        return self.fio_worker


class Work(models.Model):
    id_work = models.AutoField(primary_key=True)
    detail = models.CharField(max_length=128)
    work_name = models.CharField(max_length=64)
    work_term = models.CharField(max_length=128)
    work_price = models.IntegerField()

    def __str__(self):
        return self.detail + ", " + self.work_name


class Compl(models.Model):
    id_compl = models.AutoField(primary_key=True)
    compl_name = models.CharField(max_length=64)
    compl_article = models.CharField(max_length=20)
    compl_price = models.IntegerField()
    compl_maker = models.CharField(max_length=64)
    compl_description = models.CharField(max_length=128)

    def __str__(self):
        return self.compl_name


class Supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=128)
    supplier_contact = models.CharField(max_length=64)

    def __str__(self):
        return self.supplier_name


class Storage(models.Model):
    id_store_compl = models.AutoField(primary_key=True)
    compl_id = models.ForeignKey(Compl, on_delete=models.CASCADE)
    stock_balance = models.IntegerField()
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.compl_id) + ", " + str(self.stock_balance)


class Compl_order(models.Model):
    id_compl_order = models.AutoField(primary_key=True)
    total_cost = models.IntegerField()
    store_compl_id = models.ForeignKey(Storage, on_delete=models.CASCADE)
    amount_compl = models.IntegerField()

    def __str__(self):
        return str(self.id_compl_order) + ", " + str(self.store_compl_id)


class Ordering_services(models.Model):
    id_ordering_services = models.AutoField(primary_key=True)
    work_id = models.ForeignKey(Work, on_delete=models.CASCADE)
    work_price = models.IntegerField()
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    compl_order_id = models.ForeignKey(Compl_order, on_delete=models.CASCADE)
    note_ordering_services = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id_ordering_services)


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    sum_order = models.IntegerField()
    service_adress_id = models.ForeignKey(Service_adress, on_delete=models.CASCADE)
    ordering_services_id = models.ForeignKey(Ordering_services, on_delete=models.CASCADE)
    receivingtransfer_id = models.ForeignKey(Receiving_transfer, on_delete=models.CASCADE)
    date_order = models.DateField()

    def __str__(self):
        return str(self.id_order)
