/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package car;

/**
 *
 * @author ammarasmro
 */
public class Car {
    
    int maxSpeed = 100;
    int minSpeed = 0;
    double weight = 4079;
    boolean isTheCarOn = false;
    char condition = 'A';
    String nameOfCar = "Lucy";
    
    double maxFuel = 16;
    double currentFuel = 8;
    double mpg = 26.4;
    
    int numberOfPeopleInCar = 1;
    
    public Car(int customMaxSpeed, double customWeight, boolean customIsTheCarOn){
        maxSpeed = customMaxSpeed;
        weight = customWeight;
        isTheCarOn = customIsTheCarOn;
    }
    
    public void printVariables(){
        System.out.println("This is the max speed " + maxSpeed);
        System.out.println(minSpeed);
        System.out.println(weight);
        System.out.println(isTheCarOn);
        System.out.println(condition);
        System.out.println(nameOfCar);
        System.out.println(numberOfPeopleInCar);
    }
    
    public void wreckCar(){
        condition = 'C';
    }
    
    public void upgradeMinSpeed(){
        minSpeed = maxSpeed;
        maxSpeed = maxSpeed + 1;
    }
    
    public void getIn(){
        numberOfPeopleInCar++;
    }
    
    public void getOut(){
        numberOfPeopleInCar--;
    }
    
    public double howManyMilesTillOutOfGas(){
        return currentFuel * mpg;
    }
    
    public double maxMilesPerFillUp(){
        return maxFuel * mpg;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Car birthdayPresent = new Car(500, 5000.5, true);
        System.out.println("Birthday car v1");
        birthdayPresent.printVariables();
        birthdayPresent.getIn();
        birthdayPresent.getIn();
        birthdayPresent.getIn();
        System.out.println("Miles left: " + birthdayPresent.howManyMilesTillOutOfGas());
        System.out.println("Max Miles: " + birthdayPresent.maxMilesPerFillUp());
        System.out.println("Birthday car v2");
        birthdayPresent.printVariables();
        birthdayPresent.getOut();
        System.out.println("Birthday present v3");
        birthdayPresent.printVariables();
    }
    
}
