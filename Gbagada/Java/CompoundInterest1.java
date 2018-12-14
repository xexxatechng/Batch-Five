/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package compoundinterest1;

/**
 *
 * @author User
 */
public class CompoundInterest1 {

    /**
     * 
     */
    public static void main(String[] args) {
       double amount;
       double principal = 10000;
       double rate = .02;
       
       for(int year=1; year<=20;year++){
           amount=principal*Math.pow(1 + rate, year);
           System.out.println(year+ " "+ amount);
           
           
       }
    }
    
}
