import java.io.*;

class CreateFile
{
    public static void main(String g[]) throws Exception
    {
        File fobj = new File("DemoFile.txt");

        if(fobj.createNewFile())
        {
            System.out.println("File Created Succesfully");
        }
        else
        {
            System.out.println("Unable to create the File");
        }
    }
}