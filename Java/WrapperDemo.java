class WrapperDemo
{
    public static void main(String q[])
    {
        int no = 11;
        Integer iobj = new Integer(no);     // Boxing - Converting

        System.out.println(no);
        System.out.println(iobj);

        int x = iobj;
        System.out.println(x);
    }
}