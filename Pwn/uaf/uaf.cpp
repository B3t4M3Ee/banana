#include<cstdio>
#include<cstdlib>
#include<cstring>
class A{
public:
virtual void print()
{
	puts("class A");
}
};

class B:public A
{
public:
void print()
{
puts("class B");
}
};

void sh(){
system("sh");
}
char buf[1024];
int main()
{
setvbuf(stdout,0,_IONBF,0);
A *p=new B();
delete p;
fgets(buf,sizeof(buf),stdin);
char *q=strdup(buf);
p->print();
}
