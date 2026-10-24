import os
import re
from google import genai
from datetime import datetime

# 💡 ضع مفتاح Gemini الفعلي الخاص بك هنا
GEMINI_KEY = 'AQ.Ab8RN6K2dItsEtRCZldolMlf3TzL6r0DQDInaT06Ks16i_TTmA'
client = genai.Client(api_key=GEMINI_KEY)

def generate_article():
    try:
        # استخدام التوجيه بالإنجليزية مع طلب الكتابة بالعربية لتفادي مشاكل الترميز
        prompt = "Write a new, unique, and professional technology article entirely in Arabic about a random trending tech topic in 2026. Include a catchy Arabic title and structured subtitles."
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"❌ Error during Gemini generation: {e}")
        raise e

def create_slug(title):
    # تحويل العنوان إلى اسم ملف إنجليزي أو رقمي بسيط لمنع مشاكل الروابط العربية
    clean_title = re.sub(r'[^\w\s]', '', title)
    return datetime.now().strftime('%Y%m%d_%H%M%S')

if __name__ == "__main__":
    print("⏳ Generating article...")
    raw_content = generate_article()
    
    # محاولة استخراج أول سطر كعنوان للمقال
    lines = [l.strip() for l in raw_content.split('\n') if l.strip()]
    article_title = lines[0].replace('#', '').strip() if lines else "مقال تقني جديد"
    
    html_body = raw_content.replace("\n", "<br>")
    file_slug = create_slug(article_title)
    post_filename = f"post_{file_slug}.html"
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # 📢 روابط الأفلييت الخاصة بك
    affiliate_link = "https://amazon.com"
    
    # 1️⃣ بناء صفحة المقال المنفصلة
    post_page = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{article_title}</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; background: #f8f9fa; color: #333; }}
            .nav {{ background: #2c3e50; padding: 15px; text-align: center; }}
            .nav a {{ color: white; text-decoration: none; font-weight: bold; font-size: 1.1em; }}
            .container {{ max-width: 800px; margin: 30px auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            .date {{ color: #7f8c8d; font-size: 0.9em; }}
            .content {{ font-size: 1.1em; line-height: 1.9; color: #444; margin-top: 20px; }}
            .ad-space {{ background: #fdf6e2; border: 2px dashed #f39c12; color: #d35400; text-align: center; padding: 20px; margin: 30px 0; border-radius: 6px; font-weight: bold; }}
            .btn-buy {{ display: inline-block; background: #e74c3c; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px; font-weight: bold; display: block; text-align: center; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="nav"><a href="index.html">⬅️ العودة للرئيسية</a></div>
        <div class="container">
            <div class="ad-space">📢 مساحة إعلانية متوفرة للربح</div>
            <h1>{article_title}</h1>
            <p class="date">📅 تاريخ النشر: {current_date}</p>
            <div class="content">{html_body}</div>
            <div class="ad-space">📢 مساحة إعلانية مدمجة داخل المقال</div>
            <a href="{affiliate_link}" target="_blank" class="btn-buy">🛒 تسوق أفضل العروض التقنية عبر أمازون</a>
        </div>
    </body>
    </html>
    """
    
    # حفظ ملف المقال الجديد
    with open(post_filename, "w", encoding="utf-8") as f:
        f.write(post_page)
    print(f"🎉 Created article file: {post_filename}")
    
    # 2️⃣ تحديث صفحة الأرشيف الرئيسية (index.html) تلقائياً
    # قراءة المقالات القديمة المسجلة في ملف نصي أو إضافتها للأرشيف
    archive_log = "archive.txt"
    with open(archive_log, "a", encoding="utf-8") as f:
        f.write(f"{current_date}|||{article_title}|||{post_filename}\n")
        
    with open(archive_log, "r", encoding="utf-8") as f:
        archive_lines = f.readlines()
        
    articles_list_html = ""
    for line in reversed(archive_lines): # ترتيب من الأحدث للأقدم
        if "|||" in line:
            p_date, p_title, p_file = line.strip().split("|||")
            articles_list_html += f"""
            <div class="post-card">
                <h3><a href="{p_file}">{p_title}</a></h3>
                <p style="color:gray; font-size:0.9em;">📅 {p_date}</p>
            </div>
            """
            
    index_page = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>أرشيف مدونتي الذكية</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; background: #f4f7f6; color: #333; }}
            .header {{ background: #2c3e50; color: white; padding: 40px; text-align: center; }}
            .container {{ max-width: 900px; margin: 30px auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }}
            .post-card {{ border-bottom: 1px solid #eee; padding: 15px 0; }}
            .post-card h3 a {{ color: #2980b9; text-decoration: none; }}
            .post-card h3 a:hover {{ text-decoration: underline; }}
            .ad-space {{ background: #fdf6e2; border: 2px dashed #f39c12; color: #d35400; text-align: center; padding: 20px; margin: 20px 0; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2>🚀 مجلة الذكاء الاصطناعي والأرباح التلقائية</h2>
            <p>مقالات تقنية متجددة يومياً بواسطة AI</p>
        </div>
        <div class="container">
            <div class="ad-space">📢 مساحة إعلانية رئيسية للموقع</div>
            <h2>📚 المقالات المنشورة مؤخراً:</h2>
            {articles_list_html}
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_page)
    print("🎉 Index archive page updated successfully!")
