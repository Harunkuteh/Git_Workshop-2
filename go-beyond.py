# question.py

print("คำถาม: เมืองหลวงของประเทศไทยคือเมืองอะไร?")
answer = input("พิมพ์คำตอบของคุณ: ")

if answer.strip().lower() == "กรุงเทพ" or answer.strip().lower() == "bangkok":
    print("✅ ถูกต้อง! เมืองหลวงของไทยคือกรุงเทพฯ")
else:
    print("❌ ผิดจ้า! คำตอบที่ถูกคือ 'กรุงเทพฯ' หรือ 'Bangkok'")

print("ขอบคุณที่ร่วมตอบคำถาม 😊")
