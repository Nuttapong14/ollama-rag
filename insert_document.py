import psycopg2
import json
from sentence_transformers import SentenceTransformer

conn = psycopg2.connect(
    dbname="vector-db",
    user="admin",
    password="1234",
    host="localhost",
    port="5433"
)

cur = conn.cursor()
model = SentenceTransformer("BAAI/bge-m3")

def add_document(text):
    embedding = model.encode(text).tolist()
    cur.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (text, json.dumps(embedding)))
    conn.commit()

document = [
    "ประเทศไทยมีอากาศร้อนชื้นตลอดทั้งปี",
    "วันนี้ฉันไปเดินเล่นที่สวนจตุจักรและซื้อของฝาก",
    "เทคโนโลยีปัญญาประดิษฐ์กำลังเปลี่ยนแปลงโลกอย่างรวดเร็ว",
    "อาหารไทยที่ฉันชอบมากที่สุดคือต้มยำกุ้ง",
    "การเรียนรู้ตลอดชีวิตเป็นกุญแจสำคัญสู่ความสำเร็จ",
    "การออกกำลังกายอย่างสม่ำเสมอช่วยให้สุขภาพดีขึ้น",
    "หนังเรื่องโปรดของฉันคือ 'พี่มาก...พระโขนง'",
    "ประเทศไทยมีวัฒนธรรมที่หลากหลายและสวยงาม",
    "เครื่องบินลำนี้จะออกเดินทางเวลา 9 โมงเช้า",
    "ภาษาไทยมีความซับซ้อนและไพเราะในเวลาเดียวกัน"
]

for doc in document:
    add_document(doc)

cur = conn.cursor()
conn.close()
