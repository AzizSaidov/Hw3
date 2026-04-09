
# **ТЗ: E-commerce API (Магазин)**

## **Модели**

### **User**

* id
* username
* email

### **Category**

* id
* name

### **Product**

* id
* title
* description
* price
* category (FK → Category)
* owner (FK → User)
* created_at

### **Review**

* id
* text
* rating (1–5)
* product (FK → Product)
* user (FK → User)

---

## **Требования**

### **1. FBV**

Реализовать:

* список товаров
* создание товара
* детали товара
* обновление / удаление

---

### **2. Nested Serializer**

При GET продукта:

* показывать **все отзывы**

```json
{
  "id": 1,
  "title": "iPhone",
  "reviews": [
    {
      "id": 1,
      "rating": 5,
      "text": "Good"
    }
  ]
}

---


//////////////////////////////////  
//////////////////////////////////  ### 3. to_representation
//////////////////////////////////  
//////////////////////////////////  Добавить:
//////////////////////////////////  
//////////////////////////////////  * средний рейтинг товара
//////////////////////////////////  
//////////////////////////////////  "avg_rating": 4.5

---

### 4. get_<field>

Добавить:

review_count = SerializerMethodField()

"review_count": 10

---

### 5. Pagination

* список продуктов с пагинацией

---

### 6. Filter

Фильтр:

* по категории
* по цене (min_price, max_price)

/products/?category=1
/products/?min_price=100&max_price=500

---

### 7. Search

Поиск:

* по названию товара

/products/?search=iphone

---

### 8. Validation

* price > 0
* rating от 1 до 5
* title не пустой

---

### 9. Write-only / Read-only

* owner → write_only

* owner_data → read_only (username)

* category → write_only (id)

* category_data → read_only (name)

---

////////////////////////////////////////### 10. Поведение
////////////////////////////////////////
////////////////////////////////////////* пользователь может оставить только 1 отзыв на товар
////////////////////////////////////////* нельзя удалить чужой продукт
////////////////////////////////////////
---

## Ожидаемый ответ

{
  "id": 1,
  "title": "iPhone",
  "price": 999,
  "category_data": {
    "name": "Phones"
  },
  "owner_data": {
    "username": "hakim"
  },
  "avg_rating": 4.5,
  "review_count": 2,
  "reviews": [
    {"id": 1, "rating": 5, "text": "Good"},
    {"id": 2, "rating": 4, "text": "Nice"}
  ]
}

```