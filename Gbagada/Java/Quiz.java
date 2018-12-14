/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package quiz;

/**
 *
 * @author HP
 */
public class Quiz {

    /**
     * @param args the command line arguments
     */        // TODO code application logic here
        public static void main(String[] args) {
    String[] answerkey = {"2","4","1","1","3","1","1","4","2","2","2","4","3","1","3","3","1","4","1","1"};
    int n = 0;

        int correct = 0;
        int incorrect = 0;
        String answer = "";

        for (int i = 0; i < 20; i++){
            System.out.println("Please enter your answers. Acceptable input is limited to 1,2,3 and 4.\n");
            if (answer.compareTo(answerkey[0])==0){
                correct++;} 
            else {incorrect++;}
        }

        if (correct > 14){
            System.out.println("You passed.");
        } else {
           System.out.println("You failed.");
        }
        System.out.println("You have " + correct + " correct answers.");
        System.out.println("You have " + incorrect + " incorrect answers.");

}
    }
    

