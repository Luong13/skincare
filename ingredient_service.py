
import sqlite3

def initialize_db():
    connection = sqlite3.connect('ingredients.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE,
                        category TEXT,
                        benefits TEXT,
                        risks TEXT
                    )''')
    connection.commit()
    connection.close()

def seed_data():
    connection = sqlite3.connect('ingredients.db')
    cursor = connection.cursor()
    sample_data = [
        ("Hyaluronic Acid", "Humectant", "Hydration", "None known"),
        ("Retinol", "Active Ingredient", "Anti-aging, acne treatment", "Irritation, dryness"),
        ("Niacinamide", "Vitamin", "Brightening, hydration", "None known"),
    ]
    for name, category, benefits, risks in sample_data:
        try:
            cursor.execute('INSERT INTO ingredients (name, category, benefits, risks) VALUES (?, ?, ?, ?)', (name, category, benefits, risks))
        except sqlite3.IntegrityError:
            pass  # Ignore duplicate entries
    connection.commit()
    connection.close()

def search_ingredients(ingredients):
    connection = sqlite3.connect('ingredients.db')
    cursor = connection.cursor()

    results = []
    for ingredient in ingredients:
        cursor.execute('SELECT * FROM ingredients WHERE name LIKE ?', (f"%{ingredient}%",))
        match = cursor.fetchone()
        if match:
            results.append({
                "name": match[1],
                "category": match[2],
                "benefits": match[3],
                "risks": match[4]
            })
        else:
            results.append({"name": ingredient, "error": "Ingredient not found in database"})

    connection.close()
    return results
