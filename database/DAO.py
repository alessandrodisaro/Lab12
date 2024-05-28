from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNazioni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct(Country)
                from go_retailers gr """

        cursor.execute(query)
        results = []
        for row in cursor:
            results.append(row["Country"])

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """select distinct(year(Date))
                    from go_daily_sales gds  """

        cursor.execute(query)
        results = []
        for row in cursor:
            results.append(row[0])

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def getAllNodes(nazione ):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select  *
                    from go_retailers gr 
                    where Country = %s  """

        cursor.execute(query, (nazione, ))
        results = []
        for row in cursor:
            results.append(Retailer(**row))

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def getAllEdges(anno, nazione):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # query = """select  gds1.Retailer_code as R1, gds2.Retailer_code as R2, gds1.Product_number, count(*)
        #             from go_daily_sales gds1, go_daily_sales gds2
        #             where gdS1.Retailer_code < gds2.Retailer_code
        #             and gds1.Retailer_code in (select gr3.Retailer_code from go_daily_sales gds3,go_retailers gr3
        #                                                                 where gds3.Retailer_code = gr3.Retailer_code
        #                                                                 and gr3.Country = %s
        #                                                                 and year(gds3.Date)=%s)
        #             and gds2.Retailer_code in (select gr4.Retailer_code from go_daily_sales gds4,go_retailers gr4
        #                                                                 where gds4.Retailer_code = gr4.Retailer_code
        #                                                                 and gr4.Country = %s
        #                                                                 and year(gds4.Date)=%s)
        #             and gds1.Product_number = gds2.Product_number
        #             group by gds1.Retailer_code, gds2.Retailer_code , gds1.Product_number """

        query = """
        """

        # cursor.execute(query, (nazione, anno, nazione, anno)) con la prima query
        cursor.execute(query, ())
        results = []
        for row in cursor:
            results.append((row["R1"], row["R2"], row["peso"]))

        cursor.close()
        cnx.close()

        return results


    @staticmethod
    def getArco(r0, r1, anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select gds1.Retailer_code as R1, gds2.Retailer_code as R2, count(distinct (gds1.Product_number)) as peso
                    from go_daily_sales gds1, go_daily_sales gds2
                    where gds1.Retailer_code = %s and gds2.Retailer_code = %s
                    and gds1.Product_number = gds2.product_number
                    and year(gds1.Date) = %s and year(gds2.Date) = %s                      
                                    """


        cursor.execute(query, (r0.Retailer_code, r1.Retailer_code, anno, anno))
        results = []
        for row in cursor:
            results.append((row["R1"], row["R2"], row["peso"]))

        cursor.close()
        cnx.close()

        return results






