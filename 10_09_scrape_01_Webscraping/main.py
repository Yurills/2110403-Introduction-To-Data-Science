from bs4 import BeautifulSoup
from bs4.element import Tag



def Q1(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, "lxml")
        
        holy_days = []
        for i in range(7):
            holy_days.append(0)
        thai_day = {'จันทร์': 0, 'อังคาร': 1, 'พุธ': 2, 'พฤหัส': 3, 'ศุกร์': 4, 'เสาร์':5, 'อาทิตย์': 6}
        
        
        div = soup.find_all(attrs={'class': 'bud-day-col'})
        for e in div:
            e = e.string
            for key in thai_day:
                if(e is None): continue
                if key in e:
                    holy_days[thai_day.get(key)] += 1
   
    return holy_days
        
    

def Q2(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, "lxml")
        
        div = soup.find('a',attrs={'title': 'วันวิสาขบูชา'})
        while ('bud-day' not in div.get('class', [])):
            div = div.parent
            
        for e in div:
            if e is None: continue
            if 'วัน' in e.string:
                return e.string
                
    
    
    return 1

exec(input().strip())