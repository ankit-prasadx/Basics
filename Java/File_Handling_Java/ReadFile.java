import java.io.*;

class ReadFile
{
    public static void main(String g[]) throws Exception
    {
        FileInputStream fobj = new FileInputStream("DemoFile.txt");
        
        int i = 0;

        while((i = fobj.read()) != -1)
        {
            // System.out.println((char)i);
            System.out.print((char)i);
        }
        System.out.println();
        fobj.close();
    }
}