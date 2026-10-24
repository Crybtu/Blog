import os
import json
import google.generativeai as genai
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 1. إعداد ذكاء جوجل الاصطناعي (Gemini)
# ضع مفتاح Gemini الخاص بك هنا بدلاً من المكتوب
GEMINI_KEY = 'AQ.Ab8RN6K2dItsEtRCZldolMlf3TzL6r0DQDInaT06Ks16i_TTmA'

# الطريقة الصحيحة والمباشرة لتهيئة مكتبة Gemini الحديثة
genai.configure(api_key=GEMINI_KEY)

def generate_article():
    try:
        # استخدام النموذج الأكثر استقراراً ومرونة المتوافق عالمياً
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = "اكتب مقالاً تقنياً احترافياً ومفصلاً باللغة العربية عن 'مستقبل الذكاء الاصطناعي في عام 2026' مع العناوين الفرعية."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ خطأ أثناء توليد المقال من Gemini: {e}")
        raise e

# 2. إعداد الاتصال ببلوقر والنشر
def publish_to_blogger(content):
    # ضع معرف مدونتك المكون من أرقام هنا بين العلامتين ''
    blog_id = '6819029518868981101'
    
    if not os.path.exists('google_creds.json'):
        raise FileNotFoundError("❌ خطأ: ملف 'google_creds.json' غير موجود في المستودع!")
        
    try:
        scopes = ['https://googleapis.com']
        with open('google_creds.json', 'r') as f:
            creds_json = json.load(f)
            
        creds = service_account.Credentials.from_service_account_info(creds_json, scopes=scopes)
        service = build('blogger', 'v3', credentials=creds)
        
        html_content = content.replace("\n", "<br>")
        
        post_body = {
            "kind": "blogger#post",
            "title": "مستقبل الذكاء الاصطناعي في عام 2026",
            "content": html_content
        }
        
        request = service.posts().insert(blogId=blog_id, body=post_body, isDraft=True)
        response = request.execute()
        print(f"🎉 تم بنجاح إنشاء المقال كمسودة! الرابط: {response['url']}")
    except Exception as e:
        print(f"❌ خطأ أثناء الاتصال أو النشر على Blogger: {e}")
        raise e

if __name__ == "__main__":
    print("⏳ جاري توليد المحتوى من Gemini...")
    article_text = generate_article()
    print("⏳ جاري نشر المقال على بلوقر...")
    publish_to_blogger(article_text)
