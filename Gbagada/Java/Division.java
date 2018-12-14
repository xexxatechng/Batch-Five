/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package division;
import java.util.Scanner;

/**
 *
 * @author user
 */
public class Division {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // TODO code application logic here
        int a, b, c;
        System.out.println("Enter two numbers for division");
        
        a = input.nextInt();
        b = input.nextInt();
        c = a/b;
        System.out.println("Division of the integers = " +c);
       
        double d, e;
        System.out.println("Multiply the answer of c and d");
        c = input.nextInt();
        d = input.nextDouble();
        e = d*c;
        System.out.println("multiply the answer e = " +e);
    }
    
}
