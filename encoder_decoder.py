#encoder and decoder
"""
a->z
b->y
c->x
d->w
e->v
f->u
g->t
h->s
i->r
j->q
k->p
l->o
m->n
n->m
o->l
p->k
q->j
r->i
s->h
t->g
u->f
v->e
w->d
x->c
y->b
z->a
"""
try:
	def encoder_decoder():
			dir={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s',
			'i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j',
			'r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':' '
			,'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q',
			'K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F',
			'V':'E','W':'D','X':'C','Y':'B','Z':'A',1:0,2:9,3:8,4:7,5:6,6:5,7:4,8:3,9:2,0:1}
			value=input("enter your message to encode or decode :")

			value2=[]
			for i in value:
				value2.append(i)
			print("Answer :",end="")
			for i in value2:
				printer=dir['{}'.format(i)]
				print(printer,end="")
		
	while True:
		print("\nNote : Your message should be under a-z (lowercase alphabets) ,A-Z (uppercase alphabets) and Numbers \n CTRL+C to close program")
		encoder_decoder()
	input()
	
	
except Exception as e:
	print("Invalid")
	a=input("enter y to rerun program")
	if a is 'y' or 'Y':
		encoder_decoder()
	else:
		print("bye")

finally:
	print("Program closed")
