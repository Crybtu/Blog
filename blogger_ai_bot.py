import os
from google import genai
from datetime import datetime

# 💡 ضع مفتاح Gemini الخاص بك هنا بدلاً من كلمة your_api_key_here
GEMINI_KEY = 'AQ.Ab8RN6K2dItsEtRCZldolMlf3TzL6r0DQDInaT06Ks16i_TTmA'
client = genai.Client(api_key=GEMINI_KEY)

def generate_article():
    try:
        english_prompt = "Write a comprehensive, professional, and detailed technology article entirely in Arabic about: 'The Future of Artificial Intelligence in 2026'. Include subtitles and standard web blog formatting."
        
        response = client.models.generate_content(
model='gemini-2.5-flash',

            contents=english_prompt
        )
        return response.text
    except Exception as e:
        print(f"❌ Error during Gemini content generation: {e}")
        raise e

if __name__ == "__main__":
    print("⏳ Generating article from Gemini...")
    content = generate_article()
    
    html_content = content.replace("\n", "<br>")
    
    affiliate_link_1 = "https://amazon.com"
    affiliate_link_2 = "https://hostinger.com"
    
    web_page = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; background: #f8f9fa; color: #333; }}
            .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; }}
            .container {{ max-width: 900px; margin: 20px auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }}
            h1 {{ color: #2c3e50; }}
            .date {{ color: #7f8c8d; font-size: 0.9em; }}
            .content {{ font-size: 1.1em; line-height: 1.9; color: #444; }}
            .ad-space {{ background: #fdf6e2; border: 2px dashed #f39c12; color: #d35400; text-align: center; padding: 20px; margin: 20px 0; border-radius: 6px; font-weight: bold; }}
            .affiliate-box {{ background: #e8f4fd; border-left: 5px solid #3498db; padding: 20px; margin-top: 30px; border-radius: 4px; }}
            .btn-buy {{ display: inline-block; background: #e74c3c; color: white; padding: 10px 20px; text-align: center; text-decoration: none; border-radius: 4px; font-weight: bold; margin-top: 10px; }}
            .btn-buy:hover {{ background: #c0392b; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2>مدونة التقنية والذكاء الاصطناعي الذكية 🚀</h2>
        </div>
        
        <div class="container">
            <div class="ad-space">
                📢 مساحة إعلانية متوفرة (تظهر هنا إعلانات الشركات البديلة للربح)
            </div>

            <h1>مستقبل الذكاء الاصطناعي في عام 2026</h1>
            <p class="date">📅 تاريخ النشر: {datetime.now().strftime('%Y-%m-%d')}</p>
            <hr>
            
            <div class="content">
                {html_content}
            </div>

            <div class="ad-space">
                📢 مساحة إعلانية مدمجة داخل المقال (لتحقيق أعلى نسبة نقرات وأرباح)
            </div>

            <div class="affiliate-box">
                <h3>💡 توصيات كاتب المقال (روابط مدفوعة):</h3>
                <p>إذا كنت تبحث عن الأدوات والعتاد التقني الأفضل لتطبيق ما جاء في هذا المقال، ننصحك بالاطلاع على المنتجات التالية الموصى بها بشدة:</p>
                <a href="{affiliate_link_1}" target="_blank" class="btn-buy">🛒 تسوق أفضل أجهزة المساعدة الذكية من أمازون</a>
                <a href="{affiliate_link_2}" target="_blank" class="btn-buy" style="background:#2ecc71;">🌐 احصل على استضافة موقعك الخاص وابدأ مشروعك الآن</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(web_page)
        
    print("🎉 Success! Article page has been created and saved successfully.")
