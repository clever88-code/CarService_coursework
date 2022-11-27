
#     auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True, blank=True)
#     record = models.ForeignKey(Records, on_delete=models.CASCADE, null=True, blank=True)
#     completed_work = models.TextField('Выполненная работа', default="")
#     price = models.IntegerField('Стоимость работы')
#
#     class Meta:
#         db_table = 'orders'