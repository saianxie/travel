list = [

    "最近三个月",
    "十月",
    "十一月",
    "十二月",
    "一月",
    "二月",
    "三月",
    "四月",
    "五月",
    "六月",
    "七月",
    "国庆",
    "春节",
    "端午",
    "新年"

]
# insert into joke (gid,name)values(0,"joker"),(1,"jhj");
for i in range(2):
    print('insert into tripline_country (name,chau_id)values' + '(' + '"' + list[i] + '"' + ',' + '7' + ')' + ';')
