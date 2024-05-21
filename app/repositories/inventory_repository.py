from app.db.mysql import connect_to_db
from MySQLdb.cursors import Cursor

class InventoryRepository:
    @staticmethod
    def get_product_by_id(id):
        conn = connect_to_db()
        
        cursor: Cursor = conn.cursor()

        query = """select products.ID, products.name, sku, description, cost, price, stocks, suppliers.name, suppliers.ID 
        from products 
        left join suppliers on products.supplier_id=suppliers.ID 
        where products.ID=%s
        """

        cursor.execute(query, [id])
        single_product = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if not single_product:
            return {"message": "Item not found", "status": 0}
        
        return {
            "ID": single_product[0], 
            'name': single_product[1], 
            'sku': single_product[2], 
            'description': single_product[3],
            'cost': single_product[4],
            'price': single_product[5],
            'stocks': single_product[6],
            'supplier_name': single_product[7],
            'supplier_id': single_product[8]
            }
    
    @staticmethod
    def update_by_id(id, name, description, cost, price, stocks):

        single_product = None
        
        conn = connect_to_db()
        
        cursor: Cursor = conn.cursor()

        query="""UPDATE products
        SET name=%s, description=%s, cost=%s, price=%s, stocks=%s
        WHERE ID=%s
        """

        updated = cursor.execute(query, (name, description, cost, price, stocks, id))

        if updated:
            getQuery = "select * from products where ID=%s"
            cursor.execute(getQuery, [id])

            single_product = cursor.fetchone()
            single_product =  {
            "ID": single_product[0], 
            'name': single_product[1], 
            'description': single_product[2], 
            'cost': single_product[3],
            'price': single_product[4],
            'stocks': single_product[5],
            'supplier_id': single_product[6],
            'sku': single_product[7],
            }

        conn.commit()

        cursor.close()
        conn.close()


        return single_product
