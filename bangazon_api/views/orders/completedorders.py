Class CompletedOrderList(view):
    def get(self, request):
        with connection.cursor() as db_cursor:
            
            db_cursor.execute("""
                              )