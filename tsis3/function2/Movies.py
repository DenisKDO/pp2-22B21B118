movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
print("All movies:")
for i in movies:
    if i==movies[len(movies)-1]:
        print(i["name"])
        break
    print(i["name"],end=", ")
#task1
nam=input("Enter name of the film: ")
def above5_5(nam):
    for i in movies:
        if i["name"]==nam:
            if i["imdb"]>5.5:
                return True
            else:
                return False
print(above5_5(nam))
#task2
goodmov=[]
def gmlist(goodmov):
    print("")
    for i in movies:
        if i["imdb"]>5.5:
            goodmov.append(i)
    for i in goodmov:
        print(i['name'],i['imdb'],i['category'],sep='-')
gmlist(goodmov)
#task3
print()
categ=input("Choose the category: ")
def cat(categ):
    for i in movies:
        if i['category']==categ:
            print(i['name'])
cat(categ)
#task4
print('\nEnter few movies and we calculate average IMDB of them (if ended ender "ok"): ')
lofmovies=[]
for i in range(1000):
    a=input()
    if a=='OK' or a=='Ok' or a=='ok':
        break
    lofmovies.append(a)
def avimdb(lofmovies):
    cnt=0
    for i in lofmovies:
        for j in movies:
            if i==j['name']:
                cnt=cnt+j['imdb']
    print(round(cnt/len(lofmovies),2))
avimdb(lofmovies)
#task 5
categ=input("Choose the category and we calculate average IMDB of it: ")
def avcat(categ):
    count=0
    cnt=0
    for i in movies:
        if i['category']==categ:
            count+=i['imdb']
            cnt+=1
    print(round(count/cnt,2))
avcat(categ)
        






