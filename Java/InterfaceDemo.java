
interface Circle
{
    float PI = 3.14f;       // public ststic final float PI = 3.14f;

    float Area(float Radius);       // public abstract float Area(float Radius);
    float Circumference(float Radius);      // public abstract float Circumference(float Radius);
}

class Marvellous implements Circle
{
    public float Area (float Radius)
    {
        return PI * Radius * Radius;
    }
    public float Circumference (float Radius)
    {
        return 2 * PI * Radius;
    }
}


class InterfaceDemo
{
    public static void main(String s[])
    {
        System.out.println("Value of PI is : "+Circle.PI);      // Allowed due to characteristics are static and public
        // Circle.PI = 7.12f;      // NA due to Characteristics are final
        Circle obj = new Marvellous();
        float fRet = 0.0f;
        fRet = obj.Area(10.5f);
        System.out.println("Area is : "+fRet);
        fRet = obj.Circumference(10.5f);
        System.out.println("Circumference is : "+fRet);
    }
}