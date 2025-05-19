### Assignment 1: 
    Create Product Model with id, name, price, in_stock

### Assignment 2:
    Create Employee Model
    - Fields
        - id: int
        - name: str (min 3 characters)
        - department: optional str (default 'General')
        - salary: float (must be >= 10000)     

### Assignment 3:
    Create a Booking Model
    Fields: 
        - user_id : int
        - room_id : int
        - nights : int (must be >=1)
        - rate_per_night : float 
        - Also add computed_field: total_amount = nights * rate_per_night 

### Assignment 4: 
    Create a model
        - Each Course has modules
        - Each modules has lessons 