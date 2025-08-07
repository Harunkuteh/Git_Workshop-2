# quiz.py

score = 0

questions = [
    {
        "question": "1. เมืองหลวงของประเทศไทยคือข้อใด?",
        "choices": ["1) เชียงใหม่", "2) กรุงเทพ", "3) ภูเก็ต"],
        "answer": 2
    },
    {
        "question": "2. ภาษาใดที่ใช้เขียนโปรแกรมนี้?",
        "choices": ["1) Python", "2) Java", "3) HTML"],
        "answer": 1
    },
    {
        "question": "3. 5 + 3 เท่ากับเท่าไร?",
        "choices": ["1) 6", "2) 8", "3) 10"],
        "answer": 2
    },
    {
        "question": "4. สีของท้องฟ้าในตอนกลางวันคือ?",
        "choices": ["1) เขียว", "2) น้ำเงิน", "3) แดง"],
        "answer": 2
    },
    {
        "question": "5. ผลไม้ชนิดใดมีเปลือกหนาม?",
        "choices": ["1) แตงโม", "2) มะม่วง", "3) ทุเรียน"],
        "answer": 3
    }
]

# เริ่มคำถาม
for q in questions:
    print("\n" + q["question"])
    for choice in q["choices"]:
        print(choice)
    try:
        user_answer = int(input("เลือกคำตอบ (1, 2, หรือ 3): "))
        if user_answer == q["answer"]:
            print("✅ ถูกต้อง!")
            score += 1
        else:
            print("❌ ผิด คำตอบที่ถูกคือข้อ", q["answer"])
    except ValueError:
        print("⚠️ กรุณากรอกแค่ตัวเลข 1, 2, หรือ 3 เท่านั้น")

# สรุปคะแนน
print(f"\nคุณได้คะแนน {score} จาก {len(questions)} คะแนน")
