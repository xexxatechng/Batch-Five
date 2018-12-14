/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package simpleinterest.calculator;
// Import the scanner class
import java.util.Scanner;

/**
 *
 * @author Bishopsam
 */
public class SimpleInterestCalculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
    
    float p, r, t;
     Scanner s = new Scanner(System.in);
     
    System.out.println("Enter the Principal: ");
    p = s.nextFloat();
    
    System.out.println("Enter the Rate of interest: ");
    r = s.nextFloat();
    
    System.out.println("Enter the Time period: ");
    t = s.nextFloat();
    
    float si;
    si = (r * t * p) / 100;
    System.out.println("The Simple Interest:" + si);
    
    }
    
}
