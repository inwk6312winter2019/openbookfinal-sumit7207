import operator
book1=open('Book1.txt')
book2=open('Book2.txt')
book3=open('Book3.txt')

# Part - 1
def unique_name(b1,b2,b3):
	d=dict()
	for i in b1:
		for j in i.split():
			d[j]=d.get(j,0)+1
	for i in b2:
		for j in i.split():
			d[j]=d.get(j,0)+1
	for i in b3:
		for j in i.split():
			d[j]=d.get(j,0)+1
	my_list=d.items()
	print(my_list)

unique_name(book1,book2,book3)

# Part - 2

book1=open('Book1.txt')
book2=open('Book2.txt')
book3=open('Book3.txt')
def count_the_article(a1,a2,a3):
	article_list=["a", "the", "at", "run", "to","and","are","or","for","an","this"]
	a=dict()
	for i in a1:
		for j in i.split():
			if j in article_list:
				a[j]=a.get(j,0)+1
	for i in a2:
                for j in i.split():
                        if j in article_list:
                                a[j]=a.get(j,0)+1
	for i in a3:
                for j in i.split():
                        if j in article_list:
                                a[j]=a.get(j,0)+1

	print (a)

count_the_article(book1,book2,book3)

# Part - 3


book1=open('Book1.txt')
book2=open('Book2.txt')
book3=open('Book3.txt')

def sorted_words(c1,c2,c3):
	d=dict()
	my_list=[]
	for i in c1:
		for j in i.split():
			d[j]=d.get(j,0)+1
	for i in c2:
		for j in i.split():
			d[j]=d.get(j,0)+1
	for i in c3:
		for j in i.split():
			d[j]=d.get(j,0)+1
	for k in d:
		l=len(k)
		d[k]=l
	my_list=d.keys()
	new=sorted(my_list, key=len,reverse=True)
	print(new)

sorted_words(book1,book2,book3)


# Part - 4

book1=open('Book1.txt')
book2=open('Book2.txt')
book3=open('Book3.txt')
def character_word_count(c1,c2,c3):
        d=dict()
        new=[]
        for i in c1:
                for j in i.split():
                        d[j]=d.get(j,0)+1
        for i in c2:
                for j in i.split():
                        d[j]=d.get(j,0)+1
        for i in c3:
                for j in i.split():
                        d[j]=d.get(j,0)+1
        for k in d:
                l=len(k)
                d[k]=l
        sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
        dic=dict(sorted_d)
        print(dic)

character_word_count(book1,book2,book3)

# Part - 5


book1=open('Book1.txt')
book2=open('Book2.txt')
book3=open('Book3.txt')

def starts_with_vow(d1,d2,d3):
        tup=("a", "e", "i", "o", "u")
        my_list=[]
        total=0
        for i in d1:
                for j in i.split():
                        x=tuple(j)
                        w=x[0]
                        if w in tup:
                                total+=1
        for i in d2:
                for j in i.split():
                        x=tuple(j)
                        w=x[0]
                        if w in tup:
                                total+=1

        for i in d3:
                for j in i.split():
                        x=tuple(j)
                        w=x[0]
                        if w in tup:
                                total+=1

        print(total)

starts_with_vow(book1,book2,book3)
