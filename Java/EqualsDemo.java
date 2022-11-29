
class Demo
{
    public int No1;
    public int No2;

    public Demo(int a, int b)
    {
        No1 = a;
        No2 = b;
    }
}

class EqualsDemo
{
    public static void main (String Q[])
    {
        // Demo obj1 = new Demo(10,11);
        // Demo obj2 = new Demo(10,11);

        // if (obj1.equals(obj2))
        // {
        //     System.out.println("Objects are same");
        // }
        // else
        // {
        //     System.out.println("Objects are diiferent");
        // }


        String s1 = "Hello";
        String s2 = "Hello";
        
        System.out.println("Hashcode of s1 : "+s1.hashCode());  // hashCode = 1001
        System.out.println("Hashcode of s2 : "+s2.hashCode());  // hashCode = 1001

        if (s1.equals(s2))  // if("Hello" == "Hello")
        {
            System.out.println("Objects are same");
        }
        else
        {
            System.out.println("Objects are diiferent");
        }

        if (s1 == s2)   // if(1001 == 1001)
        {
            System.out.println("Objects are same");
        }
        else
        {
            System.out.println("Objects are diiferent");
        }
    }
}