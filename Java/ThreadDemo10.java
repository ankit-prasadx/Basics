class ThreadDemo10
{
    public static void main(String q[])
    {
        System.out.println("Inside main method");
        System.out.println("Name of main thread is : "+Thread.currentThread().getName());
        System.out.println("Priority of main thread is : "+Thread.currentThread().getPriority());
    }
}
