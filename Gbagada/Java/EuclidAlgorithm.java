/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package euclidalgorithm;
import java.util.Scanner;


/**
 *
 * @author dell
 */
public class EuclidAlgorithm {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner (System.in);
    
     
        System.out.print("Enter the first number: ");
        int firstNumber = input.nextInt();
        System.out.print("Enter second number: ");
        int secondNumber = input.nextInt();
        Euclid euclid = new Euclid(firstNumber, secondNumber);
        System.out.println(euclid.HCF());}
}
