
import re
def check_imgs(path):
    print('=== ' + path + ' ===')
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()
    imgs = re.findall(r'<img[^>]+>', t)
    for img in imgs[:5]:
        print('  ', img)
check_imgs(r'c:\Users\pc\Desktop\menu\menu_model1_emirates.html')
check_imgs(r'c:\Users\pc\Desktop\menu\menu_model2_urban.html')
check_imgs(r'c:\Users\pc\Desktop\menu\menu_model3_vibrant.html')
