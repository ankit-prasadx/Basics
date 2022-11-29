import java.sql.*;

class Database1
{
    public static void main(String Q[]) throws Exception
    {
        String URL = "jdbc:mysql://localhost:3306/ppa41";
        String Username = "root";
        String Password = "root";
        String Query = "select * from student";
        Connection cobj = DriverManager.getConnection(URL,Username,Password);

        Statement sobj = cobj.createStatement();

        ResultSet robj = sobj.executeQuery(Query);

        System.out.println("RID\tName\tCity\tMarks\t");

        while(robj.next())
        {
            System.out.print(robj.getInt("RID")+"\t");
            System.out.print(robj.getString("Name")+"\t");
            System.out.print(robj.getString("City")+"\t");
            System.out.println(robj.getInt("Marks")+"\t");
        }

    }
}