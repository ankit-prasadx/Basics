import java.lang.*;

class Employee implements Cloneable
{
    public int EmpID;
    public String Name;
    public int Salary;

    public Employee(int No, String str, int Value)
    {
        this.EmpID = No;
        this.Name = str;
        this.Salary = Value;
    }
    public Object clone() throws CloneNotSupportedException
    {
        return super.clone();
    }
}

class CloneDemo 
{
    public static void main (String q[]) 
    {
        try
        {
            Employee eobj1 = new Employee(101,"Rahul",11000);
            Employee eobj2 = (Employee)eobj1.clone();

            System.out.println("Name of first employee : "+eobj1.Name);
            System.out.println("Name of second employee : "+eobj2.Name);

            System.out.println("Salary of first employee : "+eobj1.Salary);
            System.out.println("Salary of second employee : "+eobj2.Salary);

            eobj1.Name = "Sagar";
            eobj1.Salary++;

            System.out.println("Name of first employee : "+eobj1.Name);
            System.out.println("Name of second employee : "+eobj2.Name);
            
            System.out.println("Salary of first employee : "+eobj1.Salary);
            System.out.println("Salary of second employee : "+eobj2.Salary);
        }
        catch(CloneNotSupportedException obj)
        {}
    }
}
