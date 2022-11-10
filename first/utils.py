import csv
import os
import shutil
import pandas as pd
from .models import FileModel

def results():

    if os.path.isfile("media/file/order_prices.csv"):
        os.remove("media/file/order_prices.csv")
    if os.path.isfile("media/file/product_customers.csv"):
        os.remove("media/file/product_customers.csv")
    if os.path.isfile("media/file/customer_ranking.csv"):
        os.remove("media/file/customer_ranking.csv")

    data_p = []

    with open("media/file/orders.csv", "r") as order:
        reader = csv.DictReader(order)

        for row in reader:
            value = row['products'].replace(" ", "")

            v0 = value.count("0") * 2.981163654411736
            v1 = value.count("1") * 6.490396437000094
            v2 = value.count("2") * 2.9037321212561906
            v3 = value.count("3") * 8.90156976370351
            v4 = value.count("4") * 9.806494914226443
            v5 = value.count("5") * 10.435252185512562
            final_value = v0+v1+v2+v3+v4+v5
            id = row['id']
            data_p.append((id, final_value))

    del reader
    order.close()
    del order

    new_csv = open("media/file/order_prices.csv", "w", newline='')
    writer = csv.writer(new_csv)
    writer.writerow(['id', 'total'])
    writer.writerows(data_p)
    del writer
    new_csv.close()

    data_c = []

    with open("media/file/orders.csv", "r") as order:
        reader = csv.DictReader(order)
        dt0 = []
        dt1 = []
        dt2 = []
        dt3 = []
        dt4 = []
        dt5 = []
        for row in reader:
            id_customer = row['customer']
            products = row['products'].replace(" ", "")

            if products.count("0") >= 1:
                dt0.append(id_customer)
            if products.count("1") >= 1:
                dt1.append(id_customer)
            if products.count("2") >= 1:
                dt2.append(id_customer)
            if products.count("3") >= 1:
                dt3.append(id_customer)
            if products.count("4") >= 1:
                dt4.append(id_customer)
            if products.count("5") >= 1:
                dt5.append(id_customer)

    data_c.append(("0", ' '.join(dt0)))
    data_c.append(("1", ' '.join(dt1)))
    data_c.append(("2", ' '.join(dt2)))
    data_c.append(("3", ' '.join(dt3)))
    data_c.append(("4", ' '.join(dt4)))
    data_c.append(("5", ' '.join(dt5)))

    del reader
    order.close()
    del order

    new_csv = open("media/file/product_customers.csv", "w", newline='')
    writer = csv.writer(new_csv)
    writer.writerow(['id', 'customer_ids'])
    writer.writerows(data_c)
    del writer
    new_csv.close()

    data_t = []

    with open("media/file/orders.csv", "r") as order:
        reader = csv.DictReader(order)

        for row in reader:
            value = row['products'].replace(" ", "")

            v0 = value.count("0") * 2.981163654411736
            v1 = value.count("1") * 6.490396437000094
            v2 = value.count("2") * 2.9037321212561906
            v3 = value.count("3") * 8.90156976370351
            v4 = value.count("4") * 9.806494914226443
            v5 = value.count("5") * 10.435252185512562
            final_value = v0+v1+v2+v3+v4+v5
            id_c = row['customer']
            with open("media/file/customers.csv") as customer:
                read = csv.DictReader(customer)
                for c in read:
                    if c['id'] == id_c:
                        data_t.append((id_c, c['firstname'], c['lastname'], final_value))

    del read
    customer.close()
    del customer
    del reader
    order.close()
    del order

    new_csv = open("media/file/customer_ranking_p.csv", "w", newline='')
    writer = csv.writer(new_csv)
    writer.writerow(['id', 'name', 'lastname', 'total'])
    writer.writerows(data_t)
    del writer
    new_csv.close()

    df = pd.read_csv("media/file/customer_ranking_p.csv")
    sorted_df = df.sort_values(by=['total'], ascending=False)
    sorted_df.to_csv('media/file/customer_ranking.csv', index=False)

    FileModel.objects.all().delete()


    archivo1 = FileModel(file="file/order_prices.csv", title="Precios por ID del pedido")
    archivo1.save()

    archivo2 = FileModel(file="file/product_customers.csv", title="Productos por consumidor")
    archivo2.save()

    archivo3 = FileModel(file="file/customer_ranking.csv", title="Ranking de gastos por consumidor")
    archivo3.save()

    os.remove("media/file/customer_ranking_p.csv")
    os.remove("media/file/customers.csv")
    os.remove("media/file/orders.csv")
    os.remove("media/file/products.csv")






