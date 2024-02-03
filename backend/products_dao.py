from sql_connection import get_sql_connection


def get_all_products(connection):
    

    cursor = connection.cursor()

    query=("Select products.Products_id,products.Pname,products.uom_id,products.Priceperunit,uom.uom_name "
    "from products inner join uom on products.uom_id=uom.uom_id")

    cursor.execute(query)

    response = []
    for (Products_id,Pname,uom_id,Priceperunit,uom_name) in cursor:
       response.append(
           {
               'products_id' : Products_id,
               'Pname' : Pname,
               'uom_id' : uom_id,
               'Priceperunit' : Priceperunit,
               'uom_name' : uom_name,
           }
       )

    return response

def inser_new_product(connection,product):
    cursor =connection.cursor()

    query = ("Insert into products "
             "(Pname,uom_id,Priceperunit)"
             "values (%s,%s,%s)")
    data = (product['Product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid
def delete_product(connection,Products_id):
    cursor=connection.cursor()
    query=("DELETE FROM products where Products_id=" + str(Products_id))
    cursor.execute(query)
    connection.commit()


if __name__=='__main__':
    connection=get_sql_connection()
    print(delete_product(connection,5))