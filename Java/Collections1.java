import java.util.*;

class Collections1
{
    public static void main(String args[])
    {
        LinkedList <Integer>lobj = new LinkedList<Integer>();

        lobj.add(11);
        lobj.add(21);
        lobj.add(51);
        lobj.add(101);
        lobj.add(111);

        System.out.println("Elements of linked list are : "+lobj);

        lobj.addFirst(1);
    
        System.out.println("Elements of linked list are : "+lobj);

        lobj.addLast(121);
    
        System.out.println("Elements of linked list are : "+lobj);

        Iterator iobj = lobj.iterator();
        System.out.println("Data Using Iterator is : ");
        while(iobj.hasNext())
        {
            System.out.println(iobj.next());
        }
        
        if(lobj.contains(121))
        {
            System.out.println("121 is present in linked list");
        }
        else
        {
            System.out.println("121 is not present in linked list");
        }
        
        lobj.remove();

        System.out.println("Elements of linked list are : "+lobj);
        
        lobj.remove(1);

        System.out.println("Elements of linked list are : "+lobj);
        
        lobj.remove(0);

        System.out.println("Elements of linked list are : "+lobj);
        
        lobj.removeLast();
        
        System.out.println("Elements of linked list are : "+lobj);

        System.out.println("Number of Elements are : "+lobj.size());

        lobj.set(1,500);
        System.out.println("Elements of linked list are : "+lobj);

        lobj.clear();
        System.out.println("Elements of linked list are : "+lobj);
    }
}
