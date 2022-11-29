import java.util.Iterator;
import java.util.LinkedList;
import java.util.function.LongBinaryOperator;

class Book
{
    public String Name;
    public int Price;

    Book(String s, int i)
    {
        this.Name = s;
        this.Price = i;
    }

    public void Display()
    {
        System.out.println("Book Name : "+this.Name+" Price : "+this.Price);
    }
}

class Collections3
{
    public static void main(String RR[])
    {
        LinkedList <Book>lobj = new LinkedList<Book>();

        lobj.add(new Book("Let Us C",400));
        lobj.add(new Book("Data Structures",580));
        lobj.add(new Book("C++ Programming",980));
        lobj.add(new Book("Angular Web Development",790));

        Iterator iobj = lobj.iterator();
        Book bref = null;

        while(iobj.hasNext())
        {
            bref = (Book)iobj.next();
            bref.Display();
        }
    
        lobj.clear();
    }
}
