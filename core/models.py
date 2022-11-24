from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cars(models.Model):
    car_number = models.CharField('Номера автомобиля', default="", max_length=9)
    auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True, blank=True)
    firms = models.CharField('Фирма автомобиля', default="", max_length=40)
    mark = models.CharField('Марка автомобиля', default="", max_length=255)

    class Meta:
        db_table = 'cars'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MachineTools(models.Model):
    name = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'machine tools'


class Materials(models.Model):
    name = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'materials'


class Orders(models.Model):
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, to_field=None)
    record = models.ForeignKey('Records', models.DO_NOTHING, to_field=None)

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersMachineTools(models.Model):
    order = models.OneToOneField(Orders, models.DO_NOTHING, primary_key=True)
    machine_tool = models.ForeignKey(MachineTools, models.DO_NOTHING, to_field=None)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders_machine tools'


class OrdersMaterials(models.Model):
    order = models.OneToOneField(Orders, models.DO_NOTHING, primary_key=True)
    materials = models.ForeignKey(Materials, models.DO_NOTHING, to_field=None)

    class Meta:
        managed = False
        db_table = 'orders_materials'


class Records(models.Model):
    car = models.ForeignKey(Cars, models.DO_NOTHING, to_field=None)
    date = models.TextField()
    record_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'records'
