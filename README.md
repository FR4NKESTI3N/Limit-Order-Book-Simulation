# Limit-Order-Book-Simulation

## Attributes
  order_book: Hash table with key as order_id
  
  asks: List that stores ask order order_id in ascending order with respect to order price
  
  bids: List that stores bid order order_id in ascending order with respect to order price
  
## Methods
  bbo: returns Best bid and best ask order prices. Has a property decorator so is accessed as an attribute
  
  add_limit_order: add new order
  
  cancel_limit_order: delete an order
  
  place_market_order: place a market order
  
  printBook: print: formatted output of order_book

## Output
```
lob_example = Limit()
lob_example.add_limit_order('ask', 'alice', 10, 100)
lob_example.add_limit_order('ask', 'bob', 5, 90)
lob_example.add_limit_order('bid', 'charles', 20, 85)
lob_example.add_limit_order('bid', 'dave', 10, 80)
lob_example.printBook()
```
```
  asks:[
          {
                   order_id : 1
                   user_id : alice
                   quantity : 10
                   price : 100
          },
          {
                   order_id : 2
                   user_id : bob
                   quantity : 5
                   price : 90
          },
  ],
  bids:[
          {
                   order_id : 3
                   user_id : charles
                   quantity : 20
                   price : 85
          },
          {
                   order_id : 4
                   user_id : dave
                   quantity : 10
                   price : 80
          },
  ]
```

```
lob_example.add_limit_order('ask', 'eve', 10, 95)
lob_example.printBook()
```
```
  asks:[
          {
                   order_id : 1
                   user_id : alice
                   quantity : 10
                   price : 100
          },
          {
                   order_id : 5
                   user_id : eve
                   quantity : 10
                   price : 95
          },
          {
                   order_id : 2
                   user_id : bob
                   quantity : 5
                   price : 90
          },
  ],
  bids:[
          {
                   order_id : 3
                   user_id : charles
                   quantity : 20
                   price : 85
          },
          {
                   order_id : 4
                   user_id : dave
                   quantity : 10
                   price : 80
          },
  ]
```

```
lob_example.place_market_order('ask', 12)
lob_example.printBook()
```
```
  asks:[
          {
                   order_id : 1
                   user_id : alice
                   quantity : 10
                   price : 100
          },
          {
                   order_id : 5
                   user_id : eve
                   quantity : 3
                   price : 95
          },
  ],
  bids:[
          {
                   order_id : 3
                   user_id : charles
                   quantity : 20
                   price : 85
          },
          {
                   order_id : 4
                   user_id : dave
                   quantity : 10
                   price : 80
          },
  ]
```

```
lob_example.cancel_limit_order(3)
lob_example.printBook()
```    
```
  asks:[
          {
                   order_id : 1
                   user_id : alice
                   quantity : 10
                   price : 100
          },
          {
                   order_id : 5
                   user_id : eve
                   quantity : 3
                   price : 95
          },
  ],
  bids:[
          {
                   order_id : 4
                   user_id : dave
                   quantity : 10
                   price : 80
          },
  ]
```

```
lob_example.add_limit_order('bid', 'dave', 3, 95)
lob_example.printBook()
```

```
  asks:[
          {
                   order_id : 1
                   user_id : alice
                   quantity : 10
                   price : 100
          },
  ],
  bids:[
          {
                   order_id : 4
                   user_id : dave
                   quantity : 10
                   price : 80
          },
  ]
```
