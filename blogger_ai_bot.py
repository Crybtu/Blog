import os
import json
import google.generativeai as genai
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 1. إعداد ذكاء جوجل الاصطناعي (Gemini)
# ضع مفتاح Gemini الخاص بك هنا بدلاً من المكتوب
GEMINI_KEY = 'AQ.Ab8RN6K2dItsEtRCZldolMlf3TzL6r0DQDInaT06Ks16i_TTmA'
genai.configure(api_key=GEMINI_KEY)

def generate_article():
    # استخدام النموذج المستقر الأحدث
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "اكتب مقالاً تقنياً احترافياً ومفصلاً باللغة العربية عن 'مستقبل الذكاء الاصطناعي في عام 2026' مع العناوين الفرعية."
    response = model.generate_content(prompt)
    return response.text

# 2. إعداد الاتصال ببلوقر والنشر
def publish_to_blogger(content):
    # ضع معرف مدونتك المكون من أرقام هنا بين العلامتين ''
    blog_id = '6819029518868981101'
    
    # قراءة اعتمادات جوجل من ملف خارجي مستقل لتجنب أخطاء التنسيق
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
    print(f"تم بنجاح إنشاء المقال كمسودة! الرابط: {response['url']}")

if __name__ == "__main__":
    print("جاري توليد المحتوى من Gemini...")
    article_text = generate_article()
    print("جاري نشر المقال على بلوقر...")
    publish_to_blogger(article_text)
