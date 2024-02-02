import mysql.connector


def get_all_products():
    cnx = mysql.connector.connect(user='root', password='root123',
                                host='127.0.0.1',
                                database='gs_ms')

    cursor =cnx.cursor()

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


    cnx.close()

    return response

if __name__=='__main__':
    print(get_all_products())