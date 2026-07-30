"""
seed.py

Script to initialize SQLite database tables and seed sample e-commerce product data.
"""

from backend.database.connection import engine, Base, SessionLocal
from backend.database.models import Platform, Product, Specification


def init_db():
    """Creates database tables and seeds initial data."""
    print("Initializing SQLite database tables...")
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Check if platforms already exist
        if db.query(Platform).first():
            print("Database already contains data. Skipping seed.")
            return

        print("Seeding e-commerce platforms...")
        platforms = [
            Platform(name="Amazon", website_url="https://www.amazon.in"),
            Platform(name="Flipkart", website_url="https://www.flipkart.com"),
            Platform(name="Croma", website_url="https://www.croma.com"),
        ]
        db.add_all(platforms)
        db.commit()

        print("Seeding product catalog...")
        sample_products = [
            {
                "name": "Apple iPhone 16",
                "brand": "Apple",
                "platform": "Amazon",
                "price": 74999.0,
                "rating": 4.7,
                "reviews_count": 15234,
                "category": "Mobile",
                "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400",
                "delivery_info": "Free Tomorrow Delivery",
                "offers": "10% Instant Bank Discount",
                "description": "Latest Apple smartphone powered by the A18 chip with camera control and advanced performance.",
                "url": "https://www.amazon.in",
                "spec": {
                    "storage": "128 GB",
                    "ram": "8 GB",
                    "display": "6.1-inch Super Retina XDR OLED",
                    "processor": "Apple A18",
                    "camera": "48 MP + 12 MP",
                    "battery": "3561 mAh",
                    "color": "Black"
                }
            },
            {
                "name": "Apple iPhone 16",
                "brand": "Apple",
                "platform": "Flipkart",
                "price": 73999.0,
                "rating": 4.6,
                "reviews_count": 13890,
                "category": "Mobile",
                "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400",
                "delivery_info": "Delivery in 2 Days",
                "offers": "₹3000 Exchange Bonus",
                "description": "Apple iPhone 16 with premium design, dynamic island, and outstanding battery life.",
                "url": "https://www.flipkart.com",
                "spec": {
                    "storage": "128 GB",
                    "ram": "8 GB",
                    "display": "6.1-inch Super Retina XDR OLED",
                    "processor": "Apple A18",
                    "camera": "48 MP + 12 MP",
                    "battery": "3561 mAh",
                    "color": "Ultramarine"
                }
            },
            {
                "name": "Samsung Galaxy S25",
                "brand": "Samsung",
                "platform": "Amazon",
                "price": 81999.0,
                "rating": 4.8,
                "reviews_count": 9845,
                "category": "Mobile",
                "image_url": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400",
                "delivery_info": "Free Tomorrow Delivery",
                "offers": "Free Galaxy Buds FE",
                "description": "Samsung flagship smartphone with AI Galaxy capabilities, Snapdragon 8 Elite, and Dynamic AMOLED.",
                "url": "https://www.amazon.in",
                "spec": {
                    "storage": "256 GB",
                    "ram": "12 GB",
                    "display": "6.2-inch Dynamic AMOLED 2X",
                    "processor": "Snapdragon 8 Elite",
                    "camera": "50 MP + 12 MP + 10 MP",
                    "battery": "4000 mAh",
                    "color": "Silver Shadow"
                }
            },
            {
                "name": "Samsung Galaxy S25",
                "brand": "Samsung",
                "platform": "Flipkart",
                "price": 80999.0,
                "rating": 4.7,
                "reviews_count": 8742,
                "category": "Mobile",
                "image_url": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400",
                "delivery_info": "Delivery in 2 Days",
                "offers": "₹5000 Exchange Bonus",
                "description": "Premium flagship Samsung phone with pro-grade nightography camera and long battery performance.",
                "url": "https://www.flipkart.com",
                "spec": {
                    "storage": "256 GB",
                    "ram": "12 GB",
                    "display": "6.2-inch Dynamic AMOLED 2X",
                    "processor": "Snapdragon 8 Elite",
                    "camera": "50 MP + 12 MP + 10 MP",
                    "battery": "4000 mAh",
                    "color": "Sparkling Black"
                }
            },
            {
                "name": "OnePlus 13",
                "brand": "OnePlus",
                "platform": "Amazon",
                "price": 69999.0,
                "rating": 4.6,
                "reviews_count": 6321,
                "category": "Mobile",
                "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400",
                "delivery_info": "Free Tomorrow Delivery",
                "offers": "No Cost EMI up to 12 Months",
                "description": "Ultra-fast flagship mobile with 100W SUPERVOOC charging, Hasselblad camera, and 6000 mAh battery.",
                "url": "https://www.amazon.in",
                "spec": {
                    "storage": "256 GB",
                    "ram": "12 GB",
                    "display": "6.82-inch 120Hz LTPO AMOLED",
                    "processor": "Snapdragon 8 Elite",
                    "camera": "50 MP + 50 MP + 50 MP",
                    "battery": "6000 mAh",
                    "color": "Emerald Green"
                }
            },
            {
                "name": "Apple MacBook Air M3",
                "brand": "Apple",
                "platform": "Amazon",
                "price": 104900.0,
                "rating": 4.9,
                "reviews_count": 4120,
                "category": "Laptop",
                "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400",
                "delivery_info": "Free Tomorrow Delivery",
                "offers": "Flat ₹5000 Bank Discount",
                "description": "Ultra-thin laptop powered by Apple M3 chip with up to 18 hours of battery life.",
                "url": "https://www.amazon.in",
                "spec": {
                    "storage": "256 GB SSD",
                    "ram": "8 GB Unified",
                    "display": "13.6-inch Liquid Retina",
                    "processor": "Apple M3 (8-core CPU)",
                    "camera": "1080p FaceTime HD",
                    "battery": "up to 18 Hours",
                    "color": "Midnight"
                }
            },
            {
                "name": "Apple AirPods Pro 2",
                "brand": "Apple",
                "platform": "Amazon",
                "price": 22999.0,
                "rating": 4.8,
                "reviews_count": 19234,
                "category": "Accessories",
                "image_url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400",
                "delivery_info": "Free Tomorrow Delivery",
                "offers": "₹1000 Coupon Discount",
                "description": "Wireless noise-canceling earbuds with H2 chip, personalized spatial audio, and USB-C case.",
                "url": "https://www.amazon.in",
                "spec": {
                    "storage": "-",
                    "ram": "-",
                    "display": "-",
                    "processor": "Apple H2 Chip",
                    "camera": "-",
                    "battery": "up to 30 Hours",
                    "color": "White"
                }
            },
            {
                "name": "Sony WH-1000XM5 Headphones",
                "brand": "Sony",
                "platform": "Croma",
                "price": 29990.0,
                "rating": 4.7,
                "reviews_count": 8410,
                "category": "Accessories",
                "image_url": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400",
                "delivery_info": "Express Delivery",
                "offers": "10% Cashback on HDFC",
                "description": "Industry-leading noise canceling over-ear headphones with 30-hour battery life and multi-point connection.",
                "url": "https://www.croma.com",
                "spec": {
                    "storage": "-",
                    "ram": "-",
                    "display": "-",
                    "processor": "Integrated Processor V1",
                    "camera": "-",
                    "battery": "30 Hours",
                    "color": "Silver"
                }
            }
        ]

        for p_data in sample_products:
            spec_data = p_data.pop("spec")
            product = Product(**p_data)
            db.add(product)
            db.flush()  # gets product.id

            spec = Specification(product_id=product.id, **spec_data)
            db.add(spec)

        db.commit()
        print("Database seeded successfully with sample products!")

    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
