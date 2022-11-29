// String

// StringBuffer

// StringBuilder

 class StringDemo2
{
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = new String("Demo");
        String s3 = "Hello";
        String s4 = new String("Demo");
        String s5 = new String("Ganesh");
        String s6 = "Marvellous";

        System.out.println("Hashcode of s1 : "+s1.hashCode());
        System.out.println("Hashcode of s2 : "+s2.hashCode());
        System.out.println("Hashcode of s3 : "+s3.hashCode());
        System.out.println("Hashcode of s4 : "+s4.hashCode());
        System.out.println("Hashcode of s5 : "+s5.hashCode());
        System.out.println("Hashcode of s6 : "+s6.hashCode());
    }
}