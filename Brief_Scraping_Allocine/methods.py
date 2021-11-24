import re

def minutify(str):
        h = 0
        m = 0
        if str.find('h') != -1:
                h = int(re.findall(r'(\d+)h.*', str)[0])
        if str.find('m') != -1 and h:
                m = int(re.findall(r'\d+h (\d+)m', str)[0])
        elif str.find('m') != -1:
                m = int(re.findall(r'(\d+)m', str)[0])
        return (h*60)+m