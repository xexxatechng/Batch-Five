/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package euclidalgorithm;

/**
 *
 * @author dell
 */
public class Euclid {
int firstNumber;
int secondNumber;
public Euclid(int firstNumber, int secondNumber) {
    this.firstNumber = firstNumber;
    this.secondNumber = secondNumber;
}


public int HCF() {
int gcd;
if (secondNumber > firstNumber) {
int temp = firstNumber;
firstNumber = secondNumber;
secondNumber = temp;
}
int quotient = firstNumber / secondNumber;
int remainder = firstNumber % secondNumber;
while(remainder !=0) {
firstNumber = secondNumber;
secondNumber = remainder;
remainder = firstNumber % secondNumber;
}
gcd = secondNumber;
return gcd; 
}






}
