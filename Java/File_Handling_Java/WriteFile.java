import java.io.*;

class WriteFile
{
    public static void main(String g[]) throws Exception
    {
        FileOutputStream fobj = new FileOutputStream("DemoFile.txt");

        String Data = "Marvellous Infosystems Pune";

        byte bdata[] = Data.getBytes();

        fobj.write(bdata);
        fobj.close();
    }
}