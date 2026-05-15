// use database
use inventory_management;

// create collections
db.createCollection("products");
db.createCollection("warehouses");
db.createCollection("suppliers");
db.createCollection("stock_movements");
db.createCollection("audit_logs");

// insert suppliers
db.suppliers.insertMany([
  { supplier_id: 1, supplier_name: "ABC Suppliers", contact_email: "abc@gmail.com" },
  { supplier_id: 2, supplier_name: "Global Traders", contact_email: "global@gmail.com" },
  { supplier_id: 3, supplier_name: "Fresh Supply Co", contact_email: "fresh@gmail.com" }
]);

// insert products
db.products.insertMany([
  { product_id: 1, product_name: "Laptop", supplier_id: 1, reorder_level: 10 },
  { product_id: 2, product_name: "Mouse", supplier_id: 1, reorder_level: 20 },
  { product_id: 3, product_name: "Keyboard", supplier_id: 2, reorder_level: 15 },
  { product_id: 4, product_name: "Monitor", supplier_id: 2, reorder_level: 8 },
  { product_id: 5, product_name: "Printer", supplier_id: 3, reorder_level: 5 }
]);

// insert warehouses
db.warehouses.insertMany([
  { warehouse_id: 1, warehouse_name: "Main Warehouse", location: "Chennai" },
  { warehouse_id: 2, warehouse_name: "Backup Warehouse", location: "Bangalore" }
]);

// insert stock movements
db.stock_movements.insertMany([
  { movement_id: 1, product_id: 1, warehouse_id: 1, quantity: 50, movement_type: "IN", movement_date: "2026-01-10" },
  { movement_id: 2, product_id: 2, warehouse_id: 1, quantity: 30, movement_type: "IN", movement_date: "2026-01-12" },
  { movement_id: 3, product_id: 3, warehouse_id: 2, quantity: 20, movement_type: "IN", movement_date: "2026-01-15" },
  { movement_id: 4, product_id: 1, warehouse_id: 1, quantity: 10, movement_type: "OUT", movement_date: "2026-01-18" },
  { movement_id: 5, product_id: 2, warehouse_id: 1, quantity: 5, movement_type: "OUT", movement_date: "2026-01-20" }
]);

// audit logs
db.audit_logs.insertMany([
  {
    log_id: 1,
    product_id: 1,
    warehouse_id: 1,
    adjustment: -5,
    reason: "damaged items",
    timestamp: "2026-02-01"
  },
  {
    log_id: 2,
    product_id: 2,
    warehouse_id: 1,
    adjustment: 10,
    reason: "new stock arrival",
    timestamp: "2026-02-03"
  },
  {
    log_id: 3,
    product_id: 3,
    warehouse_id: 2,
    adjustment: -2,
    reason: "returned defective",
    timestamp: "2026-02-05"
  }
]);

// indexes
db.products.createIndex({ product_id: 1 });
db.warehouses.createIndex({ warehouse_id: 1 });
db.stock_movements.createIndex({ product_id: 1 });
db.stock_movements.createIndex({ warehouse_id: 1 });
db.audit_logs.createIndex({ product_id: 1 });
db.audit_logs.createIndex({ warehouse_id: 1 });
