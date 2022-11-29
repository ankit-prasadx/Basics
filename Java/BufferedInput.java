import java.io.*;

class BufferedInput
{
    public static void main(String R[])
    {
        InputStreamReader iobj = new InputStreamReader(System.in);
        BufferedReader bobj = new BufferedReader(iobj);

        String name = null;
        int Age = 0;
        float Marks = 0.0f;

        try
        {
            System.out.println("Enter your name : ");
            name = bobj.readLine();

            System.out.println("Enter your age : ");
            Age = Integer.parseInt(bobj.readLine());

            System.out.println("Enter your marks : ");
            Marks = Float.parseFloat(bobj.readLine());
        }
        catch(IOException obj)
        {}
        
        System.out.println("Name : "+name);
        System.out.println("Age : "+Age);
        System.out.println("Marks : "+Marks);

    }
}