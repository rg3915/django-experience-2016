import csv
from django.contrib.auth.models import User
users = User.objects.all().values_list('id', 'username', 'email', 'date_joined')
with open('users.csv', 'w', newline='') as csvfile:
    user_writer = csv.writer(csvfile, delimiter=';')
    for user in users:
        user_writer.writerow(user)


# done
