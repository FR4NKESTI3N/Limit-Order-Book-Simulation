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
